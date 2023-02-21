def remove_duplicates(nums):
    for j in range(1, len(nums)):
        i = j -1
        if nums[i] == nums[j]:
            temp = nums[i]
            nums.pop(i)
            nums.append(temp)

    return nums


nums = [1,1,2]
print(remove_duplicates(nums))