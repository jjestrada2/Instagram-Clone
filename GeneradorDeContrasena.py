import random

def generarContrasena():
    mayusculas=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','E','S','T','Y','W','S']
    minusculas=['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
    simbolos=['!','#','$','%','&','/','?']
    numeros=[1,2,3,4,5,6,7,8,9]
    
    caracteres= mayusculas+minusculas+simbolos+numeros
    contrasena=[]


    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
        print(contrasena)
    
    return contrasena


def run():
    contrasena=generarContrasena()
    print('tu nueva contrasena es: '+contrasena)


if __name__=='__main__':
    run()