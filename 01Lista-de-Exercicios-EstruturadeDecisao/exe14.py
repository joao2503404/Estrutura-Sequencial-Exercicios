NotaAluno1 = float(input("Digite a primeira Nota: "))
NotaAluno2 = float(input("Digite a segunda Nota: "))

MediaNota = (NotaAluno1 + NotaAluno2) / 2

if MediaNota >= 9.0:
    conceitos = "A"
    Avaliacao = "APROVADO"
elif MediaNota >= 7.5 and MediaNota < 9.00:
    conceitos = "B"
    Avaliacao = "APROVADO"
elif MediaNota >= 6.0 and MediaNota < 7.5:
    conceitos = "C"
    Avaliacao = "APROVADO"
elif MediaNota >= 4.0 and MediaNota < 6.0:
    conceitos = "D"
    Avaliacao = "REPROVADO"
elif MediaNota <= 4.0:
    conceitos = "E"
    Avaliacao = "REPROVADO"

print(f"SUAS NOTAS: {NotaAluno1}, {NotaAluno2}")
print(f"SUA MEDIA: {MediaNota}")
print(f"CONCEITOS: {conceitos}")
print(f"SITUAÇÃO: {Avaliacao}" )



