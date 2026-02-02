light = int(input())
status = list(map(int, input().split()))
student = int(input())
action = [list(map(int, input().split())) for _ in range(student)]

for sex, num in action :
    if sex == 1 :
        for i in range(num-1, light, num) :
            status[i] = 1 - status[i]
    else :
        start, end = num - 1, num - 1
        while start-1 >= 0 and end+1 < light :
            if status[start - 1] != status[end + 1] :
                break
            else :
                start, end = start - 1, end + 1

        for i in range(start, end +1) :
            status[i] = 1 - status[i]

for i, s in enumerate(status) :
    if i//20 >= 1 and i%20 == 0 :
        print()
    print(s, end = ' ')
