N = int(input())
# 알파벳 소문자로 이루어진 단어를 길이가 짧은 것부터 ! 같다면 사전순으로 ! 
result = []
for i in range(N):
    arr = input()  # 단어 하나씩 받아서 받을때마다 result에 넣고, 
    
    result.append(arr)
result = list(set(result))
# result = list(result)
result.sort(key=lambda x:(len(x),x))  # 그걸 result에 싹 넣어서 sort정렬 
# 길이가 같은 경우 사전순으로 

for j in result:
    print(j)


# class를 만들어서 우선순위로 정렬할 수 있는 기능 
# 다른언어로 






