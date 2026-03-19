from collections import deque

start = input()
end = input()
dec_end = int(end, 2)

q = deque([(start, 0)])
visited = set()
visited.add(int(start, 2))

while q:
    bin_x, cnt = q.popleft()
    dec_x = int(bin_x, 2)
    if dec_x == dec_end:
        print(cnt)
        break
    for i in range(len(bin_x)-1):
        if dec_x^(1<<i) not in visited:
            visited.add(dec_x^(1<<i))
            q.append((bin(dec_x^(1<<i))[2:], cnt+1))
    if dec_x+1 not in visited:
        visited.add(dec_x+1)
        q.append((bin(dec_x+1)[2:], cnt+1))
    if dec_x!=0 and dec_x-1 not in visited:
        visited.add(dec_x-1)
        q.append((bin(dec_x-1)[2:], cnt+1))

