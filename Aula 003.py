# #Verifica qual número é o maior entre 3 variaveis nomeadas de v1 - v2 -v3
# v1 = int(input('Primeiro Valor: '))
# v2 = int(input('Segundo Valor: '))
# v3 = int(input('Terceiro Valor: '))
# if v1 > v2 and v1 > v3:
#     print('O maior número é {}'.format(v1))
# elif v2 > v1 and v2 > v3:
#     print('O maior número é {}'.format(v2))
# else:
#     print('O maior número é {}'.format(v3))
# print('Final do programa')

# #Verifica se o número é impar ou pá.
# v1 = int(input('Entre com o 1° valor: '))
# v2 = int(input('Entre com o 2° valor: '))
# resto_v1 = v1 % 2
# resto_v2 = v2 % 2
# if resto_v1 == 0 or resto_v2 == 0: #Também pode colocar "or not resto_v2 > 0 - também irá funcionar, or not funciona para validar se a informação é verdadeira ou não.
#     print('Um número par foi informado.')
# else:
#     print('Nenhum número informado é par.')

# Simples Calculadora de Média de nota.
nota1 = int(input('Nota 1° Bimestre: '))
if nota1 > 10:
    nota1 = int(input('Nota digitada errada, tente novamente: '))
nota2 = int(input('Nota 2° Bimestre: '))
if nota2 > 10:
    nota2 = int(input('Nota digitada errada, tente novamente: '))
nota3 = int(input('Nota 3° Bimestre: '))
if nota3 > 10:
    nota3 = int(input('Nota digitada errada, tente novamente: '))
nota4 = int(input('Nota 4° Bimestre: '))
if nota4 > 10:
    nota4 = int(input('Nota digitada errada, tente novamente: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
print('A Média é: {}'.format(media))
if media < 7.0:
    print('O Aluno está com a média baixa.')
else:
    print('O Aluno está aprovado por média.')