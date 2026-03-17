PrimeiroLado = int(input("Digite o primeiro lad do quadrado: "))
SegundoLado = int(input("Digite o segundo lado do quadrado: "))
TerceiroLado = float(input("Digite o terceiro lado do quadrado: "))

if (PrimeiroLado + SegundoLado > TerceiroLado) and (PrimeiroLado + TerceiroLado > SegundoLado) and (SegundoLado + TerceiroLado > PrimeiroLado):
    print("Os lados formam um TRIÂNGULO.")


if PrimeiroLado == SegundoLado == TerceiroLado:
    print("Triângulo Equilátero: três lados iguais")

elif PrimeiroLado == SegundoLado or PrimeiroLado == TerceiroLado or SegundoLado == TerceiroLado:
    print("Triângulo Isósceles: quaisquer dois lados iguais")

else:
        print("Tipo: Escaleno (todos os lados diferentes)")
