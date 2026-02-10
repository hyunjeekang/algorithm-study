# #문자 10개를 저장할 수 있는 배열을 만든다. 
# arr = [0 for x in range(10)]

# #10개의 문자를 입력받는다.


# #입력받은 문자들을 입력 받은 순서의 역순으로 출력한다. 


# arr = []
# for _ in range(10):
#     P = list(input().split()) 
#     arr.append(P)

# arr.reversed()
# print(arr)


arr = list(input().split()) #배열 arr 선언 

#9부터 0까지의 인덱스에 주어진 문자를 차례대로 출력한다. 
for i in range(9,-1,-1):
    print(arr[i],end="")