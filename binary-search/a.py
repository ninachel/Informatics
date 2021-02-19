def lower_bound(lst, key):
    left = 0
    right = len(lst)
    while left < right:
        mid = (left + right) // 2
        if lst[mid] < key:
            left = mid + 1
        else:
            right = mid

    return left


def upper_bound(lst, key):
    left = 0
    right = len(lst)
    while left < right:
        mid = (left + right) // 2
        if lst[mid] > key:
            right = mid
        else:
            left = mid + 1

    return left


def closest_num(lst, key):
    lower_bound_index = lower_bound(lst, key)

    if lower_bound_index == len(lst):
        return lst[-1]

    if abs(key - lst[lower_bound_index]) >= abs(key - lst[lower_bound_index - 1]):
        return lst[lower_bound_index - 1]

    return lst[lower_bound_index]


n, k = map(int, input().split())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
for i in range(k):
    print(closest_num(lst1, lst2[i]))
