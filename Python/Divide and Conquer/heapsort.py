def swap(a, b):
    return b, a

def maxHeap(arr, i, heapsize):
    l = 2 * i + 1
    r = 2 * i + 2
    if l <= heapsize - 1 and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r <= heapsize - 1 and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = swap(arr[i], arr[largest])
        maxHeap(arr, largest, heapsize)

def buildHeap(arr):
    length = len(arr)
    heapsize = length
    for i in range((length//2)-1, -1, -1):
        maxHeap(arr, i, heapsize)

def heapSort(arr):
    buildHeap(arr)
    print("After build max heap:\t", end="")
    print(*arr, sep="\t")
    length = len(arr)
    heapsize = length
    for i in range(length-1, 0, -1):
        arr[0], arr[i] = swap(arr[0], arr[i])
        heapsize -= 1
        maxHeap(arr, 0, heapsize)

def main():
    arr = [8, 9, 2, 5, 7, 1, 19]
    heapSort(arr)
    print("After heap sort:\t", end="")
    print(*arr, sep="\t")

if __name__ == "__main__":
    main()
