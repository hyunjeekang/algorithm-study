import sys
input = sys.stdin.readline

N = int(input())
num_lst = []

for _ in range(N):
    a = int(input())
    num_lst.append(a)

b = sorted(num_lst, reverse= True)

print('\n'.join(map(str, b)))
