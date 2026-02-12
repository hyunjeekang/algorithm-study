#KMP 연습문제
#IOIOI
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()
pattern = 'IO' * N + 'I'

# KMP 전처리
def kmp_preprocess(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

lps = kmp_preprocess(pattern)
# KMP 검색
count = 0
i = 0
j = 0
while i < M:
    if S[i] == pattern[j]:
        i += 1
        j += 1
        if j == len(pattern):
            count += 1
            j = lps[j - 1]
    else:
        if j != 0:
            j = lps[j - 1]
        else:
            i += 1
print(count)

