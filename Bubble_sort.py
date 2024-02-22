def bubble(arr):
    n = len(arr) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, n):
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

print(bubble([3,6,7,1,2,0,9,8]))