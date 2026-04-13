# 1. 전차의 움직임 move에 dic 형태로 저장해주기 
# 상호의 배틀싸피 !!!
move = {
    '^' : (-1,0), # 상
    'v' : (1,0), # 하 
    '<' : (0,-1), # 좌 
    '>' : (0,1) # 우 
}

T = int(input())
for tc in range(1,T+1):
    H,W = list(map(int,input().split())) # 맵 크기 
    arr1 = [list(input()) for _ in range(H)] # 맵
    N = int(input()) # 명령어 개수 
    arr2 = input() # 명령어 

# 2. 먼저 맵에서 전차의 위치를 찾고, 전차의 방향도 저장해야함 
# -> 방향에 따라 다르기 떄문임. 
    found = False # 전차 찾았니? 
    for r in range(H): 
        for c in range(W):
            if arr1[r][c] in ['^','v','<','>']: # 이 중에 있다면 
                sr,sc = r,c # 전차의 위치 저장
                direction = arr1[r][c] # 전차의 방향모양도 저장 
                arr1[r][c] = '.' # 그리고 전차 평지로 바꿔줘 -> 전차가 있다 == 갈 수 있다 == 평지다
                found = True # 전차 찾았으니까 True 
                break # 전차 찾았으면 빠져나와 

    for cmd in arr2: # 명령어를 하나씩 꺼내서 볼건데 
        if cmd == 'U': # 명령어가 "U"라면 
            direction = '^' # 윗 방향을 향해야겠찌?
            nr,nc = sr + move[direction][0], sc + move[direction][1] # 긜고 한칸 이동해야하는데
            # 현재 전차 위치에서 + 이동하는데 direction이 '^'였잖아
            # 그래서 거기에 해당하는 move에 키를 direction두고 인덱스로 각각 sr,sc에 더해주기 
            
            #경계췍 항상 필수게찌???  +글고 평지에만 갈수있다 
            if 0 <= nr < H and 0 <= nc < W and arr1[nr][nc] == '.':
                sr,sc = nr,nc # 이동한 위치 다시 현재위치로 바꾸기 


        elif cmd == 'D': # 명령어 'D'라면 
            direction = 'v' # 방향 아래 
            nr,nc = sr + move[direction][0], sc + move[direction][1] # 아래 방향으로 한칸 가는데 
            if 0 <= nr < H and 0 <= nc < W and arr1[nr][nc] == '.': # 경계안, 평지일때만 
                sr,sc= nr,nc 

        elif cmd == 'L':
            direction = '<'
            nr,nc = sr + move[direction][0], sc + move[direction][1]
            if 0 <= nr < H and 0 <= nc < W and arr1[nr][nc] == '.':
                sr,sc = nr,nc

        elif cmd == 'R':
            direction = '>'
            nr,nc = sr + move[direction][0], sc + move[direction][1]
            if 0 <= nr < H and 0 <= nc < W and arr1[nr][nc] == '.':
                sr,sc = nr,nc 

        elif cmd == 'S':  ### 포탄 쏠때 
            ## sr,sc => br,bc => nr,nc => br,bc
            br,bc = sr,sc  # 포탄의 위치 우선 전차의 현재 위치로 할당받아 

            while True:  # 이 안의 코드를 따지지말고 일단 반복해 

                # 포탄이 움직일 위치 
                nr = br + move[direction][0] 
                nc = bc + move[direction][1]

                # 맵 밖으로 갔다면 그만해 ! 
                if not (0 <= nr < H and 0 <=  nc < W):
                    break 
                
                # 벽돌을 만났다면 , 부숴 ( == 평지로 만들어 )
                if arr1[nr][nc] == "*":
                    arr1[nr][nc] = ".":
                    break 

                # 강철을 만났어? 그러면 빠져나와 
                elif arr1[nr][nc] == "#":
                    break 
                
                # 움직인 포탄의 위치 다시 포탄의 위치로 재할당해주기 
                br,bc = nr,nc 

    arr1[sr][sc] = direction # 그래서 맵의 현재 위치에 마지막 방향 할당해주고 
    # 결과 출력 
    print(f"#{tc}", end =" ") 
    for row in arr1:  
        print("".join(row))
