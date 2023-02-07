def reverse_int(x):
    mini = pow(-2, 31)
    maxi = pow(2, 31) -1

    num_list = []
    if x > 0:
        str_num = str(x)
    else:
        str_num = str(x * -1)
        num_list.append("-")
        
    for i in reversed(range(len(str_num))):
        num_list.append(str_num[i:i+1])

    fin = int(''.join(num_list))
    
    if fin <= mini or fin >= maxi:
        fin = 0

    return fin

while True:
    num = int(input("enter num: "))
    print(reverse_int(num))