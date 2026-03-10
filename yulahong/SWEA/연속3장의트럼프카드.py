card = ['A', 'J', 'Q', 'K']
path = []
N = 4

def recur2(cnt):
    if cnt == 5: # 이게 백트래킹의 역할을 함
        print(*path)     
        # for idx in path:
        #     print(lst[idx])
        return
    
    for i in card:

        path.append(i)
        recur2(cnt+1) 
        path.pop()

recur2(0)