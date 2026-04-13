N = int(input())
num_lst = []

for _ in range(N):
    a = int(input())
    num_lst.append(a)

b = reversed(num_lst)

for i in b:
    print(i)