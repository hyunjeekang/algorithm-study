N = int(input())

n_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(1,10):
    for j in range(1, 10):
        n_lst.append(i*j)

if N in n_lst:
    print(1)
else:
    print(0)