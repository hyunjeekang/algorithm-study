def backtrack(temp_list):
    if len(temp_list) == 8:
        full_order = temp_list[:3] + [0] + temp_list[3:]
        order.append(full_order)
        return
    
    for i in range(8):
        if not visited[i]:
            temp_list.append(numlist[i])
            visited[i] = True
            backtrack(temp_list)
            temp_list.pop()
            visited[i] = False
    
N = int(input())
result = [[] for _ in range(9)]
order = []
numlist = [1, 2, 3, 4, 5, 6, 7, 8]
visited = [False]*9
for n in range(N):
    data = list(map(int, input().split()))
    for d in range(len(data)):
        result[d].append(data[d])

backtrack([])

max_score = 0
for odr in order:
    score = 0
    idx = 0
    for n in range(N): # n : 이닝
        b1, b2, b3 = 0, 0, 0 # 1루 / 2루 / 3루
        out = 0
        while out < 3:
            s = result[odr[idx]][n] # 타자가 얻은 결과
            if s == 0: # out
                out += 1
            elif s == 1: # 1루타
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif s == 2: # 2루타
                score += (b2 + b3)
                b1, b2, b3 = 0, 1, b1
            elif s == 3: # 3루타
                score += (b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 1
            else :
                score += (b1 + b2 + b3 + 1)
                b1, b2, b3 = 0, 0, 0
            idx = (idx+1) % 9
    max_score = score if score > max_score else max_score
print(max_score)