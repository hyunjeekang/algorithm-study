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