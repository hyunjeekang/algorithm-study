n = int(input())

a=[1]
for i in range(1, n+1):
    c = 2**i
    a.append(c)

print(*a)