
# df_ = df[df['sal'] > 3000]

# n1 = 10  # 10
# n2 = n1  # 10
# n1 *= 2  # n1 = n1 * 2
# print(n2)
#
s = 'narendra@gmail.com'

part_1 = s.split('@')[0]
part_2 = s.split('@')[-1]
part_3 = part_2.split('.')[0]
part_4 = part_2.split('.')[-1]


def str_replacer(part_1):
    total_len = len(part_1)
    list_ = []

    for i in range(1, total_len - 1):
        char_ = s[i].replace(s[i], '*')
        list_.append(char_)

    return list_


list_1 = str_replacer(part_1)
list_2 = str_replacer(part_3)

final_ = part_1[0] + ''.join(list_1) + part_1[-1] + '@' + part_3[0] + ''.join(list_2) + '.' + part_4

print(final_)

# #
# #     # print(list_)
# #
# # list_1 = str_replacer(part_1)
# # list_2 = str_replacer(part_3)
# #
# #
# # print(final_)
# #
# # #
# # #
# # #
# # # # print(total_len)
# # # # for i in range(1, total_len - 2):
# # # #     d = part_1.replace(part_1[i], '*')
# # #
# # # # middle_part = '' + part_1.replace(part_1[1], '*')
# # # # middle_part = part_1.replace(part_1[0], '') + part_1.replace(part_1[-1], '')
# # # # print(middle_part)
# # #
# # # to_keep = part_1[0] + middle_part + part_1[-1] + '@' + '.' + part_3
# # #
# # # # print(to_keep)
# # #
# # # # middle_part = part_1.replace(part_1[1:-2], '*')
# # #
# # #
# # # # n******a@g****.com
# # #
