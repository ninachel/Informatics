def contains(lst, key):
    left = -1
    right = len(lst)
    while left < right - 1:
        mid = (left + right) // 2
        if lst[mid] > key:
            right = mid
        else:
            left = mid

    if left >= 0 and lst[left] == key:
        return "YES"

    return "NO"


n, k = map(int, input().split())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
for i in range(k):
    print(contains(lst1, lst2[i]))
