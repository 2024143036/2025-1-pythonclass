#다차원  리스트

colors=['red', 'blue', 'green']
cities=['서울', '부산', '인천', '의정부', '대전', '강릉', '논산', '포항']
combi = [colors, cities]
print(combi)
print(combi[1][2])
bigcombi=[combi,[0,2,7]]
print(bigcombi)
print(len(bigcombi))
print(bigcombi[0][1][2])
print(bigcombi[1][1])

#퀴즈
first=["egg", "salad", "bread", "soup", "coffee"]
second=["fish", "lamb", "pork", "beef", "chicken"]
third=["apple", "ban", "오렌지", "포도", "망고"]

order=[first, second, third]
john=[order[0][-2], second[1::3], third[0]]
print(john)
del john[2]
john.extend(([order[2][0:1]]))
print(john)

