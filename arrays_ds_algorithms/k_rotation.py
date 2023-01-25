# my solution

def rotate(arr, k):
    end_index = len(arr) - 1
    k_times = len(arr)%k
    while k_times < k:
        arr.insert(0, arr[end_index])
        arr.pop()
        k_times += 1

arr = [1,2,3,4,5]
rotate(arr, 7)
print(arr)

# interview solution
def reverse(array,start,end):
    while(start<end):
        array[start],array[end] = array[end], array[start]
        start +=1
        end -=1
    return array

def rotate_array(array,k):
    k= k % len(array)
    reverse(array, 0, len(array)-1)
    reverse(array, 0, k-1)
    reverse(array, k, len(array)-1)
    return array

print(rotate_array([1,2,3,4,5],3))
