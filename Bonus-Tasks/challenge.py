ones = [
    "", "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine"
]

teens = [
    "ten", "eleven", "twelve", "thirteen", "fourteen",
    "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
]

tens = [
    "", "", "twenty", "thirty", "forty", "fifty",
    "sixty", "seventy", "eighty", "ninety"
]


def number_to_words(n):
    if n < 10:
        return ones[n]

    if n < 20:
        return teens[n - 10]

    if n < 100:
        return tens[n // 10] + ones[n % 10]

    if n < 1000:
        result = ones[n // 100] + "hundred"

        if n % 100 != 0:
            result += "and" + number_to_words(n % 100)

        return result

    if n == 1000:
        return "onethousand"

    raise ValueError("Only numbers from 1 to 1000 are supported")


def count_letters(N):
    total = 0

    for number in range(1, N + 1):
        total += len(number_to_words(number))

    return total


print("N = 5:", count_letters(5))
print("N = 42:", count_letters(42))
print("N = 1000:", count_letters(1000))
