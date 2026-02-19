# import sys
# sys.stdin = open('input.txt')
#방법1(정답아님)
# T = int(input())
#
# for tc in range(1, T+1):  #홀짝으로 풀면 복잡해짐
#     #가장 큰 숫자를 가장 가중치가 낮은곳에 어떻게 먼저 배치?가 규칙
#     N, W1, W2 = map(int, input().split()) #과제 난이도 개수,A의 단계 수,B의 단계 수
#     arr = list(map(int, input().split())) #과제 난이도
#     arr.sort(reverse=True)
#     i=0
#     j=1
#     k=1
#     p=0
#     total_A =0
#     total_B =0
#     if W1 % 2 != 0 : #A단계가 홀수개라면
#         for w1 in range(1, W1+1): #1단계부터 W1단계까지 (A)
#             total_A += arr[i]*w1
#             i += 2
#
#         for w2 in range(1, W2+1): #1단계부터 W2단계까지 (B)
#             total_B += arr[j]*w2
#             j += 2
#     else:
#         for w1 in range(1, W1+1): #1단계부터 W1단계까지 (A)
#             total_A += arr[k]*w1
#             k += 2
#
#         for w2 in range(1, W2+1): #1단계부터 W2단계까지 (B)
#             total_B += arr[p]*w2
#             p += 2
#
#
#
#     total = total_A+total_B
#     print(f'#{tc} {total}')


T = int(input())

for tc in range(1, T+1):
    #가장 큰 숫자를 가장 가중치가 낮은곳에 어떻게 먼저 배치?가 규칙
    N, W1, W2 = map(int, input().split()) #과제 난이도 개수,A의 단계 수,B의 단계 수
    arr = list(map(int, input().split())) #과제 난이도
    arr.sort(reverse=True)

    #전체 가중치 리스트 만들기 !!!
    W = []
    for w1 in range(1, W1+1):
        W.append(w1)
    for w2 in range(1, W2+1):
        W.append(w2)
    W.sort()

    i=0
    total = 0
    for w in W:
        total += arr[i] * w
        i += 1

    print(f'#{tc} {total}')





