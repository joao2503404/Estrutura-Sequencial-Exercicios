num1 = float(input("Digite o valor do primeiro produto: "))
num2 = float(input("Digite o valor do segundo produto: "))
num3 = float(input("Digite o o valor do terceiro produto: "))

produtoMaisBarato = num1

if  num2 < produtoMaisBarato:
    produtoMaisBarato = num2

if num3 < produtoMaisBarato:
    produtoMaisBarato = num3

print(f"o produto mais barato esta custando {produtoMaisBarato}")
    