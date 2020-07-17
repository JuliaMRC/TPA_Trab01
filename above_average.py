def average(sum, qtd):
    return sum/qtd


def countAboveAverage(media, notas):
    aboveAverage = 0
    for i in range(len(notas)):
        if int(notas[i]) > media:
            aboveAverage += 1

    return aboveAverage

def toPercent(qtdPessoas, qtdAcimaMedia):
    return (qtdAcimaMedia * 100)/qtdPessoas


cases = int(input())

for _ in range(cases):

    soma = 0
    entrada = (input().split())
    qtdPessoas = int(entrada[0])
    notas = entrada[1:]

    for i in range (len(notas)):
        soma += int(notas[i])

    media = average(soma, qtdPessoas)
    acimaMedia = countAboveAverage(media, notas)

    print("{:.3f}%".format(toPercent(qtdPessoas, acimaMedia)))





    


