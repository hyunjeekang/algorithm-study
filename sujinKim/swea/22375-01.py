#앞에서부터 결정하면 뒤에 영향을 주지만, 이미 결정된 앞부분은 다시 바꿀 필요가 없다.
#는 그리디 전략 !!

#문자열 뒤집기
#0과 1로만 이루어진 두 개의 문자열 A와 B가 있다.
#두 문자열의 길이는 N으로 같다.
#문자열 A를 문자열 B와 똑같이 만들려고 한다.
#작업:i번째 글자를 선택하면, i번째부터 N번째까지의 모든 글자가 반전된다.
import sys
sys.stdin = open("input.txt")
N = int(input()) #A,B의 문자열의 길이
A = list(map(int, input()))
B = list(map(int, input()))
ans = 0
for n in range(N):
    if A[n] != B[n]:
        ans += 1
        #n번째부터 끝까지 상태 반전
        for j in range(n, N):
            if A[j] == 0:
                A[j] = 1
            else:
                A[j] = 0
print(ans)



