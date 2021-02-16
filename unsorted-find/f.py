n = int(input())
lst = list(map(int, input().split()))

imax = 0
for i in range(n):
    if lst[i] > lst[imax]:
        imax = i

print(imax + 1)
