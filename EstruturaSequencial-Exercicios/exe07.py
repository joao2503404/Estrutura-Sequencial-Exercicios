mensagem = "área do quadrado"
print(mensagem.center(50, "-"))

lado = float(input("Digite o valor do lado do quadrado:"))

area = lado ** 2 
dobrando = area * 2

print(f"A area do quadrado é: {dobrando:.2f}")