numbers_array = [9, 8, 7, 1, 2, 3, 5, 4, 6]


def buble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr



print(buble_sort(numbers_array))