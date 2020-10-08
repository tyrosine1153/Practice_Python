"""
lst = list(map(int, input().split()))
print(lst)
"""
books = {'123456': {"title": "집에 갈래", "year": 2020, 'price': 21600},
         '523656': {"title": "집에 갈래", "year": 2020, 'price': 19600},
         '156656': {"title": "집에 갈래", "year": 2020, 'price': 19600}
         }
for key, value in books.items():
    if value['price'] > 20000:
        print(f"ISBN: {key} 책 제목: {value['title']} 가격: {value['price']}")





