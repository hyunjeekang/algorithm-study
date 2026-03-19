n, m = map(int, input().split())

seq = []
visited = [False] * (n + 1) 

def permute():
    if len(seq) == m:
        print(*seq)
        return
    
    for i in range(1, n + 1):
        if not visited[i]: 
            visited[i] = True
            seq.append(i)
        
            permute()
            seq.pop()
            visited[i] = False

permute()