from collections import deque
test_case = int(input())

dx = [1, 2, 2,1,-1,-2,-2,-1]
dy = [2, 1,-1,-2,-2,-1, 1, 2]

def is_range(x,y,l):
    return 0 <=x<l and 0 <=y<l

for _ in range(test_case):
    l = int(input())
    o_x, o_y = map(int, input().split())
    t_x, t_y = map(int, input().split())

    visited = [[ 0 for _ in range(l)] for _ in range(l)]

    q = deque()
    q.append((o_x, o_y))
    visited[o_x][o_y] = 1

    while q:
        cur_x, cur_y = q.popleft()
        if cur_x == t_x and cur_y == t_y:
            print(visited[cur_x][cur_y]-1)
            break

        for i in range(8):
            if is_range(cur_x + dx[i], cur_y + dy[i], l) and not visited[cur_x + dx[i]][cur_y+dy[i]]:
                visited[cur_x + dx[i]][cur_y+dy[i]] = visited[cur_x][cur_y] + 1
                q.append((cur_x + dx[i], cur_y + dy[i]))
    
