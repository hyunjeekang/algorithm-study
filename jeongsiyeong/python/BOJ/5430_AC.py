T = int(input().strip())

for _ in range(T):
    cmd = input().strip()
    card_length = int(input().strip())
    card_string = input().strip()
    
    card_string = card_string[1:-1]
    
    if card_string == "":
        card_list = []
    else:
        card_list = list(map(int, card_string.split(',')))
    
    start = 0
    end = card_length
    is_reverse = False
    is_error = False
    
    for c in cmd:
        if c == 'R':
            is_reverse = not is_reverse
        elif c == 'D':
            if start == end:
                is_error = True
                break
            
            if is_reverse:
                end -= 1
            else:
                start += 1
                
    if is_error:
        print('error')
    else:
        result = card_list[start:end]
        
        if is_reverse:
            result.reverse()
            
        print("[" + ",".join(map(str, result)) + "]")