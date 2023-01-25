# my solution

arr = [-3,1,2,3,4,5]
second_arr = []

def square_array(arr):
    start_index = 0

    while len(arr) > start_index:
        arr[start_index] = arr[start_index] ** 2
        start_index += 1

    arr.sort()

square_array(second_arr)
print(second_arr)