def is_number(s):
        if "inf" in s.lower():
            return False
        else:
            try:
                int(s)
                return True
            except ValueError:
                try:
                    float(s)
                    return True
                except ValueError:
                    return False
            else:
                return False

while True:
    s = input("insert string: ")
    print(is_number(s))
