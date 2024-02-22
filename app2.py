import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time

# Bubble Sort Algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                yield arr

# Merge Sort Algorithm
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        yield arr

# Insertion Sort Algorithm
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            yield arr
        arr[j+1] = key
        yield arr

# Selection Sort Algorithm
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr

# Quick Sort Algorithm
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            yield arr
    arr[i+1], arr[high] = arr[high], arr[i+1]
    yield arr
    return i + 1

def quick_sort_helper(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        yield from quick_sort_helper(arr, low, pi - 1)
        yield from quick_sort_helper(arr, pi + 1, high)

def quick_sort(arr):
    yield from quick_sort_helper(arr, 0, len(arr) - 1)

# def visualize_sorting_algorithm(sort_algorithm, arr, ax):
#     for state in sort_algorithm(arr):
#         ax.clear()
#         ax.bar(range(len(arr)), arr, color='lightblue')
#         plt.pause(0.01)
    
def anim_sorting_algorithm(algorithm, array, ax):
    def update(frame):
        ax.clear()
        if frame < len(animation_frames):
            ax.bar(range(len(array)), animation_frames[frame], color='lightblue')

    animation_frames = list(algorithm(array.copy()))
    ani = animation.FuncAnimation(plt.gcf(), update, frames=len(animation_frames), repeat=False)
    plt.pause(0.01)
    

def main():
    st.title('Sorting Algorithm Visualization')

    num_columns = 3
    arr = np.random.randint(1, 100, 20)

    sorting_algorithms = {
        "Bubble Sort": bubble_sort,
        "Merge Sort": merge_sort,
        "Insertion Sort": insertion_sort,
        "Selection Sort": selection_sort,
        "Quick Sort": quick_sort
    }

    for algorithm_name, algorithm in sorting_algorithms.items():
        st.write(f"## {algorithm_name}")
        col1, col2, col3 = st.columns(num_columns)
        plt.figure(figsize=(8, 4))
        ax = plt.subplot()
        anim_sorting_algorithm(algorithm, arr.copy(), ax)
        col1.pyplot(plt)
        col2.pyplot(plt)
        col3.pyplot(plt)

if __name__ == "__main__":
    main()
