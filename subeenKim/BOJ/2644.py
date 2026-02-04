n = int(input())
A, B = map(int, input().split())
m = int(input())
family = {}

for i in range(m) :
    parent, child = map(int, input().split())
    # family 딕셔너리에 {key: [value], key: [value1, value2]} 형태로 저장
    if parent in family.keys() :
        family[parent].append(child)
    else :
        family[parent] = [child]

#  A의 조상 다 구하기
A_anc, stack = {A:0}, [(A, 0)]
while stack :
    num, chon = stack.pop()
    for P, C in family.items() :
        if num in C :
            A_anc[P] = chon+1
            stack.append((P, chon+1))
# B의 조상 다 구하기
B_anc, stack = {B:0}, [(B, 0)]
while stack :
    num, chon = stack.pop()
    for P, C in family.items() :
        if num in C :
            B_anc[P] = chon+1
            stack.append((P, chon+1))
            
is_family = False

for a in list(A_anc.keys()) :
    for b in list(B_anc.keys()) :
        if a == b :
            is_family = True
            break
    if is_family :
        break

if is_family :
    print(A_anc[a] + B_anc[b])
else :
    print(-1)