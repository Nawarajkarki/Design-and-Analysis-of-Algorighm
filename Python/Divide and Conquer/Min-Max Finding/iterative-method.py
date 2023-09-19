def min_max(my_list, len):
    min = my_list[0]
    max = my_list[0]

    for i in range(1, len):
        if my_list[i] > max:
            max = my_list[i]
        if my_list[i] < min:
            min = my_list[i]
    

    return min, max

def main():
    my_list = [5, 8, 7, 4, 2, 9, 12, 13, 11, 23, 1, -1, -23, 34, 545]
    n = len(my_list)

    min, max = min_max(my_list, n)
    print(f"min = {min}, max = {max}")


if __name__ == "__main__":
    main()
