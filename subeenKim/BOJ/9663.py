N = int(input())

columns = []

# 대각선 확인 abs(x좌표 차이) = abs(y좌표 차이)
# 선택 안 한 열 중에 선택
visited = [False]*N

def backtrack(n):
    global cnt
    if n == N:
        cnt += 1
        return
    
    for i in range(N):
        is_dia = False
        if not visited[i]:
            for j in range(n):
                if abs(n - j) == abs(i - columns[j]):
                    is_dia = True
                    break
            if not is_dia :
                visited[i] = True
                columns.append(i)
                backtrack(n+1)
                columns.pop()
                visited[i] = False

cnt = 0
backtrack(0)
print(cnt)