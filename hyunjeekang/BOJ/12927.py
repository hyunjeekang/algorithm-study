lamps = [0] + [1 if x == 'Y' else 0 for x in input().strip()]
n = len(lamps)
cnt = 0

for i in range(1, n):
    if lamps[i] == 1:
        cnt += 1
        for j in range(i, n, i):
            lamps[j] = 1 - lamps[j]

print(cnt)