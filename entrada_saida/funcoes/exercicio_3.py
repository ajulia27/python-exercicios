def CalcularMedia(nota1,nota2,nota3,nota4):
    media = (nota[1]+nota[2]+nota[3]+nota[4])/4
    return media

def resultado(media):
    if (media >= 5):
        return 'Aprovado'
    else:
        return 'Reprovado'
    
print('Calculadora de media')

aluno_notas = []
aluno_notas.append(input("digite o nome do aluno: "))

for in range(4):
    nota = fload(input(f"digite a (1+1) nota: "))
aluno_notas.append(nota)

m = calcularMedia(aluno_notas)
r = resultado(m)
print(f"{aluno_notas[0]} sua media é {m}, e voce foi {r}")