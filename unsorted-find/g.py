n = int(input())
lst = list(map(int, input().split()))

imin1 = 0
imin2 = 0
for i in range(n):
    if lst[i] < lst[imin1]:
        temp = imin1
        imin1 = i
        if lst[temp] < lst[imin2]:
            imin2 = temp
    elif lst[i] < lst[imin2]:
        imin2 = i

print(lst[imin1], lst[imin2])
