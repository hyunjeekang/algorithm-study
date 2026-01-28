N = int(input())
num_cards = set(map(int, input().split()))
M = int(input())
have_cards = list(map(int, input().split()))

for c in have_cards :
    print(1 if c in num_cards else 0, end = ' ')