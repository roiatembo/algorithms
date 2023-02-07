def divide(dividend, divisor):
    mini = pow(-2, 31)
    maxi = pow(2, 31) -1

    if dividend < 0 and divisor < 0:
        neg = ""
    elif dividend < 0 or divisor < 0:
        neg = "-"
    else:
        neg = ""

    if dividend < 0:
        dividend = int(str(dividend)[1:])

    if divisor < 0:
        divisor = int(str(divisor)[1:])

    quotient = 0
    current = 0

    for i in range(0, dividend, divisor):
        # print(f"Div")
        quotient += 1
        current += divisor
        
        
    if current > dividend:
        quotient -= 1

    return int(neg + str(quotient))

    # -2147483648

while True:
    dividend = int(input("Enter Dividend: "))
    divisor = int(input("Enter divisor: "))
    print(divide(dividend, divisor))