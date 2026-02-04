#문제1
#학생정보 
#students = [
   # {'name': '민수', 'class_': 'A'},
   # {'name': '지연', 'class_': 'B'},
    # {'name': '철수', 'class_': 'A'},
   # {'name': '영희', 'class_': 'B'},
    #{'name': '준호', 'class_': 'C'}
#]
#결과 
#{
 #'A': ['민수', '철수'],
 #'B': ['지연', '영희'],
 #'C': ['준호']
#}

def categorize_students(students_):
    result = {}
    for student in students_:
        class_ = student['class_']
        name = student['name']

        if class_ not in result:
            result[class_]=[]

        result[class_].append(name)

    return result
students = [
   {'name': '민수', 'class_': 'A'},
   {'name': '지연', 'class_': 'B'},
    {'name': '철수', 'class_': 'A'},
   {'name': '영희', 'class_': 'B'},
    {'name': '준호', 'class_': 'C'}
]
print(categorize_students(students))
# {
#  'A': ['민수', '철수'],
#  'B': ['지연', '영희'],
#  'C': ['준호']
# }


