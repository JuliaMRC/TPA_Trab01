
def omo(invitation_code):

    NoDuplicates = set(invitation_code)

    for item in NoDuplicates:

        if invitation_code.count(item) == 1:

            return item


aux = 0
num = int(input())

odd = []


for i in range(1, num + 1):

    num_guests = int(input())

    invitation_code = input()

    invitation_code = invitation_code.split()

    odd.append(omo(invitation_code))


for i in range(len(odd)):
    print('Case #' + str(i+1) + ':', odd[i])
  



