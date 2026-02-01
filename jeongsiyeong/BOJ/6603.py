# 백준 6603번-로또
# 0이 입력 될때까지 수행 반복한다.
# 한 줄에 주어진 숫자들 중 첫 숫자는 로또의 수(범위)
# 나머지 숫자들로 가능한 모든 숫자 조합을 출력한다(콤비네이션)
# 백트래킹 문제
import sys

def backtrack_comb(idx, current_picks, array):
    if len(current_picks)==6:
        print(*current_picks)
        return

    for i in range(idx, len(array)):
        backtrack_comb(i+1, current_picks+[array[i]], array)

lines = sys.stdin.readlines()

for i, line in enumerate(lines):
    line_array = list(map(int, line.split()))
    
    if line_array[0] == 0:
        break

    array = line_array[1:]
    k = line_array[0]

    result=[]
    backtrack_comb(0, result, array)

    next_line = lines[i+1].strip()
    if next_line != '0':
        print()

