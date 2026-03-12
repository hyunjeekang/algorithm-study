arr = list(map(int, input().split()))

counting = [0]*1000001

for a in arr:
    counting[a] += 1
    
counts = 0

for i in range(1, 1000001):
    counts += counting[i]
    if counts >= 500001:
        print(i)
        break