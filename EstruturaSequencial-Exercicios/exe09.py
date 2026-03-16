mensagem = "converta Fahrenheit para Celsius."
print(mensagem.center(50, "-"))

ValorFahrenheit = float(input("Digite o valor: "))

ValorCelsius = (ValorFahrenheit - 32) * 5 / 9 

print(f"Valor em Celsius {ValorCelsius}")

