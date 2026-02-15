K, N = map(int, input().split())

# Please write your code here.
answer = []
def backtrack(temp_list):
    if len(temp_list) == N:
        answer.append(temp_list[:])
        return
    for i in range(1, K+1):
        temp_list.append(i)
        backtrack(temp_list)
        temp_list.pop()
backtrack([])
for temp in answer:
    print(*temp)