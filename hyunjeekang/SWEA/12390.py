nums = [i for i in range(1, 13)]
def backtracking(index, path):
    global count, N, K

    if len(path) == N:
        if sum(path) == K:
            count += 1
        return

    for i in range(index,len(nums)):
        path.append(nums[i])
        backtracking(i+1, path)
        path.pop()

for t in range(1, int(input())+1):
    count = 0
    N, K = map(int, input().split())
    backtracking(0,[])
    print(f'#{t} {count}')