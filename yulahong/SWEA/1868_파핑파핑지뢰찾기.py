# R*C 크기 표
# 지뢰칸 선택하면 소리
# 지뢰 없는 칸이면 맞 닿아 있는 칸에 최대 몇개의 지뢰가 있는지 숫자로 표시
# 숫자 0일 때: 8칸에도 숫자 표시 -> BFS인데 숫자 표시하면서 가기

# 주어진 수
# 첫줄:  테케 수
# 두번째 줄 : N(표 크기)
# N개의 줄 동안 문자열
# * = 지뢰
# . = 지뢰 없음

# 필요한 거
# 8방향 탐색

from collections import deque
dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N) ]
    visited = [[0] for _ in range(N)]
    ans = 0 #초기값
    # 모든 칸을 돌면서 주변 지뢰 개수 파악 
    for r in range(N):
        for c in range(N):
            if arr[r][c] == '*':
                visited[r][c] = -1 # 지뢰는 -1로 표시
                continue
            else:

    # bfs 처리 로직
    # 연쇄 반응?
    




    print(f'#{tc} {ans}')