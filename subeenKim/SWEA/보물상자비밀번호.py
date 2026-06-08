for tc in range(1, 1+int(input())):
    N, K = map(int, input().split())
    nums = input()
    # 똑같은 숫자 배열을 뒤에다가 한 번 더 붙여서 앞으로 돌아올 필요 없이 번호를 이어서 확인할 수 있게 함.
    nums *= 2
    cut = N//4
    pws = set()
    for i in range(cut):
        # i번부터 N개의 숫자를 확인. N//4개씩 끊어서 보자.
        # 반시계방향이긴 하지만 어차피 다 볼거니까 상관없음.
        for k in range(i, i+N, cut):
            pws.add(nums[k:k+cut])
    
    # 아스키코드상으로 문자가 숫자보다 뒤에 있기 때문에 정상적으로 정렬될 것!
    pws = sorted(list(pws), reverse=True)
    result = pws[K-1]
    # 10진수로 변환
    answer = 0
    hex_to_ten = {'0': 0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    for i, r in enumerate(result):
        answer += hex_to_ten[r]*16**(cut-1-i)
    print(f'#{tc} {answer}')