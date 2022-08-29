import json as j


with open("funcionarios.json", encoding='utf-8') as funcionarios:
    funcionarios = j.load(funcionarios)

for f in funcionarios:
    if(f['user_id'] == 1336237735):
        funcionario = f['nome'].lower()


print(funcionario)
