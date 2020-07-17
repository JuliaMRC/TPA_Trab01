
def decimalToBinary(n):  
    return bin(n).replace("0b", "")

def rbn(number):
    
    binary = decimalToBinary(number)

    binaryReverse = binary[::-1]

    print(int(binaryReverse,2))


number = int(input())

rbn(number)