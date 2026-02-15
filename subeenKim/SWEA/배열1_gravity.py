T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    boxes = list(map(int, input().split()))
    garo = [0]*max(boxes)
    max_height = 0
 
    for h in range(N-1, -1, -1) :
        for i in range(boxes[h]) :
            max_height = (N - 1 - h - garo[i]) if max_height < (N - 1 - h - garo[i]) else max_height
            garo[i] += 1
 
    print(f'#{test_case} {max_height}')