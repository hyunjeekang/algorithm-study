#백준 31432-소수가 아닌 수 3

n = int(input())
arr = list(input().split())

print("YES")
num = arr[0]

if num == '0':
    print(0)
else:
    print(num * 3) #모든 자리 숫자의 합이 3의 배수이면 3의 배수->소수가 아님!