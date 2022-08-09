#Na prática

#Fase 1: Dados conhecidos ou entrada de dados

#Média mínima para ser aprovado
aprovacao = 7.0

#Média mínima para ficar para exame
exame = 6.0

#Quantidades de bimestres no ano
bimestres = 4

#Nome do aluno
nome = "Pedro Henrique"

#Lista de notas durante o ano - uma por bimestre
notas = [7.8, 8.5, 5.9, 8.1]

#Mensagem para ser mostrada ao final da execução
mensagem = ''

#Fase 2: Processamento dos dados

#Instrução de repetição para somar todas as notas do ano
soma = 0
for nota in notas:
    soma += nota

#Cálculo da média anual
media = soma / bimestres

#Instrução de decisão para adicionar texto na variável "mensagem"
if media >= aprovacao:
    mensagem = 'Aprovado'
elif media >= exame:
    mensagem = 'Exame'
else: 
    mensagem = 'Reprovado'

#Fase 3: Saída de informação
print("Nome: %s" % nome)
print("Média anual: %8.2f" % media)
print("Status: %s" % mensagem)