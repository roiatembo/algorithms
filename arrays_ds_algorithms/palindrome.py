def palindrome(string):
    str_list = [*string]
    j = len(str_list)
    new_str = ""
    for i in range(0, j):
        new_str += str_list[j-1]
        j -= 1
    
    if string == new_str:
        return "Its a palindrome"
    else:
        return "not a palindrome"


while True:
    string = input("enter string: ") 
    print(palindrome(string))

# this method unfortunately uses time complexity of o(n^2)