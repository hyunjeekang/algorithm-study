import sys
sys.stdin = open("input.txt")


N = int(input())
arr = list(int(input()) for _ in range(N))

cnt = [0]*10001 # 1 ~ 10000 [0, 0, 0, 0, ....]

for j in arr:
    cnt[arr[j]] += 1
    

# for i in range(max(arr)+1):  # arr의 가장 큰 수 (어차피 7까지만 있으니까)까지 하나씩 부르겠다
#     for p in range(cnt[i]): # 근데 cnt의 i인덱스에 있는 수만큼 꺼내겠다
#         print("\n".join(map(str,[i for _ in range(p)]))) #TypeError: can only join an iterable

# "THIS IS PYTHON"
# # ========== 1 ============
# print("\n".join(str(i) for i in range(10001) for _ in range(cnt[i])))

# # ========== 2 ============
# result = []
# for i in range(10001):
#     if cnt[i] > 0:
#         result.extend([str(i)]*cnt[i])
#
# # ['1', '1', ..]
# print("\n".join(result))

# " EASY MODE~"
# # ========== 3 ============
for i in range(10001):
    for j in range(cnt[i]): # 알아서 j 횟수만큼 돌아감
        print(i)

# TypeError: sequence item 0: expected str instance, int found
#iterable -> list 자료구조 but, 정수, 실수, 문자열, 참거짓 -> 자료형!
