arr = [0] * 100

n = int(input())

for _ in range(n):
    c, r = map(int, input().split())
    # 11..1 을 가로 길이만큼 시프트
    b_paper = ((1 << 10) - 1) << c

    for i in range(r, r + 10):
        arr[i] |= b_paper

mx_area = 0

for r in range(100):
    cur_bits = arr[r]

    for i in range(r, 100):
        cur_bits &= arr[i]

        if cur_bits == 0:
            break

        height = i - r + 1

        width = 0
        tmp = cur_bits
        while tmp > 0 :
            tmp &= (tmp << 1)
            width += 1
        
        mx_area = max(mx_area, width * height)
print(mx_area)