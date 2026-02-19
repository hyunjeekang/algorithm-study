# 첫번째 무조건 0
# 두번째 0아니면 1인데 1이면 앞으로
# 세번째는 0,1,2 뽑은 수만큼 앞으로

# 학생의 수 변수 = n 
# 0이면 자리 유지
# 0 < t <= n 일때 현재 보다 - n

n = int(input())
students = list(map(int, input().split()))

ans = []
    
for i in range(n):
    ans.insert(i - students[i], i+1)

print(*ans)