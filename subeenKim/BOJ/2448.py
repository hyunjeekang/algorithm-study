N = int(input())

# for h in range(N): # 높이
#     print(' '*(N - ((h//3+1)*3 - 1) - 1), end='')
#     if h % 3 == 0:
#         print('  *   '*(h//3 + 1))
#     elif h % 3 == 1:
#         print(' * *  '*(h//3 + 1))
#     else:
#         print('***** '*(h//3 + 1))

def draw_triangle(n):
    if n == 3:
        return ["  *  ", ' * * ', '*****']
    
    prev_tri = draw_triangle(n//2)
    result = []
    
    # 공백 더하기 (꼭대기 부분 가운데에 놓기)
    for s in prev_tri:
        result.append(" "*(n//2) + s + " "*(n//2))

    # 삼각형 더하기 (밑부분 삼각형 2개 놓기)
    for s in prev_tri:
        result.append(s + " " + s)

    return result
    
print('\n'.join(draw_triangle(N)))