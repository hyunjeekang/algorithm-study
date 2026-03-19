import sys

input = sys.stdin.readline
N = int(input())

queue = [0] * 10005 
front = 0
rear = 0

for _ in range(N):
    cmd = input().split()
    
    if cmd[0] == 'push':
        queue[rear] = cmd[1]
        rear += 1
        
    elif cmd[0] == 'pop':
        if front == rear:
            print(-1)
        else:
            print(queue[front])
            front += 1 
            
    elif cmd[0] == 'size':
        print(rear - front)
        
    elif cmd[0] == 'empty':
        print(1 if front == rear else 0)
        
    elif cmd[0] == 'front':
        if front == rear:
            print(-1)
        else:
            print(queue[front])
            
    elif cmd[0] == 'back':
        if front == rear:
            print(-1)
        else:
            print(queue[rear - 1])