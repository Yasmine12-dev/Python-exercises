def my_count(stop, start=0):
    if not isinstance(stop, int) or not isinstance(start, int):
        print("Error: Arguments must be integers")
        return

    if start <= stop:
        for number in range(start, stop + 1):
            print(number)
    else:
        for number in range(start, stop - 1, -1):
            print(number)


my_count(5)
print("---")
my_count(5, 2)
