L, CNT = map(int, input().split())
alphabets = input().split()
aeiou = ['a', 'e', 'i', 'o', 'u']

consonants, vowels = [], []
for alpha in alphabets:
    if alpha in aeiou:
        vowels.append(alpha)
    else:
        consonants.append(alpha)

def backtrack(start_c, start_v, con, vow, selected):
    if con+vow == L:
        word = ''.join(sorted(selected))
        results.append(word)
        return
    
    if con < c:
        for i in range(start_c, len(consonants)):
            selected.append(consonants[i])
            backtrack(i+1, start_v, con+1, vow, selected)
            selected.pop()
    else:
        for i in range(start_v, len(vowels)):
            selected.append(vowels[i])
            backtrack(start_c, i+1, con, vow+1, selected)
            selected.pop()


c = 2
v = L - c
results = []
while c <= len(consonants):
    if v < 1: break
    backtrack(0, 0, 0, 0, [])
    v, c = v-1, c+1

for r in sorted(results):
    print(r)


# 제미나이가 추천해준 방식 (함수가 함수를 단계적으로 호출)

# # 자음을 먼저 다 뽑음
# def c_backtrack(start_c, con, selected_c):
#     if con == c: # 자음 다 뽑으면 이제 모음 뽑으러 감
#         v_backtrack(0, 0, [], selected_c)
#         return
    
#     for i in range(start_c, len(consonants)):
#         selected_c.append(consonants[i])
#         c_backtrack(i+1, con+1, selected_c)
#         selected_c.pop()

# # 그 다음 모음을 뽑음
# def v_backtrack(start, vow, selected_v, selected_c):
#     if vow == v:
#         word = ''.join(sorted(selected_c + selected_v))
#         results.append(word)
#         return
    
#     for i in range(start, len(vowels)):
#         selected_v.append(vowels[i])
#         v_backtrack(i+1, vow+1, selected_v, selected_c)
#         selected_v.pop()

# c = 2
# v = L - c
# results = []
# while c <= len(consonants):
#     if v < 1: break
#     selected_consonants, selected_vowels = [], []
#     c_backtrack(0, 0, [])
#     v, c = v-1, c+1

# for r in sorted(results):
#     print(r)