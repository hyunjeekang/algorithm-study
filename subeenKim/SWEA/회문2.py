# 회문인지 아닌지 판단하는 함수
def is_palindrome(word):
    length = len(word)
    for i in range(length//2):
        if word[i] != word[length - 1 - i] :
            return False
    return True

# 가로 줄을 확인하는 함수
def garo(k, text):
    for x in range(len(text)):
        for y in range(len(text)-k+1):
            word = ''.join(text[x][y:y+k])
            if is_palindrome(word) :
                return True
    return False

# 세로 줄을 확인하는 함수
def sero(k, text):
    for y in range(len(text)):
        for x in range(len(text)-k+1):
            word = ''.join(text[i][y] for i in range(x, x+k))
            if is_palindrome(word):
                return True
    return False
             
for _ in range(1, 11):
    test = int(input().strip())
    text = [list(input().strip()) for _ in range(100)]
    max_k = 0
    for c in range(100, 1, -1): # 뒤에서부터 탐색하고 회문을 찾으면 바로 멈춤
        if garo(c, text):
            max_k = c
            break
    answer = max_k
    if max_k < 100 :
        for c in range(100, max_k, -1) : # 이전에 찾은 최대 k값보다 큰 k에 대해서만 탐색
            if sero(c, text):
                answer = c
                break
    print(f'#{test} {answer}')