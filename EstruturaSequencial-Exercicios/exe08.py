mensagem = "salario mensal"
print(mensagem.center(50, "-"))

ganho_hora = float(input("Digite o valor do ganho por hora:"))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês:"))

salario_mensal = ganho_hora * horas_trabalhadas

print(f"O salário mensal é: R${salario_mensal:.2f}")