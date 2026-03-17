a = float(input("Digite o valor de a: "))

if a == 0:
    print("A equação não é do segundo grau. Programa encerrado.")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = (b ** 2) - (4 * a * c)
    print(f"Delta: {delta}")


    if delta < 0:
        print("A equação não possui raízes reais. Programa encerrado.")

    elif delta == 0:
        raiz = -b / (2 * a)
        print(f"A equação possui apenas uma raiz real: {raiz}")
    
    else:
        raiz_delta = delta ** 0.5
        
        x1 = (-b + raiz_delta) / (2 * a)
        x2 = (-b - raiz_delta) / (2 * a)
        
        print(f"A equação possui duas raízes reais:")
        print(f"Raiz 1 (x'): {x1}")
        print(f"Raiz 2 (x''): {x2}")