from collections import deque
T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    pizzas = list(map(int, input().split()))

    q = deque()
    
    for i in range(N):
        q.append((i+1, pizzas[i]))
    next_pizza = N
    last_pizza = 0

    while q:
        pizza_num, cheese = q.popleft()
        cheese//=2
        if cheese == 0:
            if next_pizza < M:
                q.append((next_pizza+1, pizzas[next_pizza]))
                next_pizza+=1

            last_pizza = pizza_num
        else:
            q.append((pizza_num, cheese))
    
    print(f'#{test_case}', last_pizza)
