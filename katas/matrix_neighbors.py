"""Find neighbors of number given in a matrix."""


def neighbors(matrix, x, y):
    """Get all neighboring numbers from given x y int in matrix."""
    m = len(matrix[0]) - 1
    n = len(matrix) - 1
    neighbor = []
    if x == 0 and y == 0:
        neighbor.append(matrix[x][y + 1])
        neighbor.append(matrix[x + 1][y])
        neighbor.append(matrix[x + 1][y + 1])
        return neighbor
    elif x == n and y == m:
        neighbor.append(matrix[x][y - 1])
        neighbor.append(matrix[x - 1][y])
        neighbor.append(matrix[x - 1][y - 1])
        return neighbor
    elif x == 0 and y == m:
        neighbor.append(matrix[x][y - 1])
        neighbor.append(matrix[x + 1][y])
        neighbor.append(matrix[x + 1][y - 1])
        return neighbor
    elif x == n and y == 0:
        neighbor.append(matrix[x][y + 1])
        neighbor.append(matrix[x - 1][y])
        neighbor.append(matrix[x - 1][y + 1])
        return neighbor
    elif x == 0 and y < m and y > 0:
        neighbor.append(matrix[x][y + 1])
        neighbor.append(matrix[x][y - 1])
        neighbor.append(matrix[x + 1][y])
        neighbor.append(matrix[x + 1][y + 1])
        neighbor.append(matrix[x + 1][y - 1])
        return neighbor
    elif x == n and y < m and y > 0:
        neighbor.append(matrix[x][y + 1])
        neighbor.append(matrix[x][y - 1])
        neighbor.append(matrix[x - 1][y])
        neighbor.append(matrix[x - 1][y + 1])
        neighbor.append(matrix[x - 1][y - 1])
        return neighbor
    elif x > 0 and x < n:
        if y == 0:
            neighbor.append(matrix[x][y + 1])
            neighbor.append(matrix[x + 1][y + 1])
            neighbor.append(matrix[x - 1][y + 1])
            neighbor.append(matrix[x + 1][y])
            neighbor.append(matrix[x - 1][y])
            return neighbor
        elif y == m:
            neighbor.append(matrix[x][y - 1])
            neighbor.append(matrix[x + 1][y - 1])
            neighbor.append(matrix[x - 1][y - 1])
            neighbor.append(matrix[x + 1][y])
            neighbor.append(matrix[x - 1][y])
            return neighbor
        elif y > 0 and y < m:
            neighbor.append(matrix[x][y + 1])
            neighbor.append(matrix[x][y - 1])
            neighbor.append(matrix[x + 1][y])
            neighbor.append(matrix[x - 1][y])
            neighbor.append(matrix[x + 1][y - 1])
            neighbor.append(matrix[x - 1][y - 1])
            neighbor.append(matrix[x + 1][y + 1])
            neighbor.append(matrix[x + 1][y + 1])
            return neighbor
