def create_file():
    try:
        with open("toto.txt", "w") as file:
            pass

        print("toto.txt created successfully!")

    except OSError as error:
        print("Error:", error)


create_file()
