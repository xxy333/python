num_list = [1, 10, 12, 4, 3, 2, 3, 21, 30, 5]
def buble_sorter(nums):
    for n in range(len(nums) -1, 0, -1):
        for i in range(n):
            if nums[i] > nums[i + 1]:
                swapped = True
                nums[i], nums[i + 1] = nums[i + 1], nums







buble_sorter(num_list)
print(num_list)






