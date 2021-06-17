menu= int(input("""Menu:
1------ Peso colombianos
2-------Pesos Argwntinos
3-------Pesos Mexicanos"""))

if menu==1:

    pesos = input("ingrese la cantidad de pesos colombianos")
    pesos = float(pesos)
    valor_dolar= 3875
    dolares=pesos/valor_dolar
    dolares= str(dolares)
    print("Tienes : "+dolares +"dolares")

elif menu==2 :
    
    pesos = input("ingrese la cantidad de pesos colombianos")
    pesos = float(pesos)
    valor_dolar= 3875
    dolares=pesos/valor_dolar
    dolares= str(dolares)
    print("Tienes : "+dolares +"dolares")
elif menu==3 :
    
    pesos = input("ingrese la cantidad de pesos colombianos")
    pesos = float(pesos)
    valor_dolar= 3875
    dolares=pesos/valor_dolar
    dolares= str(dolares)
    print("Tienes : "+dolares +"dolares")
else :
    print("ingrese un numero valido perra")