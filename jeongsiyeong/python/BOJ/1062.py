import sys

# 1. 초기 설정
N, K = map(int, sys.stdin.readline().split())

# K가 5보다 작으면 antic도 못 배우니 0 출력
if K < 5:
    print(0)
    exit()
# K가 26이면 다 읽을 수 있으니 N 출력
if K == 26:
    print(N)
    exit()

# 2. 단어들을 비트마스크로 미리 변환
words = []
for _ in range(N):
    s = sys.stdin.readline().strip()
    mask = 0
    for char in s:
        mask |= (1 << (ord(char) - ord('a')))
    words.append(mask)

# 3. 기본 글자(antic) 세팅
base_mask = 0
for char in ['a', 'n', 't', 'i', 'c']:
    base_mask |= (1 << (ord(char) - ord('a')))

# 정답을 저장할 변수
max_count = 0

# 4. DFS 함수 구현 
# idx: 탐색할 알파벳 인덱스 (0~25)
# cnt: 현재까지 배운 글자 수 (초기값 5)
# learned: 현재 배운 글자 비트마스크
def dfs(idx, cnt, learned):
    global max_count
    
    # [종료 조건] 글자를 K개 다 배웠다면?
    if cnt == K:
        count=0
        for word in words:
            if (learned & word) == word:
               count += 1 
        # max_count 갱신
        max_count = max(count, max_count)
        return

    # [탐색] idx부터 25까지 알파벳을 하나씩 추가해보기
    for i in range(idx, 26):
        # 이미 배운 글자(antic)는 건너뛰기
        if not (learned & (1 << i)):
            # 해당 글자를 배우고 재귀 호출
            dfs(i + 1, cnt + 1, learned | (1 << i))

# 5. DFS 실행
dfs(0, 5, base_mask)
print(max_count)