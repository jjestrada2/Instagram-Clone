import random

def juego():
    
    banco_palabras=["CARRO,","MANZANA","CHOCOLATE","CASA","IMPRESORA","CAMA","ARDILLA"]
    palabra="CARRO"#banco_palabras[random.randrange(0,len(banco_palabras))]
    num_palabras=len(palabra)
    i=0
    while i<=num_palabras:
        print("___")
        i=i+1
    letra_jugador=input(str("ingresa una Letra "+"\n"))

    respuesta=[]
    contador=0
    for letra in palabra:
        if letra==letra_jugador:
            respuesta[contador]= letra_jugador
        else:
            print("_")
        contador=contador+1    
        print(respuesta)        
     

    
def run():
 
  juego()

if __name__=="__main__":
    run()