def write():
    try:
        with open("toto.txt", "a") as file:
            file.write("I'm a new line\n")

        print("Text added successfully!")

    except OSError as error:
        print("Error:", error)


write()
