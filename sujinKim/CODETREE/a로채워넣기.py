# STR = input()
# # NEW_STR = STR.replace(STR[1],'a')
# #문자열에서 'e'를 전부 'a'로 바꿔라 
# # NEW_STR = NEW_STR.replace(NEW_STR[-2],'a')
# NEW_STR = STR.replace(STR[1],'a',1)
# NEW_STR = NEW_STR.replace(NEW_STR[-2],'a',1)
# print(NEW_STR)

#replace 말고 슬라이싱 

STR = input()
NEW_STR = STR[:1] + 'a' + STR[2:-2] + 'a' + STR[-1]
print(NEW_STR)


#슬라이싱 하는 방법을 알게됨. 항상 인덱스를 조심하자 
#차조심 사람조심 인덱스조심 
