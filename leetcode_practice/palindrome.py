def is_palindrome(num):
    num_string = str(num)
    reverse_char_list = [*num_string[::-1]]
    reverse_num_string = ''.join(reverse_char_list)
    if reverse_num_string == num_string:
        return True
    else:
        return False

while True:
    num = int(input("Enter number: "))
    print(is_palindrome(num))