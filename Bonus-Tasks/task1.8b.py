def my_sum(*args):
    for number in args:
        if not isinstance(number, (int, float)):
            print("ValueError: All arguments must be numbers")
            return

    print(sum(args))


my_sum(1)
my_sum(1, 2, 3)
my_sum(-20, -10, 5, 5, 10, 10)
my_sum(1, "toto")
