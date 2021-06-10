def binary_search(arr, low, high, x):
    print(low, high, 'Low and Mid trace')
    binary_search.counter += 1
    if high >= low:
        mid = (high + low) // 2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x = 4
    binary_search.counter = 0

    # Function call
    result = binary_search(arr, 0, len(arr) - 1, x)
    print('number of iterations', binary_search.counter)
    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("Element is not present in array")
