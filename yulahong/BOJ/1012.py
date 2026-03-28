# 단지 문제랑 비슷
# dfs
# VISITED배열 사용
# 좌표 돌면서 ARR 완성

T = int(input())
M, N, K = map(int, input().split())
arr = [[0]*M for _ in range(N)]

for _ in range(K):
    a, b = map(int, input().split())

    arr[a][b] = 1

print(arr)

