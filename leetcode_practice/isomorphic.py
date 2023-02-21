def is_isomorphic(s,t):
    hash_t = {}
    test_list = []
    mapped = []
    for c in range(0, len(s)):
        if s[c] not in hash_t and t[c] not in mapped:
            hash_t[s[c]] = t[c]
            mapped.append(t[c])
    try:
        for char in s:
            test_list.append(hash_t[char])
    except KeyError:
        return False

    if t == ''.join(test_list):
        return True
    else:
        return False


while True:
    s = input("Enter s: ")
    t = input("Enter t: ")
    print(is_isomorphic(s,t))