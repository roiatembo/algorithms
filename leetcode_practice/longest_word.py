def longest(s):
    s_list = s.split(" ")
    for index in range(len(s_list)-1, -1, -1):
        if len(s_list[index]) > 0:
            length = len(s_list[index])
            break

    return length

while True:
    s = input("enter string: ")
    print(longest(s))