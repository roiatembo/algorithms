def search_range(nums, target):
    nums_dict = {}
    for i in range(0, len(nums)):
        if nums[i] not in nums_dict:
            nums_dict[nums[i]] = [i]
        else:
            nums_dict[nums[i]].append(i)
        
    try:
        target_list = nums_dict[target]

        if len(target_list) > 2:
            final_list = [target_list[0], target_list[-1]]
        else:
            final_list = target_list
    except:
        final_list = [-1,-1]

    return final_list



numbers = [5,5,7,7,8,8,10]
target = 6
print(search_range(numbers, target))