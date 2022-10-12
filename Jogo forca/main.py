import random
import os

rand = str(random.choice(range(1,5)))
with open('palavras/'+rand+ '.txt') as leia:
    conteudo= leia.read()

print('---Bem Vindo ao jogo da Forca---')

def dado():
    inputUser = input('Digite uma letra: ')
    test = inputUser in letra.values()
    if test == True:
        for k, v in letra.items():
            if v == inputUser:
                forca[k] = inputUser
    escolhas.append(inputUser)
    if test == False:
        lista.append(1)
lista = []
escolhas = []
letra = dict(enumerate(conteudo))
letra2 = list(conteudo)
forca = list(len(letra)*'-')

while sum(lista) <= 6:
    if sum(lista) == 0:
        print(' +---+\n |   | \n     | \n     |'
            '\n     | \n     | \n  ====')
        print('Palavras usadas até o momento:', ''.join(escolhas))
        print(''.join(forca))
        dado()
        testeForca = '-' in forca
    if sum(lista) == 1 and testeForca == True:
        print(' +---+\n |   |\n 0   | \n     | \n     |'
              '\n     | \n ====')
        print('Palavras usadas até o momento:', ''.join(escolhas))
        print(''.join(forca))
        dado()
        testeForca = '-' in forca
    elif sum(lista) == 2 and testeForca == True:
        print(' +---+\n |   |\n 0   |\n |   | \n     | \n     |'
              '\n  ====')
        print('Palavras usadas até o momento:', ''.join(escolhas))
        print(''.join(forca))
        dado()
        testeForca = '-' in forca
    elif sum(lista) == 3 and testeForca == True:
        print(' +---+\n |   |\n 0   |\n/|   | \n     | \n     |'
              '\n  ====')
        print('Palavras usadas até o momento:', ''.join(escolhas))
        print(''.join(forca))
        dado()
        testeForca = '-' in forca
    elif sum(lista) == 4 and testeForca == True:
        print(' +---+\n |   |\n 0   |\n/|\  | \n     | \n     |'
              '\n  ====')
        print('Palavras usadas até o momento:', ''.join(escolhas))
        print(''.join(forca))
        dado()
        testeForca = '-' in forca
    elif sum(lista) == 5 and testeForca == True:
        print(' +---+\n |   |\n 0   |\n/|\  | \n/    | \n     | '
              '\n  ====')
        print('Palavras usadas até o momento:', ''.join(escolhas))
        print(''.join(forca))
        dado()
        testeForca = '-' in forca
    elif sum(lista) == 6:
        print(' +---+\n |   |\n 0   |\n/|\  | \n/ \  | \n     | '
              '\n  ====')
        print(''.join(forca))
        print('Palavras usadas :', ''.join(escolhas))
        print('FIM DE JOGO \nMAIS SORTE NA PRÓXIMA')
        print('A palavra é: ', conteudo)
        break
    elif testeForca == False:
        print('Você venceu!! Parabéns!!')
        print('Palavras usadas :', ''.join(escolhas))
        print('A palavra é: ', conteudo)
        break
