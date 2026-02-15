N = int(input()) #그냥 정수 

# a=1 #초기값 
sum_val = 0 
for i in range(1,101): # i를 1부터 100까지 1,2,3,4,5,6,...100 이런식으로 
    sum_val += i
    #초기값 a = a + i 이러면 
    # a = 0 + 1 = 1
    # a = 1 + 2 = 3
    # a = 3 + 3 = 6
    # a = 6 + 4 = 10 

    # b = 1 + 2 = 3
    # b = 3 + 3 = 6
    # b = 3 + 3 = 7

    if sum_val >= N:
        print(i)
        break
