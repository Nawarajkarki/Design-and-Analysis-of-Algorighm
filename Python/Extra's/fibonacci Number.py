
# def fibonacci(n) -> int:
#     first_term = 0
#     second_term = 1
#     for i in range(3, n+1):
#         next_item = first_term + second_term
#         first_term = second_term
#         second_term = next_item
#     return next_item
# n = int(input("Enter a number:- "))
# print(fibonacci(n))


#---------------- Using Recursion ---------------------------- #

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


n = int(input("Enter a number:- "))
print(fibonacci(n))