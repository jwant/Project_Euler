# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28
# is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is
# called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum
# of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can
# be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis
# even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less
# than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers

# def sum_of_factors(number)

import math
from functools import reduce
import operator

# note
# every multiple of an abundant number is abundant
# every multiple of a perfect number is abundant
def get_abundant_numbers(r):
    numbers = []
    for i in range(2, r):
        if i in numbers:jnn
            continue

        sum = sum_of_factors(i)
        if sum > i:
            numbers.append(i)
            multiples = i * 2
            while multiples < r:
                numbers.append(multiples)
                multiples += i

        if sum == i:
            multiples = i * 2
            while multiples < r:
                numbers.append(multiples)
                multiples += i

def sum_of_factors(n):
    return 'Sum_of_factors'

# is_abundant: s > i

r = 28123
abundant_numbers = get_abundant_numbers(r)

print(abundant_numbers)