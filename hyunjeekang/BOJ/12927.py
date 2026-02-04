import sys

input_data = sys.stdin.readline().strip()
N = len(input_data)

on_lamps = {i for i, state in enumerate(input_data, 1) if state == 'Y'}
ans = 0

for i in range(1, N + 1):
    if i in on_lamps:
        ans += 1
        
        for j in range(i, N + 1, i):
            if j in on_lamps:
                on_lamps.remove(j)
            else:
                on_lamps.add(j)

print(ans)