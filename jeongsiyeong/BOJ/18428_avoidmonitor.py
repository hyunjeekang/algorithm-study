N = int(input())

arr = [list(input().split()) for _ in range(N)]

def is_range(r,c):
    return 0<=r<N and 0<=c<N

def is_safe():
    for c in checked:
        if not c:
            return False
    return True

def dfs(index, depth):
    if depth == 3:
        return
    
    if is_safe():
        print("YES")
        exit()
    
    for i in range(index, M):
        cur_r, cur_c, dir = candidates[i]
        for j in range(1, N-1):
            nr = cur_r + j*dr[dir]
            nc = cur_c + j*dc[dir]
            if is_range(nr, nc):
                for k in range(M):
                    if nr==students[k][0] and nc == students[k][1]:
                        if not checked[k]:
                            checked[k] = True
                            dfs(index+1, depth+1)
                            checked[k] = False

dr = [0, 1, 0, -1]
dc = [1, 0 , -1, 0]
students = []
candidates = []
for r in range(N):
    for c in range(N):
        if arr[r][c] == 'T':
            tmp = set()
            
            for i in range(4):
                for j in range(1, N-1):
                    nr = r + j*dr[i]
                    nc = c + j*dc[i]
                    
                    if not is_range(nr, nc):
                        break
                    else:
                        if arr[nr][nc] == 'S':
                            for t in tmp:
                                candidates.append(t)
                            break
                        elif arr[nr][nr] == 'T':
                            break
                        else:
                            tmp.add((nr, nc, i))
        elif arr[r][c] == 'S':
            students.append((r,c))
M = len(students)
checked = [False] * M

dfs(0, 0)
print("NO")