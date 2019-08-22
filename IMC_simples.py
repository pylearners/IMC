altura = 1.48
peso = 42.0
imc = peso/ (altura**2)
print (imc)
print ("Muito abaixo do peso?", imc < 17.0)
print ("Abaixo do peso normal?", imc >= 17.0 and imc <= 18.5)
print ("Peso dentro do Normal?", imc > 18.5 and imc <= 25.0)
print ("Acima do peso normal?", imc > 25.0 and imc <= 30.0)
print ("Muito acima do peso?", imc > 30.0)
