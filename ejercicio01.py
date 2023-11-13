#vecinos(x,y) = (x+1,y),(x-1,y),(x,y-1),(x,y+1)
dr = [1,-1,0,0] #desplazamiento en filas
dc = [0,0,-1,1] #desplazamiento en columnas

n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(input())

seen = [[False] * m for _ in range(n)] #lista de visitados

def dfs(r, c): #función de búsqueda en profundidad
    seen[r][c] = True
    #busco en las cuatro direcciones
    for i in range(4):
        r2 = r + dr[i]
        c2 = c + dc[i]
        if 0<=r2<n and 0<=c2<m and grid[r2][c2] == '.' and not seen[r2][c2]:
            dfs(r2, c2)


rooms = 0
for row in range(n):
    for col in range(m):
        #si no lo he visitado, empiezo búsqueda y añado uno al contador.
        if grid[row][col] == '.' and not seen[row][col]:
            rooms += 1
            dfs(row, col)


print(rooms)
