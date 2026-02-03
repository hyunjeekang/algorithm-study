def solve():
    K, N, M = map(int, input().split())
    charger_list = list(map(int, input().split()))

    charging_stop = [False] * (N + 1)
    for m in charger_list:
        charging_stop[m] = True

    cur_stop = 0
    charge_count = 0

    while cur_stop + K < N:
        next_stop = cur_stop + K

        while next_stop > cur_stop and not charging_stop[next_stop]:
            next_stop -= 1

        if next_stop == cur_stop:
            return 0

        charge_count += 1
        cur_stop = next_stop

    return charge_count


T = int(input())
for tc in range(1, T + 1):
    result = solve()
    print(f'#{tc} {result}')