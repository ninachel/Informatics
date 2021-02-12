n = int(input())
lst = list(map(int, input().split()))
x = int(input())

min_diff = 1e4
answer = -1
for i in range(n):
    if abs(x - lst[i]) < min_diff:
        min_diff = abs(x - lst[i])
        answer = lst[i]
print(answer)
