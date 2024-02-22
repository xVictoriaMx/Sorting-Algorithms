
def insertion_sort(arr):
    n = range(1, len(arr))
    for i in n:
        value_to_sort = arr[i]

        while arr[i-1] > value_to_sort and i>0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i = i - 1

    return arr

print(insertion_sort([1,4,5,2,6,8,9,0]))
