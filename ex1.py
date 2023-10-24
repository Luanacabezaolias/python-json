'''Considere que o arquivo “notas.CSV” apresenta uma listagem com os dados dos alunos de uma turma. 
Cada linha do arquivo apresenta os dados de um aluno, no formato:
RM,NOME,NOTA1,NOTA2,NOTA3,NOTA4
Implemente um programa que leia este arquivo e gere um novo arquivo JSON no formato:'''

import json
with open('notas.csv', 'r', encoding='utf-8') as arquivo:

    alunos = {}
    conta_linha = 1
    for linha in arquivo:
        if conta_linha > 1:     # ignora a primeira linha do arquivo csv
            lista = linha.split(';')
            print(lista)

            rm = lista[0]
            nome = lista[1]
            notas = [float(lista[2]),float(lista[3]),float(lista[4]),float(lista[5])]
            alunos[rm] = { 'nomes': nome, 'notas': notas}   #insere no dicionario
        conta_linha += 1

print(alunos)

with open('notas.json', 'w', encoding='utf-8') as arquivo:
    json.dump(alunos, arquivo, indent=4)

