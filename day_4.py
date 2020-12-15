def get_input():
    input = []
    with open("day_4.txt") as f:
        for line in f:
            vals = line.replace(' ', ':').split(':')
            for val in vals:
                input.append(val.rstrip('\n'))
    return input


valid_fields = {
    'byr': 1,
    'iyr': 1,
    'eyr': 1,
    'hgt': 1,
    'hcl': 1,
    'ecl': 1,
    'pid': 1,
    'cid': 0
}


def data_clean():
    passports = get_input()
    passports.append('')
    passport_list = []
    passport_dict = {}
    i = 0
    while i < len(passports):
        if passports[i] != 'cid':
            passport_dict[passports[i]] = passports[i + 1]
        i += 2
        if i < len(passports) and passports[i] == '':
            i += 1
            passport_list.append(passport_dict)
            passport_dict = {}

    return passport_list


def valid_passport_info(passport):
    for key, value in passport.items():
        if key == 'byr' and (int(value) < 1920 or int(value) > 2002):
            return False
        if key == 'iyr' and (int(value) < 2010 or int(value) > 2020):
            return False
        if key == 'eyr' and (int(value) < 2020 or int(value) > 2030):
            return False
        if key == 'hgt':
            if value[-2:] != 'in' and value[-2:] != 'cm':
                return False
            if value[-2:] == 'in' and (int(value[:-2]) < 59 or int(value[:-2]) > 76):
                return False
            if value[-2:] == 'cm' and (int(value[:-2]) < 150 or int(value[:-2]) > 193):
                return False
        if key == 'hcl' and (value[0] != '#' or not value[1:].isalnum() or len(value) != 7):
            return False
        if key == 'ecl' and value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return False
        if key == 'pid' and (len(value) != 9):
            return False
    return True


def validate_passports():
    passports = data_clean()
    valid_passports = []
    for passport in passports:
        if len(passport.keys()) == 7 and valid_passport_info(passport):
            valid_passports.append(passport)

    return len(valid_passports)


if __name__ == '__main__':
    print(validate_passports())
