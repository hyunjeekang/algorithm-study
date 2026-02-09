for tc in range(1, 11):
    N = int(input())
    magnetic = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    for y in range(N):
        stack = []
        for x in range(N):
            if magnetic[x][y] != 0 :
                # 스택이 비어있는 상황에서는 첫 값으로 S극 받지 않음 (N극에 딸려감)
                if not stack and magnetic[x][y] == 2:
                    continue
                stack.append(magnetic[x][y])
        
        # 맨 뒤에 연이어 있는 N극 삭제
        while stack and stack[-1] == 1:
            stack.pop()

        # N극 > S극 으로 바뀔 때마다 cnt +1
        if not stack :
            continue
        prev = stack.pop()
        while stack :
            now = stack.pop()
            if prev != now and now == 1:
                cnt += 1
            prev = now
    print(f'#{tc} {cnt}')