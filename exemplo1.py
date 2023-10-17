# gera um arquivo JSON a partir de um dicionario python

import json

dicionario1 = {'codigo': 123, 'nome': 'Luana Cabezaolias', 'idade': 18, 'altura': 1.60, 'notas': [9, 8, 8.5, 9.8]}

dicionario2 = {'codigo': 456, 'nome': 'Camila Padalino', 'idade': 17, 'altura': 1.73, 'notas': [9, 8.1, 7.9, 9.8]}

lista = [ dicionario1, dicionario2]
with open('dados.json', 'w') as arquivo:
    json.dump(lista, arquivo, indent=4, sort_keys=True)

