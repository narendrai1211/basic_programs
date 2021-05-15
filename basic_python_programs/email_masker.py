def str_replacer(string_):
    total_len = len(string_)
    list_ = []
    for i in range(1, total_len - 1):
        char_ = s[i].replace(s[i], '*')
        list_.append(char_)
    return list_


if __name__ == '__main__':
    s = 'narendra@example.com'
    email_split = s.split('@')
    part_1 = email_split[0]
    part_2 = email_split[-1]
    dot_split = part_2.split('.')
    part_3 = dot_split[0]
    part_4 = dot_split[-1]
    list_1 = str_replacer(part_1)
    list_2 = str_replacer(part_3)
    final_ = part_1[0] + ''.join(list_1) + part_1[-1] + '@' + part_3[0] + ''.join(list_2) + '.' + part_4
    print(final_)
