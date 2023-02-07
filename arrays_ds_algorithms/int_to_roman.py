import math

def int_to_roman(num):
    roman_dict = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000: "M"}
    types = [1000, 100, 10, 1]
    types_dict = {1000: 0, 100: 0, 10: 0, 1: 0}
    exceptions = {900: "CM", 400: "CD", 90: "XC", 40:"XL", 9: "IX", 4: "IV"}
    str_list = []

    for t in types:
        count = math.floor(num / t)
        types_dict[t] = types_dict[t] + count
        num -= count * t

    for types in types_dict:
        if types_dict[types] > 0:
            current = types_dict[types] * types
            while current != 0:
                half = (types/2) * 10
                if current not in exceptions:
                    if half <= current:
                        try:
                            str_list.append(roman_dict[half])
                            current -= half
                        except KeyError:
                            pass
                    else:
                        str_list.append(roman_dict[types])
                        current -= types
                else:
                    str_list.append(exceptions[current])
                    current -= current

    return ''.join(str_list)


while True:
    digit = int(input("Enter num: "))
    print(int_to_roman(digit))