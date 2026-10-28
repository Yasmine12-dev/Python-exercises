def ship(*args, **kwargs):
    print(" ".join(args))

    for key, value in kwargs.items():
        print(f"{key}: {value}")


ship("Batman", street="Mountain Drive", city="Gotham")

print("---")

ship(
    "Superman",
    "The man of steel",
    apartment="3D",
    num=344,
    street="Clinton Street",
    city="Metropolis"
)
