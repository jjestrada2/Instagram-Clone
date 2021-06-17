def palindromo(palabra):
    palabra= palabra.replace(' ','')
    print(palabra)
    palabra= palabra.lower()
    print(palabra)
    palabra_invertida= palabra[::-1]
    print(palabra_invertida)
    print(palabra)
    if palabra==palabra_invertida:
        print("LOL")
        return True
        
    else :
        return False
        


def run():
    palabra= input("escribe una palabra")
    palindromo(palabra)
    print(palindromo)
    if palindromo==True:
        print("la KLJAKLNC palbra es un palindromo")
    else:
        print("la palbra no es un palindroKLWNFNLmo")


if __name__ == '__main__':
    run()