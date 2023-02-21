import math

def convert_bin(sum):
    binary_list = []
    start_exp = math.floor(math.log(sum)/math.log(2))
    print(start_exp)
    rem = sum - pow(2, start_exp)
    binary_list.append("1")
    for exp in range(start_exp-1, -1, -1):
        if rem >= pow(2, exp):
            binary_list.append("1")
            rem = rem - pow(2, exp)
        else:
            binary_list.append("0")

    return binary_list

print(convert_bin(987))