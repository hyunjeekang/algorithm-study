import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0

# 1부터 2^N - 1까지 (모든 부분수열 경우의 수, 공집합 제외)
for i in range(1, 1 << N):
    subset_sum = 0
    
    for j in range(N):
        # i라는 비트마스크에 j번째 비트가 켜져 있는지 확인
        if i & (1 << j):
            subset_sum += arr[j]
    
    if subset_sum == S:
        cnt += 1

print(cnt)