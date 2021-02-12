n = int(input())
lst = list(map(int, input().split()))
x = int(input())

x_cnt = 0
for i in range(n):
    if lst[i] == x:
        x_cnt += 1

print(x_cnt)
