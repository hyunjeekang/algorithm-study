# 퀵정렬 # 분할했더니 정렬이 끝났네 ?
def quick_sort(arr):
    if len(arr) <= 1:  # 리스트의 길이가 1보다 작으면
        return arr  # 그냥 arr를 반환

    p = arr[0]  # 피벗 맨 처음값'
    left = []
    right = []

    for i in range(len(arr)):
        if i == 0:
            continue

        if p >= arr[i]:
            left.append(arr[i])

        elif p < arr[i]:
            right.append(arr[i])

    L = quick_sort(left)
    R = quick_sort(right)

    L.append(p)
    result = L + R
    return result




T = int(input())
for tc in range(1,T+1):
    N = int(input())   # 정수의 개수
    A = list(map(int,input().split())) # N개의 정수 aj가 주어진다.
    ### N/2 원소를 출력한다.
    result = quick_sort(A)


    print(f'#{tc} {result[N//2]}')






