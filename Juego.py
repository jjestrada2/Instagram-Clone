import random

def run():
    numero_aleatorio=random.randint(1,100)
    numero_elejido=int(input('Elije un numero del 1 al 100 : '))
    while numero_aleatorio != numero_elejido :
        print(numero_aleatorio)
        if numero_elejido < numero_aleatorio:
            print('Busca un numero mayor')
        else:
            print('Busca un numero menor')
        numero_elejido=  int(input('Elije otro numero'))
        
    print('Felicitaciones Ganaste')

if __name__ =='__main__':
    run()