n = int(input())
lst = list(map(int, input().split()))
x = int(input())

in_lst = False
for i in range(n):
    if lst[i] == x:
        in_lst = True
        break

if in_lst:
    print("YES")
else:
    print("NO")
