def rewrite():
    try:
        with open("zen.txt", "r") as source:
            content = source.read()

        with open("toto.txt", "w") as destination:
            destination.write(content)

        print("toto.txt now contains the Zen of Python!")

    except OSError as error:
        print("Error:", error)


rewrite()
