
def verifAH(jon, doctor):
    if len(jon) < len(doctor):
        return False
    else:
        return True


jon = input()
doctor = input()

if(verifAH(jon, doctor)):
    print("go")
else:
    print("no")



