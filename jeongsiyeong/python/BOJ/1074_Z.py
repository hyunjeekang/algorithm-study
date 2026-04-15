def divide_conquer(n, r, c):
    if n == 0:
        return 0
    
    half = 2**(n-1)

    if r < half and c<half:
        return divide_conquer(n-1, r, c)
    
    elif r<half and c>=half:
        return half*half + divide_conquer(n-1, r, c- half)
    elif r >= half and c<half:
        return 2*half*half + divide_conquer(n-1, r-half, c)
    else:
        return 3*half*half + divide_conquer(n-1, r-half, c-half)


N, r, c = map(int, input().split())

print(divide_conquer(N,r,c))
