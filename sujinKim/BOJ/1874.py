import sys
data = sys.stdin.read().split()

n = int(data[0])   #이렇게하면 data[0]=n이 된다는듯? 
stack= []
result = []
current = 1
possible = True
for i in range(1,n+1):  #1부터 n까지
    num = int(data[i])
    # if num == 
    while current <=num:
        stack.append(current)
        result.append("+")
        current += 1

    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        possible = False
        break
if possible:
    print("\n".join(result))c
else:
    print("NO")
