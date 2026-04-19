l, c = map(int, input().split())
chars = sorted(input().split())

vowels = {'a', 'e', 'i', 'o', 'u'}

def backtracking(index, cur_pw):
    if len(cur_pw) == l:
        v_count = 0
        c_count = 0
        
        for char in cur_pw:
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
        if v_count >= 1 and c_count >= 2:
            print(cur_pw)
        return
    
    for i in range(index, c):
        backtracking(i+1, cur_pw+chars[i])

backtracking(0, "")