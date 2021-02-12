x = int(input())
n = int(input())
lst = [[0] * n] * n
for i in range(n):
    lst[i] = list(map(int, input().split()))

for j in range(n):
    in_col = False
    for i in range(n):
        if lst[i][j] == x:
            in_col = True
    if in_col:
        print("YES")
    else:
        print("NO")
