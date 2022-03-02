# one base case is needed whenever we need recursion

# 1
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


# n = int((input()))
# print(factorial(n))


# 2 Math behind Recursion
# Based on PrincipalofMathematicalInduction
# We assume that result is true for (n-1) and we write code for n assuming it. While we keep our basecase where the expression is proved tp be true, i.e., (0!) = (1)

# 3.
# i. Find sum of n natural numbers
def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)


# n = int((input()))
# print(sum(n))

# 4


def pow_n(x, n):
    if n == 0:
        return 1
    return x*pow_n(x, n-1)


x = int((input()))
n = int((input()))
print(pow_n(x, n))
