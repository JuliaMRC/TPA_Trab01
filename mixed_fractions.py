def mixedFractionsResolve():

    aux = input()

    aux = aux.split()

    num = int(aux[0])
    den = int(aux[1])

    while (num != 0 and den != 0):

        quo = num//den

        res = num % den

        print(quo, res, '/', den)

        aux = input()

        aux = aux.split()

        num = int(aux[0])
        den = int(aux[1])


mixedFractionsResolve()