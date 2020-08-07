from random import shuffle

#Apresentação
print('----BEM VINDO AO RANDOMIFICADOR----\n\n')
#Entrada de dados
nome1 = input('Digite o nome do aluno 1: ')
nome2 = input('Digite o nome do aluno 2: ')
nome3 = input('Digite o nome do aluno 3: ')
nome4 = input('Digite o nome do aluno 4: ')
#Fim
#Lista a ser embaralhada
nomes = [nome1, nome2, nome3, nome4]
#Fim
print('\n')
#Saída de dados
print('Agora vou sortear a ordem de apresentação\n\n')

shuffle(nomes)

print('Então a ordem de apresentação será essa:\n')

print(nomes)

print('\n')
print('\n')
print('---coded by > Lucas Silva---')
print('\n')
