#코드트리 Trail 5 Intermediate Mid
#Lesson 1 Prefix Sum Challenge
#부분 수열의 합이 K
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
prefix = 0
S = [0]
for a in arr:
    prefix += a
    S.append(prefix)

nums = set(S)
ans = 0
for num in nums:
    if (num - k) in nums:
        ans+=1
print(ans)
