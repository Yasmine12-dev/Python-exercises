pi = 0

for i in range(999, 0, -2):
    pi = i**2 / (6 + pi)

pi = 3 + pi

print(round(pi, 6))

