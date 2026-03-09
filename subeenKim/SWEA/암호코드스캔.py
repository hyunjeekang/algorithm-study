import sys
sys.stdin = open('sample_input.txt')

def change_hex_to_bin(codes):
    hex_to_bin = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110',
              '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100',
              'D':'1101', 'E':'1110', 'F':'1111'}
    new_code = []
    for code in codes :
        n_code = ""
        for c in code :
            n_code += hex_to_bin[c]
        new_code.append(n_code.rstrip('0'))
    return new_code

def find_cipher(code):
    cipher_101 = set()
    cnt_1_0_1 = [0, 0, 0]
    ratio = {(2,1,1):'0', (2,2,1):'1', (1,2,2):'2', (4,1,1):'3', (1,3,2):'4', (2,3,1):'5', (1,1,4):'6', (3,1,2):'7', (2,1,3):'8', (1,1,2):'9'}
    for x in code:
        pwd_code = ""
        y = len(x)-1
        while y >= 0 :
            if x[y] == '1' and cnt_1_0_1[1] == 0: # 맨 뒤 1
                cnt = 0
                while y >= 0 and x[y] == '1':
                    cnt, y = cnt+1, y-1
                cnt_1_0_1[2] = cnt
            elif x[y] == '0' and cnt_1_0_1[2] > 0 and cnt_1_0_1[0] == 0: # 중간 0
                cnt = 0
                while y >= 0 and x[y] == '0':
                    cnt, y = cnt+1, y-1
                cnt_1_0_1[1] = cnt
            elif x[y] == '1' and cnt_1_0_1[1] > 0 : # 앞쪽 1
                cnt = 0
                while y >= 0 and x[y] == '1':
                    cnt, y = cnt+1, y-1
                cnt_1_0_1[0] = cnt
                # 1 0 1 찾기 끝!

                m = min(cnt_1_0_1)
                pwd = (cnt_1_0_1[0]//m, cnt_1_0_1[1]//m, cnt_1_0_1[2]//m)
                if pwd in ratio :
                    pwd_code = ratio[pwd] + pwd_code
                cnt_1_0_1 = [0, 0, 0]

                if len(pwd_code) == 8:
                    cipher_101.add(pwd_code)
                    pwd_code = ""
            else :
                y-= 1
    return cipher_101

def check_is_right(cip):
    odd, even = 0 ,0
    for i in range(7):
        if i % 2 == 1 :
            even += int(cip[i])
        else :
            odd += int(cip[i])
    
    if ((odd*3) + even + int(cip[-1])) % 10 == 0:
        return True
    return False

def sum_cipher(cip):
    total = 0
    for i in cip :
        total += int(i)
    return total

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(set([input().strip().rstrip('0') for _ in range(N)]))
    code = []
    for d in data :
        if d :
            code.append(d)
    ans = 0

    # 암호판 전체를 2진수로 변환
    code2 = change_hex_to_bin(code)

    # 암호 찾기
    cipher_ratio = find_cipher(code2)
    
    # 암호 맞는지 확인하기
    for cipher in cipher_ratio:
        if check_is_right(cipher):
            ans += sum_cipher(cipher)
    
    print(f'#{tc} {ans}')