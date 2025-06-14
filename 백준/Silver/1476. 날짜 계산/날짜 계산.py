input_e, input_s, input_m = map(int, input().split())

e, s, m = 1, 1, 1
year = 1

while True:
    if e == input_e and s == input_s and m == input_m:
        print(year)
        break

    if e < 15:
        e += 1
    else:
        e = 1

    if s < 28:
        s += 1
    else:
        s = 1

    if m < 19:
        m += 1
    else:
        m = 1

    year += 1
