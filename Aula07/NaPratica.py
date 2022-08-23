nome=input("Digite seu nome:")
idade=input("Digite sua idade:")

idade = 18
if idade >=18:
    print("Maior de idade")
else:
    print("Menor de idade")
    print("Não é permitida a sua inscrição")

sexo=str(input('Digite (F)-Feminino, (M)-Masculino:').upper())

if sexo =='M':
    print('Sexo Masculino.')
    print("Número CAM:")
elif sexo == 'F':
    print('Sexo Inválido.')