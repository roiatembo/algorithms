import math
def search_insert(nums, target):
    start_index = 0
    end_index = len(nums) - 1
    index = 0

    while start_index <= end_index:
        middle = math.floor((start_index+end_index)/2)
        if nums[middle] == target:
            index = middle
            return index
        elif nums[middle] > target:
            end_index = middle -1
        else:
            start_index = middle + 1

    if start_index == 0 and end_index < 0:
        index = 0
    elif nums[end_index] == target:
        index = end_index
    elif nums[end_index] > target:
        index = end_index - 1
    elif nums[end_index] < target:
        index = end_index + 1
    
    return index

nums = [1,4,6,7,8,9]
target = 6

print(search_insert(nums, target))