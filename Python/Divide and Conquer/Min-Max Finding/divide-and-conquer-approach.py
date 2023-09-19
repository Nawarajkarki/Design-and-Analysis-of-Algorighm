def min_max(my_list, p, r):

    if (p == r):
        max = min = my_list[p]
    
    elif (p == r-1):
        if my_list[p] < my_list[r]:
            max = my_list[r]
            min = my_list[p]
        else:
            max = my_list[p]
            min = my_list[r]
    

    else:
        # Divide the problem in half
        mid = (p + r) // 2   # Integer division

        min1, max1 = min_max(my_list, p, mid)

        min, max = min_max(my_list, mid+1, r)
        if max1 > max:
            max = max1
        if min1 < min:
            min = min1

    
    return min, max


def main():
    my_list = [5, 8, 7, 4, 2, 9, 12, 13, 11, 23, 1, -1, -23, 34, 545]
    l = len(my_list)
    min, max = min_max(my_list, 0, l-1)
    print(f"min = {min}, max = {max}")


if __name__ == "__main__":
    main()
