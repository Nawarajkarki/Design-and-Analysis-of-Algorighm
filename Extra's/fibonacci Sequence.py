## ------------------- For fibonacci Sequence ---------------
# def fibonacci(n) -> list:
#     fibonacci_list = [0, 1]
#     first_term = 0
#     second_term = 1
#     if n > 2:
#         for i in range(3, n+1):
#             next_item = first_term + second_term
#             first_term = second_term
#             second_term = next_item
#             fibonacci_list.append(next_item)
#     return fibonacci_list
# n = int(input("Enter a number:- "))
# print(fibonacci(n))



#---------------- Using Recursion ---------------------------- #


def fibonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0,1]
    else:
        fib_list = fibonacci(n - 1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list

n = int(input("Enter a number: "))
fib_series = fibonacci(n)
print("Fibonacci series up to", n, ":", fib_series)

