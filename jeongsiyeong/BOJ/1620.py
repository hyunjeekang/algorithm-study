M, N = map(int, input().split())

for_dict = {}
rev_dict = {}
for idx in range(1, M+1):
    mon_name = input()
    for_dict.setdefault(idx, mon_name)
    rev_dict.setdefault(mon_name, idx)

for q in range(N):
    query = input()
    if query.isdecimal():
        print(for_dict[int(query)])
    else:
        print(rev_dict[query])