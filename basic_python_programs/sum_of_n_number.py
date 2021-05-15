
try:
    n = int(input('Enter a number: '))
except Exception as e:
    print('Enter a valid Number')
    n = None
if n:
    result = n * (n+1) / 2
    print(int(result), 'Units of work')
