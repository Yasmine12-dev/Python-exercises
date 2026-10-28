def read_lines(*numbers):
    try:
        with open("primes.txt", "r") as file:
            lines = file.readlines()

        for number in numbers:
            if not isinstance(number, int) or number < 1 or number > len(lines):
                print("Error: Invalid line number:", number)
            else:
                print(lines[number - 1].strip())

    except OSError as error:
        print("Error:", error)


read_lines(1, 42, 666, 20000)
