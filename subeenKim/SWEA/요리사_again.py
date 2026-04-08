import sys; sys.stdin = open('sample_input.txt')

T = int(input())

def backtrack(start, cnt):
    global ans
    if cnt == N//2:
        unselected = list(all_food - set(selected))

        s1, s2 = 0, 0
        for n in range(N//2):
            for m in range(N//2):
                if n != m:
                    s1 += score[selected[n]][selected[m]]
                    s2 += score[unselected[n]][unselected[m]]
        ans = abs(s1 - s2) if abs(s1-s2) < ans else ans
        return
    
    for i in range(start, N):
        selected.append(i)
        backtrack(i+1, cnt+1)
        selected.pop()


for tc in range(1, T+1):
    N  = int(input())
    score = [list(map(int, input().split())) for _ in range(N)]
    total = []
    ans = float('inf')
    all_food = {i for i in range(1, N+1)}
    selected = [0]
    backtrack(1, 1)



    print(f'#{tc} {ans}')