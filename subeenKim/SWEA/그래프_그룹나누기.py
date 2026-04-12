T = int(input())

def union_parent(n1, n2):
    parent1 = find_parent(n1)
    parent2 = find_parent(n2)
    if parent1 < parent2:
        group[parent2] = parent1
    else:
        group[parent1] = parent2

def find_parent(n):
    if n == group[n]:
        return n
    return find_parent(group[n])

for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    group = [i for i in range(N+1)]
    for k in range(M):
        s1, s2 = nums[2*k], nums[2*k+1]
        union_parent(s1, s2)

    group_set = set()
    for g in range(1, N+1):
        group_set.add(find_parent(g))
    print(f'#{tc} {len(group_set)}')