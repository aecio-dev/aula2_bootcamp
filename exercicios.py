import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

#numero_01 = int(input("Inserir um numero inteiro: "))
#numero_02 = int(input("Inserir outro numero inteiro: "))
#resultado = numero_01 + numero_02
#print(resultado)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

#numero = int(input("Digite um número: "))
#resto = numero % 5
#print(f"O resto da divisão de {numero} por 5 é {resto}.")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

#numero_01 = int(input("Inserir um numero inteiro: "))
#numero_02 = int(input("Inserir outro numero inteiro: "))
#resultado = numero_01 * numero_02
#print(resultado)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

#numero_01 = int(input("Inserir um numero inteiro: "))
#numero_02 = int(input("Inserir outro numero inteiro: "))
#resultado = numero_01 // numero_02
#print(resultado)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

#raio_circulo = float(input("Digite o raio: "))
#area_circulo = math.pi * raio_circulo ** 2
#print(f"{area_circulo:.2f}")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

#numero_01 = float(input("Inserir um numero flutuante: "))
#numero_02 = float(input("Inserir outro numero flutuante: "))
#resultado = numero_01 + numero_02
#print(resultado)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

#numero_01 = float(input("Inserir um numero flutuante: "))
#numero_02 = float(input("Inserir outro numero flutuante: "))
#media = (numero_01 + numero_02) / 2
#print(f"A média dos números {numero_01} e {numero_02} é {media:.2f}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

# def calcular_potencia(base, expoente):
#     resultado = base ** expoente
#     return resultado
# base = int(input("Digite a base: "))
# expoente = int(input("Digite o expoente: "))
# resultado_final = calcular_potencia(base, expoente)
# print(f"{base} elevado a {expoente} é igual a {resultado_final}")


# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# celsius = float(input("Digite a temperatura em Celsius: "))
# fahrenheit = (celsius * 9/5) + 32

# print(f"{celsius}°C é igual a {fahrenheit}°F")


# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

#raio_do_circulo = float(input("Digite o raio: "))
#area_do_circulo = math.pi * raio_do_circulo ** 2
# area_do_circulo_formatada = "{:.2f}".format(area_do_circulo)
#print(f"{area_do_circulo:.2f}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

# texto = input("Digite um texto: ")

# texto_maiusculas = texto.upper()
# print("Texto em maiúsculas:", texto_maiusculas)


# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

# nome_completo = input("Digite seu nome completo: ")

# nome_minusculas = nome_completo.lower()
# print("Nome em minúsculas:", nome_minusculas)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

# frase = input("Digite uma frase: ")

# frase_sem_espacos = frase.strip()
# print("Frase sem espaços no início e no final:", frase_sem_espacos)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

# data_do_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
# lista_de_dia_mes_ano = data_do_usuario.split("/")
# print(f"O elemento 1 e o: {lista_de_dia_mes_ano[0]}")
# print(f"O elemento 2 e o: {lista_de_dia_mes_ano[1]}")
# print(f"O elemento 3 e o: {lista_de_dia_mes_ano[2]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# parte1 = input("Digite a primeira parte do texto: ")
# parte2 = input("Digite a segunda parte do texto: ")

# texto_concatenado = parte1 + parte2
# print("Texto concatenado:", texto_concatenado)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# expressao1 = input("Digite a primeira expressão (True ou False): ").lower()
# expressao2 = input("Digite a segunda expressão (True ou False): ").lower()

# valor1 = expressao1 == "true"
# valor2 = expressao2 == "true"

# resultado = valor1 and valor2

# print(f"O resultado da operação AND entre {expressao1} e {expressao2} é: {resultado}")


# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

# expressao1 = input("Digite a primeira expressão (True ou False): ").lower()
# expressao2 = input("Digite a segunda expressão (True ou False): ").lower()

# valor1 = expressao1 == "true"
# valor2 = expressao2 == "true"

# resultado_or = valor1 or valor2

# print(f"O resultado da operação OR entre {expressao1} e {expressao2} é: {resultado_or}")

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

# valor_booleano = input("Digite um valor booleano (True ou False): ")

# if valor_booleano.lower() == "true":
#      valor_invertido = False
# elif valor_booleano.lower() == "false":
#     valor_invertido = True
# else:
#     print("Valor inválido! Certifique-se de digitar 'True' ou 'False'.")

# print(f"O valor invertido é: {valor_invertido}")


# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

numero_01 = int(input("Inserir um numero: "))
numero_02 = int(input("Inserir outro numero: "))

if numero_01 == numero_02:
    print("Os números são iguais!")
else:
    print("Os números são diferentes.")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação