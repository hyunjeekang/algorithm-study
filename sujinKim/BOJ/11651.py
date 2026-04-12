N = int(input())

# 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬
LIST = []
for i in range(N):
    A,B = map(int,input().split())
    LIST.append((A,B))


LIST2 = sorted(LIST,key = lambda x : (x[1],x[0]))

for j in LIST2:
    print(*j)