import random
import time

start = time.time()

numbers = [random.randint(1, 1000000) for i in range(1000000)]

numbers.sort()

print("First 10:", numbers[:10])
print("Last 10:", numbers[-10:])
print("Time:", time.time() - start)
