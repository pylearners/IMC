print("Olá!")

peso = float (input("Digite o seu peso: "))
altura = float (input("Digite sua altura: "))

imc = (peso/(altura**2))

print("O seu IMC é: ", imc)

if (imc<17):
    print("Você está muito abaixo do peso!")

elif (imc>17 and imc<18.5):
    print("Você está abaixo do peso!")

elif (imc>18.5 and imc<25.0):
    print("Você está dentro da faixa de peso considerada normal pelo IMC!")

elif (imc>25.0 and imc<30):
    print("Você está acima do peso!")

else: 
    print("Você está obeso!")

print("FIM!")
