# my solution

def reverse_array(array):
    arr_length = len(array)
    new_array = []
    for index in range(1, arr_length + 1):
        new_array.append(array[arr_length - index])
    
    return new_array

arr = [1,2,3,4,5]
# print(reverse_array(arr))

# the solutions
def reverse(nums):
    start_index = 0
    end_index = len(nums) - 1

    while end_index > start_index:
        nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
        start_index += 1
        end_index -= 1


reverse(arr)
print(arr)