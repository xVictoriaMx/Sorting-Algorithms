def selection_sort(arr):
    n = range(0, len(arr)-1)

    for i in n:
        min_value = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_value]:
                min_value = j

        if min_value != i:
            arr[min_value], arr[i] = arr[i], arr[min_value]

    return arr

print(selection_sort([2,3,0,1,7,6,8,4,9,4]))