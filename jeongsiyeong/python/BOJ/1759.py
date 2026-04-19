l, c = map(int, input().split())
inputs = list(input().split())
inputs.sort()

vowel = []
constant = []
vo_sample = {'a','e','i','o','u'}

results = []

for mask in range( 1 << c):
    if bin(mask).count('1') == l:
        cur_pw  = ""
        v_count = 0
        c_count = 0
        
        for j in range(c):
            if (mask & (1 << j)) != 0:
                char = inputs[j]
                cur_pw += char
                if char in vo_sample:
                    v_count += 1
                else:
                    c_count += 1
        if v_count >= 1 and c_count >= 2:
            results.append(cur_pw)

results.sort()
for pw in results:
    print(pw)