

import sys
# sys.stdin = open("input.txt")

N = int(sys.stdin.readline())
arr1 = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr2 = list(map(int,sys.stdin.readline().split()))

# arr2를 돌면서 , 이 수들이 arr1안에 존재하는지 알아내기
for i in range(M):  # M개의 수의 리스트를 하나 꺼내
    for j in range(N): # i 1개를 기준으로 arr1 N개가 돌거 아니야 ?
        if arr2[i] == arr1[j]: # 그떄,
            print(1)
            break
    else:
        print(0)


