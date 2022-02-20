def sum_num(*args):
    sum_ = 0
    print(args)
    print(type(args))
    for i in args:
        sum_ += i
    return sum_


def print_kwargs(**kwargs):
    print(kwargs)


if __name__ == '__main__':
    print(sum_num(1, 2, 3, 4, 5))
    print_kwargs(a=1, b=2, c=3, d=4)
