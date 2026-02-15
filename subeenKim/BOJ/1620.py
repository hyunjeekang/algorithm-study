N, M = map(int, input().split())
name_num = {} # 이름이 key, 번호가 value인 딕셔너리
num_name = {} # 번호가 key, 이름이 value인 딕셔너리
for n in range(1, N+1):
    name = input()
    name_num[name] = n
    num_name[n] = name

for _ in range(M):
    pbm = input()
    if pbm.isdecimal():
        print(num_name[int(pbm)])
    else :
        print(name_num[pbm])