import time

def power(base, exponent):
    result = 1

    for i in range(exponent):
        result = result * base

    return result


start = time.time()
print("42^84 =", power(42, 84))
print("Time:", time.time() - start, "seconds")

print()

start = time.time()
print("42^168 =", power(42, 168))
print("Time:", time.time() - start, "seconds")
