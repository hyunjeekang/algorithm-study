# import sys
# sys.stdin = open('input.txt')

N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort() ## 오름차순
result = [0]*M
visited = [False]*N #방문배열

def DFS(index):

    if index == M:    # 만약에 뽑고자하는 수를 다 뽑았다면
        print(*result)  # 결과를 출력하고
        return #다시 호출



    for i in range(N):  # arr에서 하나씩 뺄때
        if not visited[i]:  # 방문하지 않은거라면
            result[index] = arr[i] # ex. arr의 i번째 수를 result의 i번째에 놓는다
            visited[i] = True  # 방문했고
            DFS(index+1) # 그 다음에 다음칸 인덱스로 함수를 재호출한다.
            visited[i] = False # 백트래킹

DFS(0)





