import sys

# 입력 처리
l, c = map(int, sys.stdin.readline().split())
inputs = sys.stdin.readline().split()
# 빠른 조회를 위해 미리 정렬해두면 좋습니다
inputs.sort()

vowel = []
constant = []
vo_sample = ['a','e','i','o','u']

for char in inputs:
    if char in vo_sample:
        vowel.append(char)
    else:
        constant.append(char)

# 모음, 자음 각각 정렬 (조합을 뽑을 때 순서를 보장하기 위해)
vowel.sort()
constant.sort()

# 1. (모음 개수, 자음 개수) 쌍 구하기
least_vowel = 1
least_constant = 2
chances = set() # 중복 방지를 위해 set 사용 (기존 dfs는 중복 경로가 생김)

def dfs(vow, con):
    # 가지치기: 남은 자/모음 개수를 초과하면 중단
    if vow > len(vowel) or con > len(constant):
        return

    if vow + con == l:
        chances.add((vow, con))
        return
    
    dfs(vow + 1, con)
    dfs(vow, con + 1)

dfs(least_vowel, least_constant)

final_passwords = []

#2 각 (모음개수, 자음개수) 케이스별로 조합 생성
for vow_cnt, con_cnt in chances:
    
    vows = []
    cons = []
    
    # 모음 조합 구하기
    def dfs_v(index, curr_string):
        if len(curr_string) == vow_cnt:
            vows.append(curr_string)
            return
        if index == len(vowel):
            return
        # 포함하는 경우
        dfs_v(index + 1, curr_string + vowel[index])
        # 포함하지 않는 경우
        dfs_v(index + 1, curr_string)
        
    # 자음 조합 구하기
    def dfs_c(index, curr_string):
        if len(curr_string) == con_cnt:
            cons.append(curr_string)
            return
        if index == len(constant):
            return
        dfs_c(index + 1, curr_string + constant[index])
        dfs_c(index + 1, curr_string)
        
    dfs_v(0, "")
    dfs_c(0, "")

    # 구한 모음/자음 조합을 합치기
    for v_str in vows:
        for c_str in cons:
            # 두 문자열을 합치고 내부 정렬
            comb = sorted(list(v_str + c_str))
            final_passwords.append("".join(comb))

# 3. 모든 케이스가 끝난 후, 전체 리스트를 한 번에 정렬하고 출력
final_passwords = sorted(list(set(final_passwords)))

for pw in final_passwords:
    print(pw)