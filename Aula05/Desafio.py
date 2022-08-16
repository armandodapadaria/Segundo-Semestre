def calculo_imc(nome, x, y):

  imc = x / (y*y)
  print("O imc do paciente ",nome," é", imc)


def informacoes():
 nomePaciente = input("Digite o nome do paciente ")
 telefonePaciente = input("Digite o telefone do paciente ")
 peso = float(input("Digite o peso do paciente "))
 altura = float(input("Digite a altura do paciente "))
 calculo_imc(nomePaciente,peso,altura)


informacoes()
