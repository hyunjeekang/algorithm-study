N = int(input())

arr = [[0]*100 for _ in range(100)]

for _ in range(N):
    c, r = map(int, input().split())

    for i in range(r, r + 10):
        for j in range(c, c+10):
            arr[i][j] = 1

#세로로 높이 누적하기 누적하기
for r in range(1, 100):
    for c  in range(100):
        if arr[r][c] == 1:
            arr[r][c] += arr[r-1][c]

mx_area = 0

for r in range(100):
    for c in range(100):
        height = arr[r][c]

        #높이 0이면?
        if height == 0:
            continue
        # 중간에 0을 만나면?
        for k in range(c, 100):
            if arr[r][k] == 0:
                break
        
            height = min(height, arr[r][k])

            width = k - c + 1

            mx_area = max(mx_area, width * height)

print(mx_area)