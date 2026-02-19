# #자연수로 이루어진 2행 4열의 배열이 공백을 사이에 두고 주어진다. 
# row = 2
# col = 4
# arr = [list(map(int,input().split())) for _ in range(row)]

# #가료평균구하기 
# for r in range(row):
#     sum_val = 0
#     for c in range(col):
#         sum_val += arr[r][c]
#     print(f'{sum_val/4:.1f}',end=' ')
# print()

# #세로평균구하기 
# for c in range(col):
#     sum_val = 0
#     for r in range(row):
#         sum_val += arr[r][c]
#     print(f'{sum_val/2:.1f}',end=' ')
# print()

# #전체평균
# # sum_val=0
# # for r in range(row):
# #     for c in range(col):
# #         sum_val += arr[r][c]
# #     print(f'{sum_val/8:.1f}')
# sum_val=0
# for i in range(4):
#     for j in range(2):
#         sum_val += arr[j][i]
#     print(f'{sum_val/8:.1f}')

    

# 2차원 배열을 구현해 각 줄마다 정수를 입력받습니다.
arr_2d = [
	list(map(int, input().split()))
	for _ in range(2)
]

# 가로 평균을 출력합니다.
for i in range(2):
	sum_val = 0
	for j in range(4):
		sum_val += arr_2d[i][j]
	print(f"{sum_val / 4:.1f}", end=" ")
print()

# 세로 평균을 출력합니다.
for j in range(4):
	sum_val = 0
	for i in range(2):
		sum_val += arr_2d[i][j]
	print(f"{sum_val / 2:.1f}", end=" ")
print()

# 전체 평균을 출력합니다.
sum_val = 0
for i in range(4):
	for j in range(2):
		sum_val += arr_2d[j][i]
print(f"{sum_val / 8:.1f}")
