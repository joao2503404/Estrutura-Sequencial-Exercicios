PrimeiroInteiro = int(input("coloque o primeiro numero inteiro: "))
SegundoInteiro = int(input("coloque o segundo numero inteiro: "))
NumeroReal = float(input("Digite um numero real: "))

Metadevalor = (PrimeiroInteiro * 2) * (SegundoInteiro / 2)
Somadotriplo = (PrimeiroInteiro * 3) + NumeroReal
ElevadoCubo = NumeroReal ** 3

primerioValor = (PrimeiroInteiro * 2) / Metadevalor + Somadotriplo + ElevadoCubo


print("Resultado A:", Metadevalor)
print("Resultado B:", Somadotriplo)
print("Resultado C:", ElevadoCubo)
