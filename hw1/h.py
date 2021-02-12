x = int(input())
n = int(input())
for i in range(n):
    in_col = False
    for j in range(n):
        cur = int(input())
        if cur == x:
            in_col = True
    if in_col:
        print("YES")
    else:
        print("NO")
