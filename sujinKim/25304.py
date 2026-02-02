X = int(input()) #영수증에 적힌 총 금액
N = int(input()) #구매한 물건의 종류의 수 


total = 0 #총 금액 0으로 설정 
for i in range(N): #구매한 물건의 종류를 한개씩 꺼냈을때
    a,b = map(int,input().split()) #그 종류의 가격과 물건수를 입력받는다.
    total = total + a*b #그때 총금액을 누적해서 더하기 
if total == X: #그 누적한 총금액이 영수증에 적힌 금액과 같을떄
    print("Yes") #예스출력
else:
    print("No") #아니면 노 출력 
    