import sys

# 입력 속도를 위해 sys 사용 (필수)
input = sys.stdin.readline

M = int(input())
result = 0  # [수정1] 반복문 밖에서 선언하여 값 유지

for _ in range(M):
    line = input().split()
    cmd = line[0]

    if cmd == 'all':
        # 1~20번 비트를 모두 1로 만듦 (1 << 21은 21번째 비트가 1이고 뒤가 다 0인 수. 여기서 1을 빼면 뒤가 다 1이 됨)
        result = (1 << 21) - 1
    elif cmd == 'empty':
        result = 0
    else:
        # [수정2] 정수형으로 변환
        num = int(line[1])

        if cmd == 'add':
            result |= (1 << num)
        elif cmd == 'remove':
            result &= ~(1 << num)
        elif cmd == 'check':
            # [수정3] 있으면 1, 없으면 0 출력
            if result & (1 << num):
                print(1)
            else:
                print(0)
        elif cmd == 'toggle':
            result ^= (1 << num)