def vending_machine_simulator():
    stock = 100
    while True:
        req = int(input('How many candies do you want? '))
        if req > stock:
            print('sorry, we are out of stock')
            break
        else:
            for i in range(1, req+1):
                print('Candy ', i)
            stock = stock - req
            print("stock = ", stock)


vending_machine_simulator()
