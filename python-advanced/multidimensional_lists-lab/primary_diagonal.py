def get_primary_diagonal(mm):
    the_sum = 0
    for i in range(len(mm)):
        the_sum += matrix[i][i]
    return the_sum


n = int(input())

matrix = []

for _ in range(n):
    row = ([int(x) for x in input().split()])
    matrix.append(row)

print(get_primary_diagonal(matrix))
