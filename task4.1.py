pi = 0
sign = 1

for i in range(1, 10000000, 2):
    pi = pi + sign * (4 / i)
    sign = -sign

print(round(pi, 6))

