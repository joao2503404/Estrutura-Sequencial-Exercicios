valor_da_hora = float(input("Quanto você ganha por hora? "))
horas_no_mes = float(input("Quantas horas você trabalhou? "))

salario_bruto = valor_da_hora * horas_no_mes

if salario_bruto <= 900:
    porcentagem_ir = 0
elif salario_bruto <= 1500:
    porcentagem_ir = 5
elif salario_bruto <= 2500:
    porcentagem_ir = 10
else:
    porcentagem_ir = 20

desconto_ir = salario_bruto * (porcentagem_ir / 100)
desconto_inss = salario_bruto * 0.10
desconto_sindicato = salario_bruto * 0.03
valor_fgts = salario_bruto * 0.11

total_descontos = desconto_ir + desconto_inss + desconto_sindicato
salario_liquido = salario_bruto - total_descontos

print("Salário Bruto: R$", salario_bruto)
print("IR (", porcentagem_ir, "%): R$", desconto_ir)
print("INSS (10%): R$", desconto_inss)
print("Sindicato (3%): R$", desconto_sindicato)
print("FGTS (11%): R$", valor_fgts)
print("Total de descontos: R$", total_descontos)
print("Salário Liquido: R$", salario_liquido)