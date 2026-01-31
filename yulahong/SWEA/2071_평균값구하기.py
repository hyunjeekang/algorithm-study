T = int(input())

for tc in range(1, T + 1):
    num = list(map (int, input().split()))
    a = sum(num)/10
    b = int(a + 0.5)
   
   
print(f'#{tc} {b}')
    




