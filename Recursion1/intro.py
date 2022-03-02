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


# x = int((input()))
# n = int((input()))
# print(pow_n(x, n))


# 6
def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n-1)
    print(n)
    return


# x = int((input()))
# print_1_to_n(x)


def print_n_to_1(n):
    if n == 0:
        return
    print(n)
    print_n_to_1(n-1)
    return


x = int((input()))
print_n_to_1(x)


# 8
# nth Fibonacci sum -- 1,1,2,3,5,...
# fib(n)=fib(n-1)+fib(n-2)
def fib(n):
    if n == 1:
        return 1
    fib_n_1 = fib(n-1)
