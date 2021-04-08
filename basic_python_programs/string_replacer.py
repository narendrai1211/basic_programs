import sys
import re


def replacer(string_):
    # print(type(string_input))
    try:
        final_string = str(string_)
        final_string = re.sub(r'[^0-9]', '', final_string)
        s = re.sub("\d", "#", final_string)
        return s
    except Exception as e:
        print('not a valid string')
        return 'Error processing string not a valid string'


if __name__ == '__main__':
    string_input = sys.argv[1]
    result = replacer(string_input)
    print(result)
