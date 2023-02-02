def int_to_roman(num):
    roman_dict = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000: "M"}
    str_list = []

    while num !=0:
        if num >= 1000:
            str_list.append(roman_dict[1000])
            num -= 1000
        elif num >= 500:
            str_list.append(roman_dict[500])
            num -= 500
        elif num   >= 100:
            str_list.append(roman_dict[100])
            num -= 100
        elif num >= 50:
            str_list.append(roman_dict[50])
            num -= 50
        elif num >= 10:
            str_list.append(roman_dict[10])
            num -= 10
        elif num >= 5:
            str_list.append(roman_dict[5])
            num -= 5
        elif num >= 1:
            str_list.append(roman_dict[1])
            num -= 1

    
    return ''.join(str_list)

while True:
    digit = int(input("Enter num: "))
    print(int_to_roman(digit))