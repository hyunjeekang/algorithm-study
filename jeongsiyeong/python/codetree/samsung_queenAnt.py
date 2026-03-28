def build_town(houses):
    global house_id_counter
    for house in houses:
        alive_house[house_id_counter] = house
        house_id_counter += 1

def build_house(house):
    global house_id_counter
    alive_house[house_id_counter] = house
    house_id_counter+=1
    
def crash_house(house_idx):
    if house_idx in alive_house:
        del alive_house[house_idx]

def patrol_house(ant_num):
    targets = sorted(list(alive_house.values()))
    
    if not targets or ant_num >= len(targets):
        print(0)
        return
    
    left = 0
    right = targets[-1]
    answer = right
    
    while left <= right:
        mid = (left + right)//2
        
        used_ants = 0
        i = 0
        
        while i < len(targets):
            used_ants += 1
            cover_limit = targets[i] + mid
            
            while i < len(targets) and targets[i] <= cover_limit:
                i += 1
        if used_ants > ant_num:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1
    print(answer)
                
#여왕 개미가 내린 명령의 수 Q
Q = int(input())

#살아있는 집 번호
alive_house = {}
house_id_counter = 1
#Q줄에 걸쳐 한 줄에 하나씩 명령
for _ in range(Q):
    cmds = list(map(int, input().split()))
    if cmds[0] == 100:
        #마을 건설
        build_town(cmds[2:])
    elif cmds[0] == 200:
        #개미집 건설
        build_house(cmds[1])
    elif cmds[0] == 300:
        #개미집 철거
        crash_house(cmds[1])
    elif cmds[0] == 400:
        #개미집 정찰
        patrol_house(cmds[1])