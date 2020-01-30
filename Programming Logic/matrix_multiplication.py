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
    result = mat_1 * mat_2
    print(result)
    return result


matrix_multiplication()
