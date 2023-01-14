def selectionSort(arr):
    n = len(arr)
    for i in range(0, n-1):
        min = i
        for j in range(i, n-1):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]


arr = [1, 2, 3, 5, 4, 2, 1, 6, 7]

selectionSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i])
