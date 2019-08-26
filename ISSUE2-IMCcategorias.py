print("Olá!")

peso = 60
altura = 1.70**2 

imc = (peso/altura)

print("O resultado do IMC com os dados sugeridos é: ", imc)

print ("Muito abaixo do peso?", imc < 17.0)
print ("Abaixo do peso normal?", imc >= 17.0 and imc <= 18.5)
print ("Peso dentro do Normal?", imc > 18.5 and imc <= 25.0)
print ("Acima do peso normal?", imc > 25.0 and imc <= 30.0)
print ("Muito acima do peso?", imc > 30.0)

print("Obrigado. Volte sempre!")
