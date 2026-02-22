# N장의 카드
# 카드는 1-N 번호가 있음 > 인덱스 하나씩 밀면 같겠다
# 1번카드가 제일 위, N번이 제일 아래
# 제일 위 바닥에 버린 후 그 다음 카드 제일 아래로 옮김


from collections import deque

N = int(input())
card_lists = deque(range(1, N+1))

while len(card_lists) > 1:
    card_lists.popleft()
    card_lists.append(card_lists.popleft())

print(card_lists[0])