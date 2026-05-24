# 도착점까지 가는 게임, 계단 밟으면 점수 얻음
# 계단은 한번에 한 계단 혹은 두 계단
# 연속된 세개 밟으면 안됨(시작점은 계단 미포함)> 조건 걸기
# 마지막 도착 계단은 무조건 밟기
# 최댓값 출력

# 인풋
# 첫줄 = 계단의 개수
# 둘째 줄부터 게단에 쓰여있는 점수 > 인덱스 활용

t = int(input())
stair_scores  = [] # [10, 20, 15, 25, 10, 20]
visited = [0]*(t+2) #[0, 0, 0, 0, 0, 0, 0]
max_ans = 0

for _ in range(t):
    a = int(input())
    stair_scores.append(a)

# 인덱스 사용할 계단 리스트
scores = [0] + stair_scores # [0, 10, 20, 15, 25, 10, 20]

# def dfs(ground, score, step):
#     global max_ans
    
#     # print(ground, score, step)
    
    
#     visited[ground] = 1
#     if ground <= 0:
#         max_ans = max(max_ans, score )
#         # 뭘 리턴할건지
#         return
        
#         # 최조지점
#         # socres[t+1] -> ground(==0)이 될 때가지 보내기
#     for i in range(1,3):
#         # if visited[ground + 1] == 1 and i == 1:
#         if step == 2 and i == 1 and ground != 1:  
#             continue
        
#         if ground - i < 0:
#             break
#             # ground - 1 가지마
        
#         if i != 1:
#             dfs(ground - i, score + scores[ground - i], 1)
#         else:
#             dfs(ground - i, score + scores[ground - i], step+1)
#         visited[ground - i] = 0
            
# dfs(t, scores[t], 1)
# print(max_ans)

def dfs(ground, score):
    global max_ans
    
    # print(ground, score, step)
    
    
    visited[ground] = 1
    if ground <= 0:
        max_ans = max(max_ans, score )
        # 뭘 리턴할건지
        return
        
        # 최조지점
        # socres[t+1] -> ground(==0)이 될 때가지 보내기
    for i in range(1,3):
        if visited[ground + 1] == 1 and i == 1 and ground != 1:
        # if step == 2 and i == 1 and ground != 1:  
            continue
        
        if ground - i < 0:
            break
            # ground - 1 가지마
        
        if i != 1:
            dfs(ground - i, score + scores[ground - i])
        else:
            dfs(ground - i, score + scores[ground - i])
        visited[ground - i] = 0
            
dfs(t, scores[t])
print(max_ans)
            
        # 재귀/ dfs
        # 인덱스로
        # 현재 방문한 곳이 직전 방문한 곳과 인덱스 연속되면 그 다음 연속된 인덱스는 방문하지 못하도록 조건
 
    
# 내려오면서 더하면서 내려오가
# 스코어스의 인덱스가 1이나 2가 됐을 때 더한 최종 값 반환
# max() 함수로 비교해서 최댓값 도출


#로직
# 분기가 나눠짐 
# 10
#     -20
#         -25
#             -20(끝)
#     -15
#         -25
#             -20(끝)
#         -10
#             -20(끝)
# 20
#     -15
#         -10
#             -20(끝)
#     -25
#         -10
#             -20(끝)
#         -20(끝)
# 다음이랑 다다음만 보면 됨
# 만약 3개 연속이면 다시 돌아오기

# 끝점이 고정이니까 끝에서부터 계산하기
# 방문처리해서 다시 안 방문하게 만들기
# dfs

# 되는 경우 다 구해서 저장해서 max함수 써서 답 출력