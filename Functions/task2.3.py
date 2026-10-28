import os

def list_files(folder):
    print(folder + ":")

    for item in os.listdir(folder):
        path = os.path.join(folder, item)
        print(item)

        if os.path.isdir(path):
            list_files(path)


list_files(".")
