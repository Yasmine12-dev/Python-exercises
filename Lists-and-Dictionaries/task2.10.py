superheroes = {
    "Batman": {
        "aliases": ["Bruce Wayne", "Dark knight", "Caped Crusader"]
    },
    "Superman": {
        "aliases": ["Kal-El", "Clark Kent", "The Man of Steel"]
    },
    "Wolverine": {
        "aliases": []
    }
}

for name, information in superheroes.items():
    print(name + ":")

    if information["aliases"]:
        for alias in information["aliases"]:
            print(alias)
    else:
        print("No aliases found.")

    print()
