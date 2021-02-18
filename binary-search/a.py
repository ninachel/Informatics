from bisect import bisect_left


def closest_num(lst, key):
    lower_bound_index = bisect_left(lst, key)

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
