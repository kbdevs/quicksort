import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            yield arr
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    yield arr

    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pivot_index = yield from partition(arr, low, high)
        yield from quicksort(arr, low, pivot_index - 1)
        yield from quicksort(arr, pivot_index + 1, high)

def update_fig(arr, rects):
    colors = plt.cm.viridis(arr)
    for rect, val, color in zip(rects, arr, colors):
        rect.set_height(val)
        rect.set_color(color)

def animate_sort(arr):
    plt.style.use('dark_background')
    fig, ax = plt.subplots()
    ax.set_title("Quicksort")
    bar_rects = ax.bar(range(len(arr)), arr, align="edge")
    anim = animation.FuncAnimation(fig, func=update_fig, fargs=(bar_rects,),
    frames=quicksort(arr, 0, len(arr) - 1),
    interval=1, repeat=False)  # Set interval to 100 milliseconds
    plt.show()

if __name__ == "__main__":
    # Generate a random list of integers
    arr = random.sample(range(1, 101), 100)
    animate_sort(arr)
