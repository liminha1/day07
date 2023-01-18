# Closres
#
# def calculate():
#     x = 1
#     y = 2
#     temp = 0
#     def add_sub(n):
#         nonlocal temp
#         # x = 11  # local variable
#         temp = temp + x + n -y
#         return temp
#     return add_sub
#
#
# c1 = calculate()
# for i in range(5):
#     print(c1(i))
#
# print(type(c1))
# print(c1)

# Lambda
import random

# function as parameter
# def process(no_list, f):
#     for no in no_list:
#         print(f(no))
# def squares(n):
#     """
#     제곱 함수
#     :param n: integer
#     :return:  integer
#     """
#     return n * n
#
# numbers = [random.randint(1, 100) for i in range(5)]
# print(numbers)
# process(numbers, squares)

def process(no_list, f):
    for no in no_list:
        print(f(no))


numbers = [random.randint(1, 100) for i in range(5)]
print(numbers)
process(numbers, lambda x: x * x)