def solve():
    dump_limit = int(input())
    boxes = list(map(int, input().split()))


    counts = [0] * 101
    min_h = 100
    max_h = 1

    for h in boxes:
        counts[h] += 1
        if h < min_h: min_h = h
        if h > max_h: max_h = h

    for _ in range(dump_limit):
        if max_h - min_h <= 1:
            break

        counts[min_h] -= 1
        counts[min_h + 1] += 1

        counts[max_h] -= 1
        counts[max_h - 1] += 1

        if counts[min_h] == 0:
            min_h += 1
        if counts[max_h] == 0:
            max_h -= 1

    return max_h - min_h

for tc in range(1, 11):
    result = solve()
    if result is not None:
        print(f'#{tc} {result}')