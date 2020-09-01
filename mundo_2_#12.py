#Aula 12
    #Condição Aninhada

nome = str(input('Olá, qual é o seu nome? '))
print ('Seja Bem-Vindo {}!'.format(nome))
nota1 = int(input('{}, Qual foi 1º nota da sua Ac1? '.format(nome)))
nota2 = int(input('E da Ac2? '))
nota3 = int(input('E da Ac3? '))
nota4 = int(input('E da Ac4? '))
resultado = ((nota1 + nota2 + nota3 + nota4) / 4) * 0.5

if resultado >= 4:
    print('A soma deu {}, Parabéns {}, você passou no semestre !'.format(resultado, nome))
else:
    print('A Soma deu {}, Você foi reprovado {}, estude mais.'.format(resultado, nome))