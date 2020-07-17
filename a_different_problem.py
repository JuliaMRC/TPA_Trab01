import sys

for line in sys.stdin:

    entrada = line.split()

    num1 = int(entrada[0])
    num2 = int(entrada[1])

    print(abs(num1-num2))
