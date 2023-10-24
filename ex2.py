'''Considere o arquivo “foods.CSV”, com três colunas, no formato abaixo, onde cada linha representa um 
indivíduo com suas respectivas informações. 
NAME,ID,FAVORITE FOOD
Implemente um programa que a partir do arquivo indicado gere um arquivo JSON no formato:

'''
import json

with open('foods.csv', 'r', encoding='utf-8') as arquivo:
    foods = {}
    conta_linha = 1
    for linha in arquivo:
        if conta_linha > 1:
            lista = linha.split(';')
            print(lista)

            id = lista[1]
            nome = lista[0]
            comida_favorita = lista[2]
            foods[id] = {'nome': nome, 'food': comida_favorita}
        conta_linha += 1
print(foods)

with open('foods.json', 'w', encoding='utf-8') as arquivo:
    json.dump(foods,arquivo, indent=4)
           

