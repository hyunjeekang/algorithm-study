N, K = map(int, input().split())
K = list(map(int, input().split()))

for i in K:
    ans = i*100 // N

    print(ans)
