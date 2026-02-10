import sys
input = sys.stdin.readline

arr = list(input().rstrip())  #초기 편집기에 입력되어 있는 문자열 입력받음
M = int(input()) #입력할 명령어 개수 
arr1 = []  #오른쪽 


#arr는 N개인데 그러면 커서는 N+1까지 가능 
#슬라이싱을 하면 for문이랑 if문을 너무 많이 쓰는거 같아서 
#스택? 을 써보자 
# for _ in range(M): #M개의 줄에 걸쳐 입력할 명령어가 순서대로 주어짐 
#         ORDER = input()  #M번 새 명령      
#         if ORDER == 'L':     #커서 왼쪽으로 한칸 옮김
#                 arr1.pop(arr)
#         if ORDER == 'D':     #커서 오른쪽으로 한칸 옮김
#                 arr1.append(arr[:-2]) 
#         if ORDER == 'B': #커서 왼쪽에 있는 문자를 삭제
#                 arr1.pop(arr[:])
#         if ORDER == 'P': #$문자를 커서 왼쪽에 추가함
#                 arr1.append()
                             
for _ in range(M):  #M번 반복하는동안 
    ORDER = input().split() #ORDER에 입력받겠다.

    if ORDER[0] == 'L': #만약 명령어가 L이라면
        if arr:
            arr1.append(arr.pop()) #왼쪽배열 끝의 것을 오른쪽에 넣는다.
            # arr.pop() #왼쪽 배열 끝을 삭제한다
        
    elif ORDER[0] == 'D': #명령어가 D라면
        if arr1:
            arr.append(arr1.pop()) #오른쪽배열 첫번째것을 왼쪽에 넣는다.
            # arr1.pop(0)    #오른쪽 첫번째것을 삭제한다.
        

    elif ORDER[0] == 'B': #명령어가 B라면
        if arr:   #arr가 비워있지 않다면
            arr.pop() #맨 끝에 것을 지운다.
        
        
    else:
        # ORDER[0] == 'P': #명령어의 첫번째가 P라면
 
        arr.append(ORDER[1]) #문자를 추가한다. 


print(''.join(arr)+''.join(reversed(arr1))) #이건 이유를 모르겠네

        
        




