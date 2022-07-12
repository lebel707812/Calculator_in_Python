print('\n********************* CALCULADORA!!!*******************')

def soma(x, y):
	return x + y

def subtracao(x, y):
	return x - y

def divisao(x, y):
	return x / y

def multip(x, y):
	return x * y


dado = input("Selecione \n 1 para SOMA \n 2 para SUBTRAÇÃO \n 3 para DIVISÃO \n 4 para MULTIPLICAÇÃO:  ")

num1 = int(input('Digite o número 1:  '))

num2 = int(input('Digite o número 2:  '))

if dado == "1":
	print(num1, "+", num2, "=", soma(num1, num2))

elif dado == "2":
	print(num1, "-", num2, "=", subtracao(num1, num2))

elif dado == "3":
	print(num1, "/", num2, "=", divisao(num1, num2))

elif dado == "4":
	print(num1, "*", num2, "=", multip(num1, num2))

else:
	print("Operação invalída")