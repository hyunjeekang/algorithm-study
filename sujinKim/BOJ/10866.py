from collections import deque


N = int(input())


q= []
for i in range(N):
    a = input().split()
    q.append(a)


result = deque()
for j in q:
    if j[0] == "push_front":
      
        result.appendleft(j[1])
    elif j[0] == "push_back":
        result.append(j[1])

    elif j[0] == "pop_front":
        if len(result) != 0:
            print(result.popleft())
        else:
            print(-1)

    elif j[0] == "pop_back":
        if len(result) != 0:
            print(result.pop())
        else:
            print(-1)

    elif j[0] == "size":
        print(len(result))
    elif j[0] == "empty":
        if len(result) != 0:
            print(0)
        else:
            print(1)
    elif j[0] == "front":
        if len(result) != 0:
            print(result[0])
        else:
            print(-1)
    elif j[0] == "back":
        if len(result) != 0:
            print(result[-1])
        else:
            print(-1)


