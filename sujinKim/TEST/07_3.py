#점수 구간별로 학생 이름 묶기 
def categorize_scores(scores_practice):

    result = {}

    for score in scores_practice:
        name = score['name']
        score = score['score']

        if score >= 90:
            score = 'A'
        elif score  >80:
            score = 'B'
        else:
            score = 'C'

        if score not in result:
            result[score]=[]

        result[score].append(name)

    return result
            

scores = [
    {'name': '민수', 'score': 80},
    {'name': '지연', 'score': 92},
    {'name': '철수', 'score': 75},
    {'name': '영희', 'score': 88}
]

# | 점수    | 그룹  |
# | ----- | --- |
# | 90 이상 | 'A' |
# | 80~89 | 'B' |
# | 80 미만 | 'C' |
print(categorize_scores(scores))
