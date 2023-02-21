def plus_one(digits):
    joined_list = []
    final_list = []
    for num in digits:
        joined_list.append(str(num))
    
    increased_digit = int(''.join(joined_list)) + 1
    for char in str(increased_digit):
        final_list.append(int(char))
    
    return final_list

digits = [9]
print(plus_one(digits))