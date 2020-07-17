def stringContains(substring, string):
    

    for i in range(len(substring)):

        if substring[i] != string[i]:
            return False

    return True

qtd = int(input())

substring = "Simon says"

for _ in range(qtd):
    string = input()
    if(stringContains(substring, string)):
        string.strip("Simon says")
        print(string[11:])

