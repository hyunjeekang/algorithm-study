#14501 퇴사문제
#DP문제
n=int(input())
time=[]
pay=[]
for _ in range(n):
    t,p=map(int,input().split())
    time.append(t)
    pay.append(p)
#dp테이블 생성
dp=[0]*(n+1)
#뒤에서부터 계산
for i in range(n-1,-1,-1):
    #상담이 퇴사일 안에 끝나는 경우
    if i+time[i]<=n:
        dp[i]=max(dp[i+1],pay[i]+dp[i+time[i]])
    else:
        dp[i]=dp[i+1]
print(dp[0])