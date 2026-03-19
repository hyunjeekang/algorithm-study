n = int(input())
numbers = list(map(int, input().split()))
#덧셈, 뺄셈, 곱셈, 나눗셈
operators = list(map(int, input().split()))
results=[]

def dfs(index, current_result, plus, minus, mul, div):
    if index == n:
        results.append(current_result)
        return
    if plus > 0:
        next_result = current_result + numbers[index]
        dfs(index+1, next_result, plus-1, minus, mul, div)
    if minus > 0:
        next_result = current_result - numbers[index]
        dfs(index+1, next_result, plus, minus-1, mul, div)
    if mul > 0:
        next_result = current_result * numbers[index]
        dfs(index+1, next_result, plus, minus, mul-1, div)
    if div > 0:
        next_result = int(current_result/ numbers[index])
        dfs(index+1, next_result, plus, minus, mul, div-1)

dfs(1,numbers[0],*operators)

print(max(results))
print(min(results))