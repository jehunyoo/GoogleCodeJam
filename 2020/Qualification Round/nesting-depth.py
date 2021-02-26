T = int(input())

for t in range(1, T+1):
    S = input() + '0'
    nested_S = ""
    prev = 0

    for s in S:
        digit = int(s)
        if prev == digit:
            pass
        elif prev < digit:
            nested_S += "(" * (digit - prev)
        elif prev > digit:
            nested_S += ")" * (prev - digit)
        nested_S += s
        prev = digit

    print(f"Case #{t}: {nested_S[:-1]}")