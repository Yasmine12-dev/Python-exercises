def new_division(num, den, acc=1):
    if not isinstance(num, (int, float)) or not isinstance(den, (int, float)):
        print("Error: Numerator and denominator must be numbers")
        return

    if den == 0:
        print("Error: Cannot divide by zero")
        return

    if not isinstance(acc, int) or acc < 0:
        print("Error: Accuracy must be a non-negative integer")
        return

    print(f"{num / den:.{acc}f}")


new_division(8.4, 13)
new_division(8.4, 13, 6)
new_division(10, 0)
