
T = int(input())
N = int(input())
MAX_R = 200

rects = [
    tuple(map(int,input().split()))
    for _ in range(N)
]

checked = [
    [0]*(MAX_R+1)
    for _ in range(MAX_R+1)
]

for r1,c1,r2,c2, in range(N):

    for x in range(r1,r2):
        for y in range(c1,c2):
             checked[r][c] += 1

count2 = 0

for x in range(MAX_R):
    for y in range(MAX_R):
        if checked[r][c] >= 2:
            count2 += 1
            

print(count2)


