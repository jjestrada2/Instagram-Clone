menu= int(input("""Menu:
1------ Peso colombianos
2-------Pesos Argwntinos
3-------Pesos Mexicanos"""))

def conversionMoneda(Moneda,ValorDeMoneda) :
    pesos = input("ingrese la cantidad de pesos "+ Moneda)
    pesos = float(pesos)
    dolares=pesos/ValorDeMoneda
    dolares= str(dolares)
    print("Tienes : "+dolares +"dolares")

if menu==1:
 conversionMoneda("Colombianos",3875)
    

elif menu==2 :
    conversionMoneda("Argentinos",65)
elif menu==3 :
    conversionMoneda("Mexicanos",35)
else :
    print("ingrese un numero valido perra")