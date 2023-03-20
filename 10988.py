N = list(input())
s = len(N)
s_h = s // 2
lst_a = N[:s_h]
lst_b = N[-s_h:]
if s == 1:
    print(1)
else:
    if s % 2 == 1:
        if lst_a == lst_b[::-1]:
            print(1)
        else:
            print(0)
    else:
        if lst_b[::-1] == lst_a:
            print(1)
        else:
            print(0)