#IMC Atualizado
nome = str(input ('Qual seu nome?: '))
peso = float (input ('Qual seu peso(kg)?: '))
altura = float (input ('Qual sua altura(m)?: '))
imc = (peso/(altura*altura))
print ('Seu IMC é: {:.2f}'.format(imc))
print ('Muito abaixo do peso?', imc<17)
print ('Abaixo do peso?', imc>=17 and imc<=18.5)
print ('Peso dentro do normal?', imc>18.5 and imc<=25)
print ('Acima do peso?', imc>25 and imc<=30)
print ('Muito acima do peso?', imc>30)