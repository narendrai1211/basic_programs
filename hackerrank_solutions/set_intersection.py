if __name__ == '__main__':
    len_a = int(input())
    a = set(input().split())
    len_b = int(input())
    b = set(input().split())

    c = a.intersection(b)
    print(len(c))


# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
