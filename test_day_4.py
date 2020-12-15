import pytest
from day_4 import valid_passport_info


def test_byr():
    test1 = {'byr': '1919'}
    assert valid_passport_info(test1) is False
    test2 = {'byr': '1920'}
    assert valid_passport_info(test2) is True
    test3 = {'byr': '1950'}
    assert valid_passport_info(test3) is True
    test4 = {'byr': '2002'}
    assert valid_passport_info(test4) is True
    test5 = {'byr': '2003'}
    assert valid_passport_info(test5) is False

def test_iyr():
    test1 = {'iyr': '2009'}
    assert valid_passport_info(test1) is False
    test2 = {'iyr': '2010'}
    assert valid_passport_info(test2) is True
    test3 = {'iyr': '2015'}
    assert valid_passport_info(test3) is True
    test4 = {'iyr': '2020'}
    assert valid_passport_info(test4) is True
    test5 = {'iyr': '2021'}
    assert valid_passport_info(test5) is False

def test_eyr():
    test1 = {'eyr': '2019'}
    assert valid_passport_info(test1) is False
    test2 = {'eyr': '2020'}
    assert valid_passport_info(test2) is True
    test3 = {'eyr': '2025'}
    assert valid_passport_info(test3) is True
    test4 = {'eyr': '2030'}
    assert valid_passport_info(test4) is True
    test5 = {'eyr': '2011'}
    assert valid_passport_info(test5) is False

def test_hgt():
    test1 = {'hgt': '179'}
    assert valid_passport_info(test1) is False
    test2 = {'hgt': '149cm'}
    assert valid_passport_info(test2) is False
    test3 = {'hgt': '150cm'}
    assert valid_passport_info(test3) is True
    test4 = {'hgt': '170cm'}
    assert valid_passport_info(test4) is True
    test5 = {'hgt': '193cm'}
    assert valid_passport_info(test5) is True
    test6 = {'hgt': '194cm'}
    assert valid_passport_info(test6) is False
    test7 = {'hgt': '58in'}
    assert valid_passport_info(test7) is False
    test8 = {'hgt': '59in'}
    assert valid_passport_info(test8) is True
    test9 = {'hgt': '70in'}
    assert valid_passport_info(test9) is True
    test10 = {'hgt': '76in'}
    assert valid_passport_info(test10) is True
    test11 = {'hgt': '77in'}
    assert valid_passport_info(test11) is False

def test_hcl():
    test1 = {'hcl': '000000'}
    assert valid_passport_info(test1) is False
    test2 = {'hcl': '0000!0'}
    assert valid_passport_info(test2) is False
    test3 = {'hcl': '#000000'}
    assert valid_passport_info(test3) is True
    test4 = {'hcl': '#123abc'}
    assert valid_passport_info(test4) is True
    test5 = {'hcl': '#123ab'}
    assert valid_passport_info(test5) is False

def test_ecl():
    test1 = {'ecl': 'zzz'}
    assert valid_passport_info(test1) is False
    test2 = {'ecl': 'blu'}
    assert valid_passport_info(test2) is True
    test3 = {'ecl': 'z'}
    assert valid_passport_info(test3) is False
    test4 = {'ecl': 'grt'}
    assert valid_passport_info(test4) is False

def test_pid():
    test1 = {'pid': '00000000'}
    assert valid_passport_info(test1) is False
    test2 = {'pid': '000000000'}
    assert valid_passport_info(test2) is True
    test3 = {'pid': '0000000000'}
    assert valid_passport_info(test3) is False

def test_dicts():
    test1 = {'byr': '1980', 'hgt': '171cm', 'eyr': '2021', 'pid': '9435249395', 'ecl': 'oth', 'hcl': '#a97842', 'iyr': '2017'}
    assert valid_passport_info(test1) is False