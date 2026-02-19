# A, B= map(int,input().split())

# while A <= B:
#     if A %2 == 1:
#         A *= 2
#     if A%2 == 0:
#         A += 3
# print(A)

inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])
i = a

while i <= b:
    print(i,end=" ")
    if i%2 == 1:
        i *= 2
    else:
        i += 1