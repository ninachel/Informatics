n, m = map(int, input().split())
matrix = [[0] * n] * n
for i in range(n):
    matrix[i] = list(map(int, input().split()))

saddle_points = 0
imax = 0
jmin = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] < matrix[i][jmin]:
            jmin = j
    for k in range(m):
        if matrix[k][jmin] > matrix[imax][jmin]:
            imax = k
    for j in range(m):
        if matrix[i][j] == matrix[imax][jmin]:
            saddle_points += 1

print(saddle_points)
