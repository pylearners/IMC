nome = str(input("Qual o seu nome? "))
print("Olá, %s. Seja bem-vindo(a)!" %(nome))

peso = float (input("Digite o seu peso: "))

altura = float (input("Digite sua altura: "))

imc = (peso/(altura**2))

print("O peso informado foi: %s, e a altura informada foi: %s" %(peso, altura))
print("Portanto, o seu IMC é: ", imc)

print ("Muito abaixo do peso?", imc < 17.0)
print ("Abaixo do peso normal?", imc >= 17.0 and imc <= 18.5)
print ("Peso dentro do Normal?", imc > 18.5 and imc <= 25.0)
print ("Acima do peso normal?", imc > 25.0 and imc <= 30.0)
print ("Muito acima do peso?", imc > 30.0)

print("Obrigado! FIM! ")

