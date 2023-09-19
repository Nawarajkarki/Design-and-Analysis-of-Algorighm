def mergeSort(a, p, r):
    if p < r:
        q = (p + r) // 2       # Here // is used to insure the integer division
        mergeSort(a, p, q)
        mergeSort(a, q + 1, r)
        merge(a, p, q, r)

def merge(a, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    list1 = [0] * (n1 + 1)    # Creates a List with n1+1 elements, with all elemenets being Zero (0)
    list2 = [0] * (n2 + 1)    # Creates a List with n1+1 elements, with all elemenets being Zero (0)

    for i in range(n1):
        list1[i] = a[p + i]

    for j in range(n2):
        list2[j] = a[q + j + 1]

    list1[n1] = float('inf')           # Assigning infinity to the list[n1]
    list2[n2] = float('inf')
    i = 0
    j = 0

    for k in range(p, r + 1):
        if list1[i] <= list2[j]:
            a[k] = list1[i]
            i = i + 1
        else:
            a[k] = list2[j]
            j = j + 1


def main():
    my_list = [5, 8, 7, 4, 2, 9, 12, 13, 11, 23, 1, -1, -23,34,545]
    n = len(my_list)

    mergeSort(my_list, 0, n - 1)
    print(my_list)


if __name__ == '__main__':
    main()