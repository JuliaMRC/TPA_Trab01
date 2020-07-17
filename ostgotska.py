def countAE(arrayString, substring):

    cont = 0

    for item in arrayString:

        if (item.count(substring) > 0):
            cont += 1

    return cont

substring = 'ae'
string = input()

arrayString = string.split(' ')

if((countAE(arrayString, substring) * 100)/len(arrayString) >= 40.0):
    print('dae ae ju traeligt va')
else:
    print('haer talar vi rikssvenska')