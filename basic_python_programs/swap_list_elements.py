from collections import Counter

if __name__ == '__main__':
    l_ = [1, 2, 3]
    l_[0], l_[-1] = l_[-1], l_[0]
    print(l_)
    input_ = 'the quick brown fox jumps over the lazy dog'
    list_ele = input_.split(' ')
    list_ele.reverse()
    # print(list_ele)
    output_string = ' '.join(list_ele)
    print(output_string)

    d = Counter(input_)
    d = list(dict(d).keys())
    d.sort()
    print(d)
    print(len(d))
