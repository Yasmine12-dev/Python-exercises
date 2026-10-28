def my_division(num, den):
    if not isinstance(num, int) or not isinstance(den, int):
        print("Error: Both arguments must be integers")
        return

    if den == 0:
        print("Error: Cannot divide by zero")
        return

    quotient = num // den
    remainder = num % den

    print(quotient)
    print(remainder)


my_division(42, 4)
my_division(10, 0)
