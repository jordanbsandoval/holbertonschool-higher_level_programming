#!/usr/bin/python3
""" Probando iteraciones en python con for"""
words = ["jordan", "ronaldo", "buitrago"]
users = {'Hans': 'active', 'Éléonore': 'active', '景太郎': 'inactive'}

for i in words:
    print(f"{i}")

diccionario = {"name": "jordan", "ciudad" : "cucuta", "height" : 1.76, "estado": "inactive"}

for user, status in  diccionario.copy() .items():
    if status == "inactive":
        del diccionario[user]
    print(f"{user}: {status}")

users_actives = {}
for i, status in users.items():
    print(i)
    if status == "active":
        users_actives[i] = status

for i in users_actives:
    print(i)