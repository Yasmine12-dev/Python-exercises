superheroes = {
    "Batman": {
        "id": 1,
        "aliases": ["Bruce Wayne", "Dark knight"],
        "location": {
            "number": 1007,
            "street": "Mountain Drive",
            "city": "Gotham"
        }
    },
    "Superman": {
        "id": 2,
        "aliases": ["Kal-El", "Clark Kent"],
        "location": {
            "number": 344,
            "street": "Clinton Street",
            "city": "Metropolis"
        }
    }
}

print(superheroes["Superman"]["location"]["city"])
