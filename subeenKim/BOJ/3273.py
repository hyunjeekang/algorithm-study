n = int(input())
a_list = list(map(int, input().split()))
x = int(input())

# i는 리스트의 가장 앞, j는 리스트의 마지막 인덱스에 위치시킨다.
cnt, i, j = 0, 0, n-1
a_list.sort()
while True :
    # 두 수의 합이 x보다 크면 요소의 값이 더 작아야 하기 때문에 j를 한 칸 당긴다.
    if a_list[i]+a_list[j] > x :
        j -= 1
    # 두 수의 합이 x와 같으면 cnt를 늘리고, i는 한 칸 뒤로, j는 한 칸 앞으로 이동시킨다.
    elif a_list[i]+a_list[j] == x :
        cnt += 1
        i, j = i+1, j-1
    # 두 수의 합이 x보다 작으면 요소의 값이 더 커져야 하기 때문에 j를 한 칸 뒤로 이동시킨다.
    else :
        i += 1

    # j가 i와 같아지거나 넘어서면 종료한다.
    if i >= j :
        break
print(cnt)