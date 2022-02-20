def fuel_calc(input_array):
    fuel = 0
    initial_fuel = 0
    for i in range(0, len(input_array)):
        fuel += input_array[i]
        if fuel <= 0:
            print(fuel)
            initial_fuel += 1
            fuel += 1

        if fuel < 1:
            print(f'Elif {fuel}')
            initial_fuel += 1
            fuel += 1
        else:
            pass
    return initial_fuel
    # pass


if __name__ == '__main__':
    arr = [5, 2, -8, 3, 6]
    fuel_calc(arr)
