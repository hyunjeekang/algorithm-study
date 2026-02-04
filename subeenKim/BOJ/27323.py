N = int(input())
before = list(map(int, input().split()))
after = list(map(int, input().split()))

cnt = 0
for i in range(N) :
    if before[i] < after[i] :
        cnt += (after[i] - before[i])

print(cnt)