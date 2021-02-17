def closest_num(lst, key):
    pass


n, k = map(int, input().split())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
for i in range(k):
    print(closest_num(lst1, lst2[i]))
