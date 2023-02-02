def longest_sub(string):
    str_list = [*string]
    hash_t = {}
    lens = {}

    for char in range(0, len(str_list)):
        if str_list[char] not in hash_t:
            hash_t[str_list[char]] = [char]
        else:
            hash_t[str_list[char]].append(char)

    print(hash_t)
        
    for key in hash_t:
        if len(hash_t[key]) == 1:
            subs_len = len(str_list) - hash_t[key][0]
        elif len(hash_t[key]) == 2:
            subs_len = hash_t[key][1] - hash_t[key][0]

        lens[key] = subs_len
    
    print(lens)
    
    the_big = max(lens, key=lens.get)

    if len(hash_t[the_big]) < 2:
        long_sub = string[hash_t[the_big][0]:]
    else:
        long_sub = string[hash_t[the_big][0]:hash_t[the_big][1]]
    
    return long_sub

while True:
    string = input("enter: ")
    print(longest_sub(string))