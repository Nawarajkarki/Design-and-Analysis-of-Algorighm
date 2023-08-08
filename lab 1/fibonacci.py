def fibonacci(n) -> list:
    fibonacci_list = [0, 1]
    first_term = 0
    second_term = 1
    if n > 2:
        for i in range(3, n+1):
            next_item = first_term + second_term
            first_term = second_term
            second_term = next_item
            fibonacci_list.append(next_item)

    return fibonacci_list
    


n = int(input("Enter a number:- "))
print(fibonacci(n))