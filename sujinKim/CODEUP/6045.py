#정수 3개가 공백을 두고 입력된다. 
a,b,c = map(int,input().split())
HAP = [a,b,c]
sum_abc = sum(HAP)
avg_abc = sum_abc/len(HAP)

print(sum_abc, f"{avg_abc:.2f}")



#숫자 자료형 종류 (int,float,bool)
#산술연산자 자꾸 헷갈리는거 /(나눗셈,실수결과),//(몫,정수 나눗셈),%(나머지)
#/:무조건 float, //:정수 몫 
# %나머지 연산 특이점 : 나머지를 항상 양수 방향으로 맞춤 
# 연산 우선순위 : ** -> * / // % -> + - 