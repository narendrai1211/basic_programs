def bubble_sort(list_e, total_size):

    for i in range(0, total_size - 1):
        # print('Pass -- ', i)
        # going through each element
        # why 2 for loops -- for number of passes -- outer loop runs n - 1 times because,
        # we do n-1 passes per iteration in bubble sort -- standard rule
        print('j will start from .. 0 to ', total_size - 1 - i)
        for j in range(0, total_size - 1 - i):
            print(f'value of j is .. {j}')
            if list_e[j] > list_e[j+1]:
                temp = list_e[j]
                list_e[j] = list_e[j+1]
                list_e[j+1] = temp
    return list_e


if __name__ == '__main__':
    list_ = [4, 1, 41, 2]
    arr_size = len(list_)
    bubble_sort(list_, arr_size)
