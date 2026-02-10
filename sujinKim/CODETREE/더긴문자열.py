# a, b=map(int,input().split())

#####바보야......문자열 받아야하는데 자꾸 int 쓸래??? 정수는 길이가 없단 말이여... 
#len()은 어디서든 써도 된당........ 
# #길이가 20이하인 두 개의 단어가 공백을 사이에 두고 주어진다. 
# #출력을 뭘 해야하냐면 첫 번째 줄에 길이가 더 긴 문자열과 길이를 공백 사이에 두고 출력 ...

# if len(a) > len(b):
#     print('a', len(a))

# elif len(a) < len(b):
#     print('b', len(b))

# else:
#     print('same')


# '%s'를 사용해서 문자열을 각각 입력받습니다. 

#문자열을 입력받는다. 
str1, str2 = input().split()
#문자열의 길이를 구한다.
len1 = len(str1)    #길이를 먼저 변수에 할당받아야하나봄 
len2 = len(str2)
#더 긴 문자열과 그 문자열의 길이를 출력한다. 
if len1 > len2:
    print(str1,len1)
elif len1 < len2:
    print(str2,len2)
else:
    print("same")



