
def fibonacci(n) -> int:
    first_term = 0
    second_term = 1
    if n > 2:
        for i in range(3, n+1):
            next_item = first_term + second_term
            first_term = second_term
            second_term = next_item

    return next_item
    


n = int(input("Enter a number:- "))
print(fibonacci(n))