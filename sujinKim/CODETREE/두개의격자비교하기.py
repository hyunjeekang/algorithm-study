N,M = tuple(map(int,input().split())) #격자의 행의 개수, 열의 개수 
#N개의 줄에 걸쳐 첫 번쨰 N*M크기의 격자가 주어짐
arr1 = [list(map(int,input().split())) for _ in range(N)]
#N+2번쨰 줄부터 n개의 줄에 걸쳐 두 번째 N*M크기의 격자가 주어짐 
arr2 = [list(map(int,input().split())) for _ in range(N)]

new_arr = [
    [0 for _ in range(M)]   ###### 행열 크기를 조심하자잉
    for _ in range(N)
]
for i in range(N):
    for j in range(M):
        if arr1[i][j] == arr2[i][j]:
            new_arr[i][j]=0
        else:
            new_arr[i][j]=1
for row in new_arr:
    print(*row)

# new_arr = [
#     [1 if arr1[i][j] != arr2[i][j] else 0 for j in range(M)]
#     for i in range(N)
# ]

# #새로운 배열을 출력합니다. 
# for row in new_arr:
#     for elem in row:
#         print(elem, end=" ")
#     print()

