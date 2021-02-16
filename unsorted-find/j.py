n = int(input())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
max_value = lst[0]
for elem in lst:
    if elem < max_value:
        print(elem)
        break
# imax1 = 0
# imax2 = 0
# answer = 0
# for i in range(n):
#     if lst[i] > lst[imax1]:
#         temp = imax1
#         imax1 = i
#         if lst[temp] > lst[imax2]:
#             imax2 = temp
#     elif lst[i] > lst[imax2]:
#         imax2 = i
# answer = lst[imax2]
#
# print(answer)
