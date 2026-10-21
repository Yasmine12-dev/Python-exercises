n = "123456789"
total = 0

for digit in n:
    total = total + int(digit)

print("The sum of digits is:", total)


#Use the same code to calculate the sum of the digits of 112233445566778899.

n = "112233445566778899"
total = 0

for digit in n:
    total = total + int(digit)

print("The sum of digits is:", total)

#Use the same code to calculate the sum of the digits of 123456789 ∗ 987654321.
n = 123456789
a = 987654321

result = n * a
total = 0

for digit in str(result):
    total = total + int(digit)

print("The sum of digits is:", total)
