#백준 1934번 최소공배수
#스터디 발표 예시용으로 추가

#최대공약수(Greatest Common Divisor):유클리드 호제법 + 재귀함수
def gcd(a, b):
    if b ==0:
        return a
    return gcd(b, a%b)

#최소공배수(Least Common Multiple)
def lcm(a, b):
    return a*b//gcd(a,b)

t = int(input())

for _ in range(t):
    a,b = map(int, input().split())
    print(lcm(a,b))