import sys

def findSum(ent):
    
    entrada = ent

    for i in range(0, len(entrada)):
        
        testeInicio = entrada[i]
        
        entrada.remove(testeInicio)
        
        entrada.insert(0,testeInicio)
        
        
        soma = 0
        
        for j in range (1, len(entrada)):
            
            soma += entrada[j]
        
        if soma == testeInicio:
            return testeInicio

#teste = []

for line in sys.stdin:

    entrada = list(map(int, line.split()))

    print(findSum(entrada))


