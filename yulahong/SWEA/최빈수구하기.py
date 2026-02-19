# 점수 < 몇번?
# 딕셔너리로 풀어야겠다
# 새로운 딕셔너리 할당

T = int(input())

for tc in range(T, T+1):
    a = input()
    count_dict = {}

    scores = list(map(int, input().split()))
    # 나는 점수 리스트를 돌면서 카운트딕트 딕셔너리에 키값으로 추가하고싶다
    # 만약 나왔던 점수가 또 나오면 누적합을 하고싶다

    for key in scores:
        #점수 리스트에서 키값이 없다면 get함수로 키값을 할당하겠다 그리고 디폴트 값으로 1을 주겠다>.get(key,1)
        count_dict[key] = count_dict.get(key, 0) + 1

print(count_dict)
    #만약 카운트딕트에 




    # print(f'#{tc} {}')