import copy
import sys

import numpy as np

mat_1 = np.array(
    [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9)
    ]
)

mat_2 = np.array(
    [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9)
    ]
)


def matrix_multiplication():
    f_result = mat_1 * mat_2
    print(f_result)
    return f_result


def take_input():
    print('Taking input for matrix A')
    for i in range(0, number_of_rows_a):
        temp_list = []
        for j in range(0, number_of_cols_a):
            temp_list.append(int(input()))
        list_a.append(temp_list)

    print('Taking input for matrix B')
    for i in range(0, number_of_rows_b):
        temp_list = []
        for j in range(0, number_of_cols_b):
            temp_list.append(int(input()))
        list_b.append(temp_list)


def matrix_multiplication_traditional():
    if number_of_cols_a == number_of_rows_b:
        print('Taking input')
        take_input()
        resulting_matrix = f'{number_of_rows_a} x {number_of_cols_b}'
        print(resulting_matrix)
        for i in range(0, number_of_rows_a):
            for j in range(0, number_of_cols_b):
                c[i][j] = 0
                for k in range(number_of_rows_b):
                    c[i][j] += (list_a[i][k] * list_b[k][j])
        return c

    else:
        print('Invalid input for matrix cannot multiply it ')
        sys.exit(1)


if __name__ == '__main__':
    number_of_rows_a = int(input('Rows for A: '))
    number_of_cols_a = int(input('Cols for A: '))
    number_of_rows_b = int(input('Rows for B: '))
    number_of_cols_b = int(input('Cols for B: '))

    list_a = []
    list_b = []
    c = [
        [0 for _ in range(number_of_rows_a)]  # create row having n number of rows
        for _ in range(number_of_cols_b)  # repeat this step until n number_of_cols
    ]

    result = matrix_multiplication_traditional()
    print(result)

    # matrix_multiplication()
