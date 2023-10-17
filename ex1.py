'''Considere que o arquivo “notas.CSV” apresenta uma listagem com os dados dos alunos de uma turma. 
Cada linha do arquivo apresenta os dados de um aluno, no formato:
RM,NOME,NOTA1,NOTA2,NOTA3,NOTA4
Implemente um programa que leia este arquivo e gere um novo arquivo JSON no formato:'''

with open('notas.csv', 'r') as arquivo:
    for linha in arquivo
