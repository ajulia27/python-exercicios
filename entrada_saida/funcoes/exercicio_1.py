def CalcularMedia(nota1,nota2,nota3,nota4):
    media = (nota1+nota2+nota3+nota4)/4
    return media

print('Calculadora de media')
n1 = float(input('digite a 1 nota: '))
n2 = float(input('digite a 2 nota: '))
n3 = float(input('digite a 3 nota: '))
n4 = float(input('digite a 4 nota: '))
m = calcularMedia(n1,n2,n3,n4)
print(f"sua media é {m}")