def remove_element(nums, val):
    while val in nums:
        nums.remove(val)

    return f"{len(nums)}, nums = {nums}"

nums = [3,2,2,3]
val = 3

print(remove_element(nums, val))