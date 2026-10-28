superheroes = {
    "Batman": {
        "id": 1,
        "aliases": ["Bruce Wayne", "Dark knight"],
        "location": {"city": "Gotham"}
    },
    "Superman": {
        "id": 2,
        "aliases": ["Kal-El", "Clark Kent", "The Man of Steel"],
        "location": {"city": "Metropolis"}
    }
}

superheroes["Batman"]["aliases"].append("Caped Crusader")

superheroes["Wolverine"] = {
    "id": 3,
    "aliases": [],
    "location": None
}

print(superheroes)
