dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]
movimientos = ['D', 'U', 'L', 'R']

# Busqueda en anchura (BFS)
visited = [] # nodos visitaods
queue = [] # cola

def bfs(grid, start, end):
    visited.append(start)
    queue.append((start, ""))
    idx = 0 # indice del elemento.
    while queue:
        (x, y), ruta = queue[idx]
        if (x, y) == end:
            return "SÍ\n" + str(len(ruta)) + "\n" + ruta

        for i, j, letra in zip(dr, dc, movimientos):
            r2, c2 = x + i, y + j
            if 0 <= r2 < n and 0 <= c2 < m and grid[r2][c2] != '#' and (r2, c2) not in visited:
                queue.append(((r2, c2), ruta + letra))
                visited.append((r2, c2))
        idx += 1
    return "NO"



n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]


inicio, final = None, None

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'A':
            a = (i, j)
        elif grid[i][j] == 'B':
            b = (i, j)

print(bfs(grid, a, b))
