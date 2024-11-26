given_array = [3, 2, 5, 1, 3, 5, 6, 10, 20, 11]
def buble_sort(arr):
    for i, array_number in enumerate(arr):
        if array_number[i] > array_number[i+1]:
            lower = array_number[i]
            higher = array_number[i+1]
            print(array_number[i], array_number[i+1])

print(lo

