grid = [[1,3,1],[1,5,1],[4,2,1]]
m,n = len(grid),len(grid[0])
dircs = [[0,1],[1,0]]  # Only allowed to move right or down

results =[]
def dfs(r,c,visited):
    if (r > m-1) or (c > n-1):
        return
    visited.append(grid[r][c])
    
    if (r == m-1) and (c == n-1):
        results.append([i for i in visited])
        
    for i,j in dircs:
        newr, newc = r+i, c+j
        dfs(newr,newc,visited)
    visited.pop()     
    
dfs(0,0,[])
print(results)

#OR

grid = [[1,3,1],[1,5,1],[4,2,1]]
m,n = len(grid),len(grid[0])

results = []
def dfs(i,j,visited):
    if (i > m-1) or (j > n-1):
        return
    visited.append(grid[i][j])
    
    if (i == m-1) and (j == n-1):
        results.append([i for i in visited])
    
    dfs(i+1,j,visited)
    dfs(i,j+1,visited)
    visited.pop()
    
dfs(0,0,[])
print(results)

#try to implement dynamic programming to keep track of path sum