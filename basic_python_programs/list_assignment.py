
def equalise(list_1, list_2):
    factor = 0
    while len(list_1) != len(list_2):
        if len(list_1) < len(list_2):
            list_1.append('added')
            factor += 1
        else:
            list_2.append('added')
            factor += 1
    print('Factor is ', factor)
    return factor


def do_operation(l1, l2, factor):
    for i, j in zip(l1, l2):
        print(i, j)
        output_list.append(i)
        output_list.append(j)
# cleaning the output
    while factor != 0:
        output_list.remove('added')
        factor = factor - 1
    print(output_list)


if __name__ == '__main__':
    l1_ = [1, 2]
    l2_ = [5, 8, 9, 10]
    output_list = []
    factor_ = equalise(l1_, l2_)
    do_operation(l1_, l2_, factor_)


