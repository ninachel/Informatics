n = int(input())
lst = list(map(int, input().split()))
x = int(input())

for i in range(n):
    if lst[i] == x:
        print(i + 1)
