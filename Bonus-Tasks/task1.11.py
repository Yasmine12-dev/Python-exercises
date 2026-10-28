def my_count(stop, start=0, step=1):
    if not all(isinstance(x, int) for x in (stop, start, step)):
        print("Error: Arguments must be integers")
        return

    if step == 0:
        print("Error: Step cannot be zero")
        return

    if start < stop:
        for number in range(start, stop, abs(step)):
            print(number)

    elif start > stop:
        for number in range(start, stop, -abs(step)):
            print(number)


my_count(10)
print("---")
my_count(100, -100, 42)
print("---")
my_count(-100, 100, -42)
print("---")
my_count(10, 0, 0)
