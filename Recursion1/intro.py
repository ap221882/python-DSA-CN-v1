# one base case is needed whenever we need recursion

# 1


from pickle import TRUE


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


# x = int((input()))
# print_n_to_1(x)


# 8
# nth Fibonacci sum -- 1,1,2,3,5,...
# fib(n)=fib(n-1)+fib(n-2)
# TWO BASE CASES NEEDED
def fib(n):
    if n == 2:
        return 1
    if n == 1:
        return 1
    fib_n_1 = fib(n-1)
    fib_n_2 = fib(n-2)
    output = fib_n_1+fib_n_2
    return output


# x = int((input()))
# print(fib(x))


# 10
# import sys
# sys.setrecursionlimit(3000)


# 11
def is_sorted(my_list):
    l = len(my_list)
    if l == 0 or l == 1:
        return True
    if my_list[0] > my_list[1]:
        return False
    else:
        return is_sorted(my_list[1:])
        # isSmallerListSorted = is_sorted(my_list[1:])
    # if isSmallerListSorted:
    #     return True
    # else:
    #     return False


print(is_sorted([2, 3, 4, 5, 1, 2, 3, 3, 9]))
print(is_sorted([1, 2, 3]))


# 12
# Sum of array recursively
def sum_of_array(arr):
    l = len(arr)
    if l == 0:
        return 0
    if l == 1:
        return arr[0]
    return arr[0] + sum_of_array(arr[1:])

# break from between
# def sum_of_array2(arr):
#     l = len(arr)
#     if l == 0:
#         return 0
#     if l == 1:
#         return arr[0]
#     return arr[0] + sum_of_array(arr[1:])


print(sum_of_array([1, 2, 5, 6, 0, 6, 6, ]))

# 13


def check_number_in_array(x, arr):
    l = len(arr)
    if l == 0:
        return 'Not found'
    if l == 1:
        if arr[0] == x:
            return 'Found'
        else:
            return 'Not found'
    findFirst = (arr[0] == x)
    findRestArray = check_number_in_array(x, arr[1:])
    return findFirst or findRestArray


print(check_number_in_array(1, [2, 4, 5, 6, 1])
      )


# 14
def isSortedBetter(arr, si):
    l = len(arr)
    # si=0
    if si == l or si == l-1:
        return True
    if arr[si] > arr[si+1]:
        return False
    else:
        return isSortedBetter(arr, si+1)


print(isSortedBetter([2, 3, 4, 5, 1, 2, 3, 3, 9], 0))
print(isSortedBetter([2, 3], 0))
