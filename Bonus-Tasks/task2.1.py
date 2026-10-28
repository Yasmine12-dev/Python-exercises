def read_file(filename):
    try:
        with open(filename, "r") as file:
            print(file.read())
    except OSError as error:
        print("Error:", error)


read_file("primes.txt")

