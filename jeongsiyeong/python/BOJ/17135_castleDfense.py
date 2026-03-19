import itertools
N, M, D = map(int, input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

def dist(r1,c1,r2,c2):
    return abs(r1-r2)+abs(c1-c2)

def copy_arr(arr):
    temp_arr = [line[:] for line in arr]
    return temp_arr

archers = list(itertools.combinations(range(M),3))

mx_kill = -1

for archer in archers:
    temp_arr = copy_arr(arr)
    kill = 0

    for turn in range(N):
        targeted = set()

        for a_c in archer:
            a_r= N
            closest_dist = float('inf')
            target = None

            for m_r in range(N):
                for m_c in range(M):
                    if temp_arr[m_r][m_c] == 1:
                        d = dist(a_r, a_c, m_r, m_c)
                        if  d<= D:
                            if d < closest_dist:
                                closest_dist = d 
                                target = (m_r, m_c) 
                            elif d == closest_dist and target:
                                if m_c < target[1]:
                                    target = (m_r, m_c)
            if target:
                targeted.add(target)
        for r, c in targeted:
            temp_arr[r][c] = 0
            kill += 1
        temp_arr.pop()
        temp_arr.insert(0, [0]*M)
    mx_kill = max(mx_kill, kill)

print(mx_kill)


