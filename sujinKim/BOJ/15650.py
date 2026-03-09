# 조합 : 순열과 달리 index=0 인 부분에 방문해제를 하면 안될거 같음 


N,M = map(int,input().split())

array = [i for i in range(1,N+1)]

result = [0]*M
# visited = [False]*(N+1)

def DFS(index,start):
    if index == M:
        print(*result)
        return 
    
    for i in range(start,N+1): # array를 한바퀴 돌거야
        # if not visited[i]: # 만약 방문하지 않았다면 
            # visited[i] = True # 방문표시를 하고 
            result[index] = i #결과값의 인덱스에 넣어 
            DFS(index + 1,i+1) # 그 다음에 옆칸의 인덱스에 함수를 불러
            # visited[i] = False # 원복 
       
             
DFS(0,1) 

