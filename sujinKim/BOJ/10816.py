N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

dic = {}
for i in arr1:  # arr1에서 하나씩 꺼내는데
    if i in dic:  # dic에 있는 키라면
        dic[i] += 1
    else:  # dic에 없는 키라면
        dic[i] = 1  # 1을 할당해줌

result = []
for j in arr2:
    if j in dic:
        result.append(dic[j])
    else:
        result.append(0)

print(*result)


