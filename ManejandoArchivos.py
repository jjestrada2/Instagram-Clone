def read():
    numbers=[]
    with open("./Archivos/Archivo.txt","r") as f:
       for line in f:
           numbers.append(int(line))
    print(numbers)

def write():
    names=["Juan","Estevan","Adrian","Roger","Robert"]
    with open("./Archivos/names.txt","w") as f:
        for name in names:
            f.write(name)
            f.write('\n')
        

def run():
    read()
    write()


if __name__ == '__main__':
    run()