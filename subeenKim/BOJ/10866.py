# import deque 하지 않고 문제 풀어보기!

N = int(input())
commands = [input().split() for _ in range(N)]
q = []
for c in commands:
    if c[0] == 'push_back':
        q.append(c[1])
    elif c[0] == 'push_front':
        q = [c[1]] + q
    elif c[0] == 'pop_front':
        print(q.pop(0) if q else -1)
    elif c[0] == 'pop_back':
        print(q.pop() if q else -1)
    elif c[0] == 'size':
        print(len(q))
    elif c[0] == 'empty':
        print(0 if q else 1)
    elif c[0] == 'front':
        print(q[0] if q else -1)
    elif c[0] == 'back':
        print(q[-1] if q else -1)