'''Implemente um sistema para cadastro de Pets, com as opções Inserir, Excluir, Listar Todos. Utilize um 
arquivo JSON para armazenar as informações. O arquivo JSON deve ter a estrutura abaixo e conforme as 
operações realizadas, o arquivo deve ser modificado.'''

import os
import json

def inserir():
    try:
        if os.path.exists('pet.json'):          # verifica se o arquivo ja existe
            with open('pets.json','r',encoding='utf-8') as arquivo:
                lista_pets = json.load(arquivo)


        else:
            lista_pets = []


        nome = input('Nome do PET: ')
        tipo = input('Tipo do PET: ')
        idade = int(input('Idade do PET: '))
        pet = {'tipo':tipo,
                'nome':nome,
                'idade': idade}
        
        lista_pets.append(pet)
        

        # gera o arquivo json
        with open('pets.json','w',encoding='utf-8') as arquivo:
            json.dump(lista_pets, arquivo, indent=4, ensure_ascii=False)
            print('PET cadastrado com sucesso')
    except FileExistsError:
        print('ERRO: Arquivo não localizado')
    except ValueError:
        print('ERRO: a idade deve ser um número inteiro')


def listar():
    try:
        if os.path.exists('pets.json'):
            with open('pets.json','w',encoding='utf-8') as arquivo:
                lista_pets = json.load(arquivo)
                if len(lista_pets) == 0:
                    print('Não há PETS cadastrados')
                else:
                    for pet in lista_pets:
                        print('-----------')
                        print(f'Nome: {pet["nome"]}')
                        print(f'Tipo: {pet["tipo"]}')
                        print(f'Idade: {pet["idade"]}')
        else:
            print('Não há PETS cadastrados')
    except FileExistsError:
        print('ERRO: Arquivo não localizado')

def excluir():
    try:
        if os.path.exists('pets.json'):
            with open('pets.json','w',encoding='utf-8') as arquivo:
                lista_pets = json.load(arquivo)
        else:
            lista_pets = []

        if len(lista_pets) == 0:
            print('Não há PETS cadastrados')
        else:
            nome = input('Informe  n ome do PET que será excluido: ')
            for pet in lista_pets:
                if pet['nome'] == nome:
                    lista_pets.remove(pet)
                    achou = True
                    break

            if achou == False:
                print(f'O pet de nome {nome} não está cadastrada')
            else:
                with open('pets.json','w',encoding='utf-8') as arquivo:
                    json.dump(lista_pets, arquivo, indent=4, ensure_ascii=False)
                print('PET excluido com sucesso')

    except FileExistsError:
        print('ERRO: Arquivo não localizado')
    

while True:
    print('1 - Inserir')
    print('2 - Excluir')
    print('3 - Listar Todos')
    print('4 - Sair')
    opcao = int(input('Escolha uma opção: '))
    match opcao:
        case 1:
            inserir()
        case 2:
            excluir()
        case 3:
            listar()
        case 4:
            print('Fim do programa')
            break
        case _:
            print('Opção inválida')



