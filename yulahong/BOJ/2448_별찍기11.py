# 예제 보고 유추한 뒤 별을 찍기
# k = 3 세로줄 수?
# 3층짜리 별탑 만들어서 복사?
# 1층에 별 하나/ 2층에 별 두 개/ 3층에 별 5개

def star(y, x, size):
    if size == 3:

        star_arr[y][x] = '*'
        star_arr[y+1][x-1] = '*'
        star_arr[y+1][x+1] = '*'

        for i in range(5):
            star_arr[y+2][i] = '*'

        for row in star_arr:
            print("".join(row))


N = 3
star_arr = [[' ' for _ in range(5)] for _ in range(3)] # 5칸짜리 3층
star(0, N-1, N)
# star_arr[0][2] = '*'
# star_arr[1][1] = '*'
# star_arr[1][3] = '*'

# for i in range(5):
#     star_arr[2][i] = '*'

# for row in star_arr:
#     print("".join(row))


N = int(input())

arr = [[" "] *(2*N-1) for _ in range(N)]
def inner_star(r, c, n):
    if n == 3:
        arr[r][c] = "*"
        arr[r+1][c-1], arr[r+1][c+1] = "*", "*"
        for i in range(c-2, c+3):
            arr[r+2][i] = "*"
        return
    else:
        inner_star(r,c,n//2)
        inner_star(r+n//2, c - n//2, n//2)
        inner_star(r+n//2, c+n//2, n//2)
inner_star(0, N-1, N)

for line in arr:
    print("".join(line))        
