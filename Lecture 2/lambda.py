people=[
   {"name":"Harry","house":"Gryffindor"},
   {"name":"Cho","house":"Ravenclaw"},
   {"name":"Draco","house":"Slytherin"}
]

# def f(person):
#     return person["name"] #can also be searched depending on house

people.sort(key = lambda person : person["name"])#can also be searched depending on house

print(people)