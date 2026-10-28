def read_line(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                print(line, end="")
    except OSError as error:
        print("Error:", error)


read_line("zen.txt")
