K, N = map(int, input().split())

# Please write your code here.
array = [i for i in range(1,K+1)]

result = [0]*N
# visited = [False]*(N+1)
#중복순열 
def DFS(index):
    if index == N:
        print(*result)
        return 
    for i in range(K):
        result[index]=array[i]
        DFS(index+1)
DFS(0)

