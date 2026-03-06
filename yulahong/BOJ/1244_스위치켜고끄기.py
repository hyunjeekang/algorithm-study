# 스위치 번호 = 인덱스로 활용
# 1 = 켜져있음
# 0 = 꺼져있음
# 학생들 받은 수 1 <= 자연수 <= 스위치 개수
# 남학생: 스위치 번호 자기가 받은 수의 배수이면 스위치 상태 바꿈
# 여학생: 자신이 받은 수와 같은 번호의 스위치를 중심으로 좌우가 대칭이면서 
# 가장 많은 스위치 포함하는 구간 찾아서 그 구간 속 스위치 다 바꿈

#변수
switch_num = int(input()) #스위치의 개수
switch = list(map(int, input().split()))
students_num = int(input())

students_info = []
for _ in range(students_num): 
    a, b = map(int, input().split()) #a =  학생 성별 b = 학생이 받은 번호
    students_info.append((a, b))




#로직
# 학생 리스트 인덱스 0번에 3추가 > insert(0,3) 사용
new_switch = [3] + switch
# 학생 정보에서 정보 순회> for i in stuedents_info
for i in students_info:
    #남학생일 때 i[0] == 1
    # for j in range(스위치개수+1)
    # 번호표 숫자 배수 구하기 > i[1]*j 조건 > swith_num보다 작을 때까지
    # 조건에 맞는 i[1]*j 새로운 리스트>idx_list 에 저장 
    # idx리스트 순회하면서 인덱스 번호에 부합하는 스위치 번호 바꾸기

    if i[0] == 1:
        step = i[1]

        for idx in range(step, switch_num+1, step):
            if new_switch[idx] == 0:
                new_switch[idx] = 1
            else:
                new_switch[idx] = 0
    
    # #여학생일 때 i[0] == 2
    else:
        # 시작점 스왑 
        if new_switch[i[1]] == 0:
            new_switch[i[1]] = 1
        elif new_switch[i[1]] == 1:
            new_switch[i[1]] = 0
        # print(new_switch)      

        # 범위 안쪽 & 대칭을 만족할 때까지(좌와 우의 값이 같다)
        #   좌의 값도 스왑, 우의 값도 스왑
        j = 1
        while i[1]+j <= switch_num and 0 < i[1]-j  and new_switch[i[1] + j] == new_switch[i[1] - j]:
            if new_switch[i[1] + j] == 0 and new_switch[i[1] - j] == 0:
                new_switch[i[1] + j] = 1 
                new_switch[i[1] - j] = 1
            else:
                new_switch[i[1] + j] = 0
                new_switch[i[1] - j] = 0     

            j+=1

new_switch.pop(0)
ans = new_switch   

# 1- 20 : 1
# 21- 40: 2
# 41 - 60: 3

if switch_num % 20 == 0:
    row_cnt = switch_num // 20
else:
    row_cnt = (switch_num // 20) + 1

for i in range(row_cnt):
    print(*ans[20*i:20*i+20])
