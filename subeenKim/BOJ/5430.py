from collections import deque

T = int(input())
for _ in range(T):
    dir = 0
    func = input()
    n = int(input())
    arr = input().strip('[]')
    if arr:
        arr = deque(list(map(int, arr.split(','))))
    else :
        arr = deque([])
    answer = []

    for p in func:
        if p == 'R':
            dir = (dir + 1) % 2
        else :
            if dir == 0 and arr : # 처음 순서 방향
                arr.popleft()
            elif dir == 1 and arr : # 처음 순서와 반대 방향
                arr.pop()
            else :
                print('error')
                break
    else :
        answer = '['
        if dir == 1:
            arr = list(arr)[::-1]

        for i, a in enumerate(arr):
            answer += str(a)
            if i < len(arr)-1:
                answer += ','
        answer += ']'
        print(answer)