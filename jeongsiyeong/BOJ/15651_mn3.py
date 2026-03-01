N, M = map(int, input().split())

def perm2(depth):
    if depth == M:
        print(*result)
        return
    for i in range(1,N+1):
        result[depth] = i
        perm2(depth+1)

result = [ 0 for _ in range(M)]
perm2(0)