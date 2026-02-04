def categorize_order(orders_many):

    result={}

    for order in orders_many:
        user = order['user']
        item = order['item']

        if user not in result:
            result[user]=[]

        result[user].append(item)
    return result

orders = [
    {'user': '민수', 'item': '노트북'},
    {'user': '지연', 'item': '마우스'},
    {'user': '민수', 'item': '키보드'},
    {'user': '영희', 'item': '모니터'},
    {'user': '지연', 'item': '스피커'}
]
print(categorize_order(orders))