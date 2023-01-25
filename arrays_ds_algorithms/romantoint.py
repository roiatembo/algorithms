def romantoint(str):
    roman_dict = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
    str_list = list(str)
    integer = 0
    prevchar = 2000
    for char in str_list:
        if roman_dict[char] > prevchar:
            integer = (integer - prevchar) + (roman_dict[char] - prevchar)
        else:
            integer += roman_dict[char]
            
        
        prevchar = roman_dict[char]

    return integer

while True:
    rom = input("Insert roman numerals: ").upper()
    print(romantoint(rom))