N = int(input())
for i in range(N):
    print("*"*(i+1),end="")
    print(" "*(2*N-2*(i+1)),end="")
    print("*" * (i + 1))

for j in range(N,0,-1):
    print("*"*(j-1),end=" ")
    print(" "*(2*N-2*j),end=" ")
    print("*"*(j-1))