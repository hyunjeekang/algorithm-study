# 서로다른 L개의 소문자 구성
# 최소 한개의 모음과 두개의 자음
# 알파벳 순서 정렬 배열
# 문자의 종류 C가지일 때 가능서 있는 암호 모두 구하기

# L, C
# C개의 문자들 공백으로 구분되어 주어짐

# L: 암호 길이, C: 문자 개수 입력받기
L, C = map(int, input().split())
# 문자 리스트 입력받고 사전순으로 정렬하기
chars_lst = sorted(list(input().split()))

vowels_lst = ['a', 'e', 'i', 'o', 'u']

def backtrack(start, password):
    # 종료 조건: 암호 길이를 다 채웠을 때
    if len(password) == L:
        for char in password:
            if char in vowels_lst:
                v_count += 1
        
        #모음 한개 이상 2개 이상일 때 출력

        if v_count >= 1 and c_count >= 2:
            print("".join(password))
        return
    
    for i in range(start, C):
        password.append(chars[i])
        backtrack(i + 1, password) # i+1을 넘겨서 다음 문자부터 고르도록 함 (중복 방지)
        password.pop()

backtrack(0, [])