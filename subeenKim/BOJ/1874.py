N = int(input())
num_list = [int(input()) for _ in range(N)]

i = 0 # 찾고자 하는 수열 인덱스 값
values = [] # 출력할 값을 모을 리스트
stack = []
nums = []

for n in range(1, N+1) :
    stack.append(n)
    values.append('+')

    while stack and stack[-1] == num_list[i] :
        values.append('-')
        nums.append(num_list[i])
        i += 1
        stack.pop()

if nums != num_list :
    print('NO')
else :
    print("\n".join(values))