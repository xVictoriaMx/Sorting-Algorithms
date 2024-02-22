import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            yield arr
        arr[j + 1] = key
        yield arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        yield from merge_sort(L)
        yield from merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            yield arr

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            yield arr

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            yield arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            yield arr
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    yield arr
    return i + 1

def quick_sort_helper(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        yield from quick_sort_helper(arr, low, pi - 1)
        yield from quick_sort_helper(arr, pi + 1, high)

def quick_sort(arr):
    yield from quick_sort_helper(arr, 0, len(arr) - 1)


def animate_sorting_algorithm(algorithm, arr):
    fig, ax = plt.subplots()
    ax.set_title(f"{algorithm.__name__} Sorting")
    bar_rects = ax.bar(range(len(arr)), arr, color='lightblue')

    def update_fig(arr, rects):
        for rect, val in zip(rects, arr):
            rect.set_height(val)

    anim = animation.FuncAnimation(fig, func=update_fig, fargs=(bar_rects,), frames=algorithm(arr.copy()),
                                   repeat=False)
    plt.show()

arr = np.random.randint(1, 100, 20)

animate_sorting_algorithm(insertion_sort, arr.copy())
animate_sorting_algorithm(merge_sort, arr.copy())
animate_sorting_algorithm(selection_sort, arr.copy())
animate_sorting_algorithm(bubble_sort, arr.copy())
animate_sorting_algorithm(quick_sort, arr.copy())