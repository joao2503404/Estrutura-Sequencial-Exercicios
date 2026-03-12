nota = float(input("digite a primeira nota do aluno: "))
nota1 = float(input("digite a segunda nota do aluno: "))

media = (nota + nota1) / 2

if media >= 7:
    print("Aprovado")
elif media == 10:
    print("Aprovado com Distinção")
else:    
    print("Reprovado")

