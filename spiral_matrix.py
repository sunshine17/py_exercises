def spiral_order(matrix):
    if len(matrix) == 1:
        return matrix[0]
    n = len(matrix[0])
    if n == 1:
        return [x[0] for x in matrix]
    ret = []
    while matrix:
        ret.extend(matrix.pop(0))
        if matrix:
            matrix = rotate_90_degree(matrix)
    return ret

def rotate_90_degree(matrix):
    m, n, = len(matrix), len(matrix[0])
    t = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            t[i][j] = matrix[j][i]
    t.reverse()
    return t

