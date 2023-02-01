def repeat(string):
    str_list = [*string]
    str_dict = {}

    for i in range(0, len(str_list)):
        if str_list[i] not in str_dict:
            str_dict[str_list[i]] = 1
        else:
            str_dict[str_list[i]] += 1

    for key in str_dict:
        if str_dict[key] == 1:
            return str_list.index(key)


string = "abAA1ac"
print(repeat(string))