from collections import deque





N = int(input())
q = deque()

for i in range(N):
    A = input().split()
    q.append(A)


result = []
for j in q:
    if j[0] == "push":
        result.append(j[1])
    elif j[0] == "pop":
        if len(result) != 0:
            print(result.pop(0))
        else:
            print(-1)
    elif j[0] == "size":
        print(len(result))
    elif j[0] == "empty":
        if len(result) == 0:
            print(1)
        else:
            print(0)
    elif j[0] == "front":
        if len(result) != 0 :

            print(result[0])
        else:
            print(-1)
    elif j[0] == "back":
        if len(result) != 0:
            print(result[-1])
        else:
            print(-1)





