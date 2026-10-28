animalsCounts = [['cat', 666], ['dog', 3], ['elephant', 42]]

result = sorted(animalsCounts, key=lambda animal: animal[1])

print(result)
