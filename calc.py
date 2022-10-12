print('\n \n------------- Python Calculadora -------------\n \n')
print('Selecione o número referênte a sua operação')
print(' 1-Soma \n 2-Subtração \n 3-Divisão \n 4-Multiplicação ')
entrada = int(input())


def algoritimo():
    if entrada == 1:
        soma = lambda x, c: x + c
        soma1 = int(input('Primeiro número: '))
        soma2 = int(input('\nSegundo número: '))
        print('\n', soma1, "+", soma2, "=", soma(soma1, soma2))
    elif entrada == 2:
        subtra = lambda x, c: x - c
        subtra1 = int(input('Primeiro número: '))
        subtra2 = int(input('\nSegundo número: '))
        print('\n', subtra1, "-", subtra2, '=', subtra(subtra1, subtra2))
    elif entrada == 3:
        divi = lambda x, c: x / c
        divi1 = int(input('Primeiro número: '))
        divi2 = int(input('\nSegundo número: '))
        print('\n', divi1, '/', divi2, '=', divi(divi1, divi2))
    elif entrada == 4:
        multi = lambda x, c: x * c
        multi1 = int(input('Primeiro número: '))
        multi2 = int(input('\nSegundo número: '))
        print('\n', multi1, '*', multi2, '=', multi(multi1, multi2))
    else:
        print('Entrada Inválida')
algoritimo()

contin = input('\n \n \n Se deseja realizar outra operação, pressione ENTER \n '
                 'Se não quiser, pressione QUALQUER tecla e em seguida ENTER \n')

while (contin == ''
                 ''):
    print('Selecione o número referênte a sua operação')
    print(' 1-Soma \n 2-Subtração \n 3-Divisão \n 4-Multiplicação ')
    entrada = int(input())
    algoritimo()
    contin = input('\n \n \n Se deseja realizar outra operação, pressione ENTER \n '
                   'Se não quiser, pressione QUALQUER tecla e em seguida ENTER \n')
else:
    print('---------------- Operação Realizada ------------- \n '
          '------------- Aplicativo Encerrado -------------')

