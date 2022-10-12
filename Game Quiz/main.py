import random
import json
import os


with open('questions/perg.json', 'r') as nome:
    leitura = nome.read()
    lei = json.loads(leitura)

def perg1 (p):
    p_1 = str(p)
    p1 = 'questions/' + p_1 + '.txt'
    with open(p1, 'r') as pergunta:
        abri = pergunta.read()
        print('\n', abri)

print('Bem Vindo ao Quiz \n Responda as 10 perguntas \n')
dic = len(lei)

perguntas = random.sample(range(dic), 10)

#print(perguntas)

pontos = 0
contador = 0
fracasso = 0
while contador < 10:
        dado_resp = str(perguntas[contador])
        perg1(dado_resp)
        resp = input('\n Digite a LETRA referente a resposta correta \n')
        resp1 = resp.lower()
        if resp1 == 'a' or resp1 == 'b' or resp1 == 'c' or resp1 == 'd' or resp1 == 'e':
            if lei[dado_resp] == resp1:
                print('Boa!!! Acertou!')
                pontos = pontos + 10
                contador += 1
            else:
                print('Uia! Resposta incorreta. A alternativa correta era a letra:', str(lei[dado_resp].upper()))
                contador += 1
        else:
            print('TENTE DE NOVO')
            fracasso += 1
            if fracasso == 5:
                print('Não precisamos fazer um teste pra saber o quanto intelgiente você é. Não consegue nem seguir instruções')
                break

if contador == 10:
    print('Sua pontuação é \n', pontos)

pontos = 0

if contador == 10:
    if pontos <= 10:
        print('Cacete... Tu erro muito. Vai estuda')
    elif (pontos <= 30) and (pontos >= 9):
        print('Não chegou a ser tão mal. Mas foi bem mal.')
    elif (pontos <= 50) and (pontos >= 31):
        print("Até que foi bem hein. Mas da pra melhorar! Bora!!")
    elif (pontos <= 70) and (pontos >= 51):
        print('Opa!! Mandou bem hein.')
    elif (pontos <= 90) and (pontos >= 71):
        print('Mandou muito!! Por pouco não acertou tudo!')
    else:
        print('Você é super dotado?!?! Acertou tudo!')