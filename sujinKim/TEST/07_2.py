#색깔별로 과일 이름 묶기
def categorize_fruits(fruits_f):
    result = {}

    for fruit in fruits_f:
        color = fruit['color']
        name = fruit['name']

        if color not in result:
            result[color]=[]
        
        result[color].append(name)

    return result


fruits = [
    {'name': '사과', 'color': '빨강'},
    {'name': '딸기', 'color': '빨강'},
    {'name': '바나나', 'color': '노랑'},
    {'name': '포도', 'color': '보라'},
    {'name': '레몬', 'color': '노랑'}
]

print(categorize_fruits(fruits))