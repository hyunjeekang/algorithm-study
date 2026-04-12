N = int(input())

LIST = []
for i in range(N):
    A, B = map(int,input().split())
    LIST.append((A, B))

LIST.sort()
for j in LIST:
    print(*j)