n = int(input("Enter an integer: "))

if n == 42:
    print("a", end="")

if n <= 21:
    print("b", end="")

if n % 2 == 0:
    print("c", end="")

if n / 2 < 21:
    print("d", end="")

if n % 2 != 0 and n >= 45:
    print("e", end="")

if n != 42 and n > 21 and n % 2 != 0 and n / 2 >= 21 and not (n >= 45):
    print("f", end="")

print()
# end is for no space 
#if: Python checks every condition, even if a previous one was true.
#elif: Python checks the next condition only if all previous conditions were false.
