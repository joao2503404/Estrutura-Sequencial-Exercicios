mensagem = "converta Celsius em Fahrenheit"
print(mensagem.center(50, "-"))

ValorCelsius = float(input("Digite o valor: "))

ValorFahrenheit = (ValorCelsius * 9 / 5) + 32 

print(f"Valor em Celsius {ValorFahrenheit}")
