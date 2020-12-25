MAX_LEN = 5
list_stack = []


def push(element, array):
    if len(array) < MAX_LEN:
        array.append(element)
        print('Added element to stack')
        print(array)
    else:
        print('Cannot insert element as it is full size now', MAX_LEN - 1)
        return MAX_LEN - 1


def check_empty(array):
    if len(array) - 1 == -1:
        return -1
    else:
        return len(array) - 1


def pop(array):
    try:
        element = list_stack.pop()
    except Exception as e:
        status = check_empty(array)
        if status == -1:
            print('Cannot pop more element as stack is empty')
        return len(list_stack) - 1
    print(list_stack)
    print('Removed element from stack', element)
    status = check_empty(array)
    if status == -1:
        print('Cannot pop more element as stack is empty')
    return element


if __name__ == '__main__':
    print('------Stack Implementation------')
    push(3, list_stack)
    pop(list_stack)
    push(5, list_stack)
    pop(list_stack)
    push(4, list_stack)
    push(2, list_stack)
    push(7, list_stack)
    push(5, list_stack)
    push(1, list_stack)
    push(3, list_stack)
    push(3, list_stack)
    push(3, list_stack)
    push(3, list_stack)
    push(3, list_stack)
    push(3, list_stack)
    push(3, list_stack)
    push(3, list_stack)
    push(3, list_stack)
    push(3, list_stack)
    push(3, list_stack)
    pop(list_stack)
    pop(list_stack)
    pop(list_stack)
    pop(list_stack)
    pop(list_stack)
    pop(list_stack)
    pop(list_stack)
