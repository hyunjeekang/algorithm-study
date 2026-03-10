# 중복순열


path = []

def recur(cnt):
    if cnt == 2:
        print(path)
        return
    
    # 0을 선택
    path.append(0)
    recur(cnt+1)
    path.pop() 

    path.append(1)
    recur(cnt+1)
    path.pop()

    path.append(2)
    recur(cnt+1)
    path.pop()

recur(0)

#순열
path = []
N = 3
used = [0]*3

def recur2(cnt):
    if cnt == 2: # 이게 백트래킹의 역할을 함
        print(*path)     
        # for idx in path:
        #     print(lst[idx])
        return
    
    for i in range(3):
        if used[i]: # 사용한 적 있다면 넘어가라 = 안되면 패스해라
            continue

        used[i] = 1 # 방문처리
        path.append(i)
        recur2(cnt+1) 
        path.pop()
        used[i] = 0

recur2(0)
    

[4,3,35,65,6,34,3,42,32]