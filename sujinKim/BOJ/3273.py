#첫쨰줄:수열의 크기 n이 주어짐 
n = int(input())

#둘쨰줄:수열에 포함되는 수 많아서 리스트로 묶어봄 
A = list(map(int,input().split()))

#셋째줄 : X
X = int(input())

count = 0 #(a,b)쌍의 갯수 0개로 설정 . 
for a in range(n):  #a 변수가 n번 꺼내지는동안 
      for b in range(n): #b변수도 n번 꺼내짐
            if a + b == X:  #변수 a+b의 합이 X와 같아지면
                  count += 1  #(a,b)쌍의 개수가 +1씩 높아짐 
print(count-1) #개수 "0" 빼기 


#이거 사실 시간초과인데 제 수준에는 이정도로밖에 못쓰는디
#지피티 풀이1
# n = int(input())
# A = list(map(int, input().split()))
# X = int(input())

# seen = set()
# count = 0

# for v in A:
#     need = X - v
#     if need in seen:
#         count += 1
#     seen.add(v)

# print(count)
#지피티풀이2
# n = int(input())
# A = list(map(int, input().split()))
# X = int(input())

# A.sort()
# i, j = 0, n - 1
# count = 0

# while i < j:
#     s = A[i] + A[j]
#     if s == X:
#         count += 1
#         i += 1
#         j -= 1
#     elif s < X:
#         i += 1
#     else:
#         j -= 1

# print(count)
#지피티풀이3
# n = int(input())
# A = list(map(int, input().split()))
# X = int(input())

# exist = [0] * 1000001   # 숫자 등장 여부 체크용
# count = 0

# for v in A:
#     if X - v > 0 and exist[X - v] == 1:
#         count += 1
#     exist[v] = 1

# print(count)

