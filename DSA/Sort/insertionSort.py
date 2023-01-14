def insertionList(arr):
    n = len(arr)
    for i in range(1, n-1):
        min = arr[i]
        j = i-1
        while j >= 0 and min < arr[j]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j+1] = min


arr = [9, 1, 2, 4, 5, 6, 7]
insertionList(arr)
for i in range(len(arr)):
    print("%d" % arr[i])
