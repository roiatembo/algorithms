# method 1
def find_fib(term):
    fib_seq = [0,1]
    if term < 2:
        return term
    else:
        for index in range(2, term+1):
            fib_seq.append((fib_seq[index - 1]) + (fib_seq[index - 2]))
    
    return fib_seq[term]


def fib_recursive(n, ht={0: 0, 1: 1}):
    if n in ht:
        return ht[n]
    else:
        ht[n] = fib_recursive(n -1, ht) + fib_recursive(n - 2, ht)
        return ht[n]