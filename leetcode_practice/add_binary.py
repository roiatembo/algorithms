import math
def add_binary(a,b):
    def integer(bin):
        interger = 0
        current_digit = 1
        for c in range(len(bin), 0, -1):
            if bin[c-1] != "0":
                interger += current_digit
            
            current_digit += current_digit
        return interger
    
    def convert_bin(sum):
        binary_list = []
        start_exp = math.floor(math.log(sum)/math.log(2))
        rem = sum - pow(2, start_exp)
        binary_list.append("1")
        for exp in range(start_exp-1, -1, -1):
            if rem >= pow(2, exp):
                binary_list.append("1")
                rem = rem - pow(2, exp)
            else:
                binary_list.append("0")
        return ''.join(binary_list)

    sum = integer(a) + integer(b)
    return convert_bin(sum)


while True:
    a = input("Enter first num: ")
    b = input("Enter second num: ")
    print(add_binary(a,b))