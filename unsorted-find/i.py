n, m = map(int, input().split())
matrix = [[0] * n] * n
for i in range(n):
    matrix[i] = list(map(int, input().split()))

saddle_points = 0
min_indices = []
max_indices = []
jmin = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] < matrix[jmin][j]:
            jmin = i
    min_indices.append(jmin)
imax = 0
for j in range(m):
    for i in range(n):
        if matrix[i][j] > matrix[imax][j]:
            imax = i
    max_indices.append(imax)

for i in range(n):
    for j in range(m):
        if matrix[i][j] == matrix[min_indices[i]][max_indices[j]]:
            saddle_points += 1

print(saddle_points)
