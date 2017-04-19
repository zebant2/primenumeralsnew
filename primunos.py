__author__ = 'HP'


def prime_numbers(num):
    """Function that generates prime numbers from 0 to n(given number)"""

    prime_nums = []

    if num in (0, 1):
        return "You know '0' and '1' are not Prime numbers smh"
    if num < 2:
        return "Anything less than 2 is not possible to generate prime numbers."
    if type(num) != int:
        return "Integers are the only data types allowed."

    for i in range(2, num + 1):
        if i > 1:
            for p in range(2, i):
                if (i % p) == 0:
                    break
            else:
                prime_nums.append(i)
    return prime_nums

print(prime_numbers(99))