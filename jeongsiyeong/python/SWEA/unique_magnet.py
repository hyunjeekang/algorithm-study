from collections import deque

class Magnet:
    def __init__(self):
        self.magnet_q = deque()

    def set_magnet(self, pole_list):
        self.magnet_q = deque(pole_list)
    
    def rotate(self, direction):
        self.magnet_q.rotate(direction)
    
    def get_top_pole(self):
        return self.magnet_q[0]

    def get_right_pole(self):
        return self.magnet_q[2]
    
    def get_left_pole(self):
        return self.magnet_q[6]

T = int(input())

for test_case in range(1, T + 1):
    K = int(input())
    magnets = []
    for _ in range(4):
        m = Magnet()
        m.set_magnet(list(map(int, input().split())))
        magnets.append(m)
        
    for _ in range(K):
        idx, direction = map(int, input().split())
        idx -= 1 
            
        move = [0] * 4
        move[idx] = direction
            
        for i in range(idx, 0, -1):
            if magnets[i].get_left_pole() != magnets[i-1].get_right_pole():
                move[i-1] = -move[i]
            else:
                break
            
        for i in range(idx, 3):
            if magnets[i].get_right_pole() != magnets[i+1].get_left_pole():
                move[i+1] = -move[i]
            else:
                break 
            
        for i in range(4):
            if move[i] != 0:
                magnets[i].rotate(move[i])
        
    total = 0
    for i in range(4):
        if magnets[i].get_top_pole() == 1: 
            total += (2 ** i)
        
    print(f'#{test_case} {total}')
