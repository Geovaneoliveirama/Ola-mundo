# Calculando a média alcançada por um aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media == 10:
    print(f"Média:{media: }, Aprovado com Distinção! ")
elif media >= 7:
    print(f"Média:{media: }, Aprovado! ")
else:
    print(f"Média:{media: }, Reprovado! ")