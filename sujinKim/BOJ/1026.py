N = int(input())
A = list(map(int,input().split()))  # A에 있는 N개의 수가 순서대로 주어지고, 셋째줄에는 B에 있는 수가 순서대로 주어진다.
B = list(map(int,input().split())) # B에 있는 수가 순서대로 주어진다.
A.sort()
B.sort(reverse=True)

MIN =0
for i in range(N):
    MIN += (A[i] * B[i])

print(MIN)
