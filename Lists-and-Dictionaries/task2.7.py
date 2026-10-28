types = {
    "Electric": ["Pikachu"],
    "Grass": ["Bulbasaur", "Leafeon"],
    "Fire": ["Charmander", "Scovillain"]
}

# Method 1: Using a loop
for pokemon_type, pokemons in types.items():
    if "Pikachu" in pokemons:
        print("Method 1:", pokemon_type)

# Method 2: Using next()
result = next(
    (pokemon_type for pokemon_type, pokemons in types.items()
     if "Pikachu" in pokemons),
    "Not found"
)

print("Method 2:", result)
