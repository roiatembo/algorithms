def sum_peculiar(arr, count = 1):
    total = 0
    for item in arr:
        if type(item) == "list":
            count += 1
            sum_peculiar(item, count)
        else:
            total += item

    return total

arr = [1,1,[2,2]]
print(sum_peculiar(arr))