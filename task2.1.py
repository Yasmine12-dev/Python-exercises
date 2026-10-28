for n in [9, 10, 11]:
    total = 0

    for i in range(1, n + 1):
        total += int("1" * i)

    print("Sum:", total)

    for power in range(2, 6):
        print("Power", power, ":", total ** power)

    print()
