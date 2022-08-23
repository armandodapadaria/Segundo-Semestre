#Na Prática, Comando Condicional If em Python
#Programa de auxílio a decisão sobre o preço de mercado

# PA e PercA, preço do 1o colocado e percentual de participação no mercado
# PB e PercB, preço do 2o colocado e percentual de participação no mercado
# PC e PercC, preço do 3o colocado e percentual de participação no mercado
# PS, preço sugerido
#DIF, a diferença de preços (margem)

PA=float(input("Preço de mercado concorrente A => "))
PercA=float(input("Participação de mercado concorrente A % => "))
PB=float(input("Preço de mercado concorrente B => "))
PercB=float(input("Participação de mercado concorrente B % => "))
PC=float(input("Preço de mercado concorrente C => "))
PercC=float(input("Participação de mercado concorrente C % => "))
PS=float(input("Preço de sugestão => "))

#Cálculo do valor médio de mercado
VMM = PA * (PercA/100) + PB*(PercB/100) + PC*(PercC/100)
print ("Valor de mercado: R$", VMM)

if PS>VMM :
    DIF = PS-VMMprint("Seu preço de venda está excessivo em relação ao mercado")
    print("Margem ultrapassa, em reais:", DIF)
    print("Entre com nova sugestão de preço")
else :
    DIF = VMM-PS
    print("PArabéns. Seu preço de venda est[a COMPETITIVO em relação ao mercado")
    print("Margem DISPONIVEL em reais:", DIF)