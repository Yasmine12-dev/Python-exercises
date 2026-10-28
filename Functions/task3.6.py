names = ["Joe", "William", "Jack", "Averell"]

print("Shortest to longest:", sorted(names, key=len))
print("Longest to shortest:", sorted(names, key=len, reverse=True))
