dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def is_range(x, y):
    return x >= 0 and x < 5 and y >= 0 and y < 5

arr = [list(input().split()) for _ in range(5)]

result = set()

for i in range(5):
    for j in range(5):
        stack = [(i, j, arr[i][j])]

        while stack:
            cx, cy, current = stack.pop()
            if len(current) == 6:
                result.add(current)
                continue

            for k in range(4):
                next_x = cx + dx[k]
                next_y = cy + dy[k]
                if is_range(next_x, next_y):
                    stack.append((next_x, next_y, current+arr[next_x][next_y]))
                        
print(len(result))