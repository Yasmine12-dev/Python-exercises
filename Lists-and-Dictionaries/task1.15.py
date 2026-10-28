numbers = [42, 3, 4, 18, 3, 10]

result = [x // 2 if x % 2 == 0 else x * 2 for x in numbers]

print(result)
