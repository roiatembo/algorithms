def group_anagram(strs):
    strings_dict = {}
    final_list =[]
    if len(strs) > 0:
        for word in strs:
            alphabet = ''.join(sorted(word))

            if alphabet not in strings_dict:
                strings_dict[alphabet] = [word]
            else:
                strings_dict[alphabet].append(word)
        for keys in strings_dict:
            final_list.append(strings_dict[keys])

        return final_list
    else:
        return [""]


print(group_anagram(strs = ["a"]))