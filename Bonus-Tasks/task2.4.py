def count_lines(filename):
    try:
        with open(filename, "r") as file:
            total = sum(1 for line in file)

        print(filename, "contains", total, "lines")

    except OSError as error:
        print("Error:", error)


count_lines("zen.txt")
count_lines("primes.txt")
