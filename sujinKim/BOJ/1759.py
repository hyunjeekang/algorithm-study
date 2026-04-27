## 암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a,e,i,o,u)과 최소 두 개의 자음으로 구성되어 있다고 알려져 있다. 
## 정렬된 문자열을 선호하는 조교들의 성향으로 미루어 보아 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측된다. 
# 즉, abc는 가능성이 있는 암호이지만 bac는 그렇지 않음

# 새 보안 시스템에서 조교들이 암호로 사용했을 법한 
# 근데 순서를 생각 안해도 되는점 == 오름차순 
import sys
L,C = map(int,input().split())

arr = sorted(sys.stdin.readline().split()) # 글자 입력받으면서 정렬 
result = [] # 담는곳 
moeum = ['a','e','i','o','u']
j = 0 # 자음 개수
m = 0 # 모음 개수 

# 조합 (근데 오름차순이라 순서를 고려하지 않아도 되는 !>.. )
def BACK(start,depth):  # 조합은 앞에 순서만 바꾸니까 

    # 종료 조건 
    if depth == L:

    #모음 개수 세기 
        for i in result:
            if i in moeum:
                m += 1
            else: # 자음일때 
                j += 1

        
    # 조건 확인 ( 모음 1개 이상 , 자음 2개 이상 ) == if문으로 해야할듯 
        if m >= 1 and j >= 2:
            result.append()
    # 조합 뽑기(정렬된 arr에서 하나씩 뽑았다가 다시 뺴면서 )
    for p in range(start,C):
        result.append(arr[p])
        BACK()??
        

