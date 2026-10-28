list1 = [1, 1, 1, 1, 2, 2, 2, 2, 2]
list2 = [42, "42", 42.0, 21 + 21, 42 * 10 / 10]

result1 = list(set(list1))
result2 = list(set(list2))

print(result1)
print(result2)
