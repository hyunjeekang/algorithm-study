arr = [list(map(int,input().split())) for _ in range(3)]
rows = 3
cols = 3

new_arr = []
for i in range(rows):
    new_row =[]
    for j in range(cols):
        #각 요소에 3을 곱하여 새로운 행에 추가 
        new_row.append(arr[i][j]*3)
    new_arr.append(new_row)

for row in new_arr:
    print(*row)