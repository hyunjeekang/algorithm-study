import math

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())

    dist = y - x
    k = int(math.sqrt(dist))

    if dist - k**2 == 0 :
        print(2*k-1)
    elif dist - k**2 <= k :
        print(2*k)
    elif dist - k**2 <= 2*k :
        print(2*k+1)
    else :
        print(2*k+2)