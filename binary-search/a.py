def closest_num(lst, key):
    left = 0
    right = len(lst)
    lower_bound_index = -1
    while left < right:
        mid = (left + right) // 2
        if lst[mid] < key:
            lower_bound_index = mid
            left = mid + 1
        else:
            right = mid

    if lower_bound_index == -1:
        return lst[-1]

    if abs(key - lst[lower_bound_index]) > abs(key - lst[lower_bound_index - 1]):
        return lst[lower_bound_index - 1]

    return lst[lower_bound_index]


n, k = map(int, input().split())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
for i in range(k):
    print(closest_num(lst1, lst2[i]))
