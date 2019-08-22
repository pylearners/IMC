# IMC
nome = str(input('Digite seu nome: '))
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/(altura ** 2) 
if (imc<17):
    print("seu IMC é {:.2f} e Você está muito abaixo do peso!".format(imc))

elif (imc>17 and imc<=18.5):
    print("seu IMC é {:.2f} e  Você está abaixo do peso!".format(imc))

elif (imc>18.5 and imc<=25.0):
    print("seu IMC é {:.2f} e  Você está dentro da faixa de peso considerada normal pelo IMC!".format(imc))

elif (imc>25.0 and imc<=30):
    print("seu IMC é {:.2f} e  Você está acima do peso!".format(imc))

else: 
    print("seu IMC é {:.2f} e  Você está obeso!".format(imc)))
    
    
# EXEMPLO
Digite seu nome: mari
Digite seu peso: 62
Digite sua altura: 1.53
seu IMC é 26.49 e  Você está acima do peso!
