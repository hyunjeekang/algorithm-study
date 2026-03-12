a, d, k = map(int, input().split())

for i in range(1000000):
    if a + (d * i) == k:
        ans = i + 1
        print(ans)
        break
else:
    print('X')

