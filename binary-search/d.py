import bisect


def first_last(lst, key):
    first = bisect.bisect_left(lst, key)
    if first != len(lst):
        last = bisect.bisect_right(lst, key)
        return str(first + 1) + ' ' + str(last)

    return 0


n, m = map(int, input().split())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
for i in range(m):
    print(first_last(lst1, lst2[i]))
