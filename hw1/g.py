n = int(input())
lst = list(map(int, input().split()))

imin_first = 0
for i in range(n):
    if lst[i] < lst[imin_first]:
        imin_first = i

imin_second = 0
for i in range(n):
    if lst[i] < lst[imin_second] and i != imin_first:
        imin_second = i

print(lst[imin_first], lst[imin_second])
