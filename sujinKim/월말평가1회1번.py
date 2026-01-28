#문제 및 오답노트
#스마트팜관리시스템을개발중인김싸피는센서로부터수집된온습도데이터를분석하려고합니다.
#하루동안수집된온도가리스트로주어질때, 평균온도를실수(float)형태로반환하는calculate_avg함수를완성하시오.############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
#1
def calculate_avg(temperatures):

    hap = 0
    length = 0
    for i in temperatures:
        hap = hap + i
        length = length + 1

    return hap/length
#2
    # a = sum(temperatures)/len(temperatures)
    # return a

#####################################################
# 아래 코드를 삭제하는 경우
# 모든 책임은 삭제한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(calculate_avg([20, 25, 30, 22, 28]))  # 25.0
print(calculate_avg([10, 10, 10]))          # 10.0
print(calculate_avg([1, 2, 4]))          # 2.3333333333333335
#####################################################