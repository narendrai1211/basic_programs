import random

DIGITS = [str(i) for i in range(0, 10)]

LOWERCASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
             'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
             'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
             'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<', '^', '&', '-', '+', str('\\'), '`', '"', '\'']


def pass_gen(cnt):
    print('Please enter length of each password ... ')
    num_chars = input(f'Enter length of password minimum 8 characters {cnt + 1}:')
    password_ = ''
    for i in range(0, int(num_chars)):
        password_ = password_ + random.choice(combined_list)
    set_passwords.add(password_)
    with open(fname, 'w') as f:
        for i_pwd in set_passwords:
            f.write(i_pwd + '\n')


if __name__ == '__main__':
    pwd_cnt = input('How many passwords do you want to generate? : ')
    fname = 'passwords_generated.txt'
    set_passwords = set()
    combined_list = LOWERCASE + DIGITS + UPCASE_CHARACTERS + SYMBOLS
    for _ in range(0, int(pwd_cnt)):
        pass_gen(_)
    print(f'Please check the file {fname}')
