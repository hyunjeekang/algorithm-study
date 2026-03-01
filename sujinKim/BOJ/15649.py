# N, M = map(int,input().split())

# arr = [] 
# for i in range(1,N+1):
#     arr.append(i)
#     break  # 이렇게 하면 arr라는 빈 리스트에 1부터 N까지 하나씩 넣는다. 
# #이제 여기서 M개 만큼 뽑아서 순열을 만들어야함. 
# #출력하고자 하는 것이 뽑아서 만든 순열들 

# def imme(step):
#     for j in range()


import sys
sys.stdin = open('input.txt')

N,M=map(int,input().split())
#
# array = []
# for j in range(1,N+1):
#     array.append(j)
array = [i for i in range(1,N+1)]

# N =4
# M =2

# array = [i for i in range(1, N+1)]
result = [0]*M
visited = [False]*(N+1)

# print(result)

def DFS(index):
    if index == M:
        print(*result)
        return
    for i in range(N):

        if not visited[i]:
            visited[i] = True
            result[index] = array[i]
            DFS(index + 1)
            visited[i] = False # 원복 (Backtracking)
        else:
            continue

DFS(0)