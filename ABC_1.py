

entradaNum = list(map(int, input().split()))

entradaNum.sort()

entradaLet = input()

if (entradaLet == 'ABC'):
    print(entradaNum[0], entradaNum[1], entradaNum[2])

elif (entradaLet == 'ACB'):
    print(entradaNum[0], entradaNum[2], entradaNum[1])

elif (entradaLet == 'BAC'):
    print(entradaNum[1], entradaNum[0], entradaNum[2])

elif (entradaLet == 'BCA'):
    print(entradaNum[1], entradaNum[2], entradaNum[0])

elif (entradaLet == 'CAB'):
    print(entradaNum[2], entradaNum[0], entradaNum[1])

elif (entradaLet == 'CBA'):
    print(entradaNum[2], entradaNum[1], entradaNum[0])
