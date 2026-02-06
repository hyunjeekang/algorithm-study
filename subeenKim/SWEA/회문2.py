def is_palindrome(word):
    length = len(word)
    for i in range(length//2):
        if word[i] != word[length - 1 - i] :
            return False
    return True
 
def garo(k, text):
    for x in range(len(text)):
        for y in range(len(text)-k+1):
            word = ''.join(text[x][y:y+k])
            if is_palindrome(word) :
                return True
    return False
 
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
    for c in range(100, 1, -1):
        if garo(c, text):
            max_k = c
            break
    answer = max_k
    if max_k < 100 :
        for c in range(100, max_k, -1) :
            if sero(c, text):
                answer = c
                break
    print(f'#{test} {answer}')