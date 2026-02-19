N = int(input())
#홀수번쨰행은 그냥 출력, 짝수번쨰행은 거꾸로 출력 

# arr = [
#     [0 for _ in range(N)]
#     for _ in range(N)
# ]
for i in range(N):
    # cnt = 1
    for j in range(N):
        # arr.append(cnt)
        # cnt += 1
        if i % 2 == 0:
            print(j+1,end="")
        else:
            print(N-j,end="")
    print()
#             arr.reverse()

# for row in arr:
#     print(*row)


    
