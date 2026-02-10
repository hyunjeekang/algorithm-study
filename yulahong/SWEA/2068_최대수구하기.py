T = int(input())

for tc in range(1, T+1):
    my_list = list(map(int, input().split()))
    a = max(my_list)
    print(f'#{tc} {a}')