#풀이1
# f1,f2 = map(float,input().split())
# print(f"{f1/f2:.3f}")



#풀이2
# f1,f2 = map(float,input().split(" "))
# print(round(f1/f2,3))

#풀이3
# f1,f2 = map(float,input().split())
# a = f1/f2
# print(round(a,3))

# :.3f의 뜻 : 소수점 3자리 고정 /자동 반올림 / 0도 채워줌 
# round() : 숫자를 가장 가까운 정수로 반올림. 

#올림 ceil() : ceil(2.4)=3
#내림 floor() : floor(3.7)=3

#문자열 포맷팅 
print("{:.0f}".format(3.55555))
print("{:.1f}".format(3.55555))
print("{0}과 {0}".format(3.55555,3.777777))
print("{0}과 {1}".format(3.5463,4.636))
print("{0:.3f}과 {1:.3f}".format(3.55555,3.77777))
#보이는것처럼 {0}은 포맷 함수의 첫번째 인자값을 나타내고 {1}은 두번쨰 인자값을 나타내는듯?
