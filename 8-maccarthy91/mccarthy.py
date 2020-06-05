def mccarthy91(n):
    k = 1
    while k:
        if n > 100:
            n -= 10
            k -= 1
        else:
            n += 11
            k += 1
    return n

def mccarthy91_rec(n):
    if n > 100:
        return n - 10
    else:
        return mccarthy91_rec(mccarthy91_rec(n + 11))

for i in range(1, 1000):
    print(i, mccarthy91(i))
