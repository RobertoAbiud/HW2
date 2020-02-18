import random
from operator import itemgetter

def start():
    opcion_seguir = True
    while opcion_seguir == True:
        while opcion_seguir == True:
            try:
                create_read = int(input("\n1.- Create a new file \n2.- Read an existing file\n3.-Random file name\n What action do you want to do?: "))
                opcion_seguir = False
            except:
                print("\nPlease select any of the options")
        
        opcion_seguir = True
        if create_read == 1:
            file_name = input("Name of the new file?: ")
            instancias(file_name)
            opcion_seguir = False
        elif create_read == 2:
            file_name = ""
            opcion_seguir = False
        elif create_read == 3:
            file_name = "numbers"
            instancias(file_name)
            opcion_seguir = False
        else:
            print("\nPlease select any of the options")
    return file_name

# A function that creates the instances
def instancias(file_name):
    valid = False
    valid2 = False
    while valid == False:
        while valid2 == False:
            n = float(input("\nHow many items?: "))
            if n <= 0 or n - int(n) != 0:
                print("\nThe number of items must be a positive and integer value")
                break
            
            lv = float(input("Lowest value: "))
            hv = float(input("Highest value: "))
            if lv <= 0 or lv - int(lv) != 0 or lv <= 0 or lv - int(lv) != 0 or hv <= 0 or hv - int(hv) != 0 or lv>hv:
                print("The lowest value must be lower than the highest value")
                break
            
            lw = float(input("Lowest weight: "))
            hw = float(input("Highest weight: "))
            if lw <= 0 or lw - int(lw) != 0 or hw <= 0 or hw - int(hw) != 0 or lw>hw:
                print("The lowest weight must be lower than the highest weight")
                break
            else:
                valid = True
                valid2= True
    n = int(n); lv = int(lv); hv = int(hv); lw = int(lw); hw = int(hw)
    if n >= 100000:
        print("Loading...")
    v = []; w = []

    v = crear_aleatorio(n, lv, hv, v)
    w = crear_aleatorio(n, lw, hw, w)

    crear_archivo(n,v,w,file_name,lw,hw)

# A function that creates a list with random numbers
def crear_aleatorio(n, menor, mayor, vector):
    for i in range(n):
        vector.append(random.randint(menor,mayor))
    
    return vector
        
# A function that creates a file
def crear_archivo(n,v,w,file_name,lw,hw):
    archivo = open(file_name+".txt","w")
    archivo.write('%s'%n+" "+'%s'%((n*((lw+hw/2)*(0.3))))+"\n")
    for i in range(n):
        archivo.write(('%s'%(i+1)) + " " + '%s'%v[i] + " " + '%s'%w[i] + "\n")
    archivo.close()

# A function that reads the file
def read_file(file_name):
    opcion_seguir = True
    while opcion_seguir == True:
        try:
            if file_name == "":
                file_name = input("\nWhat is the name of the existing file?: ")
            numbers = []; weights = []; ratio = []
            archivo = open(file_name+".txt","r")
            lines = archivo.readlines()[1:]
            for line in lines:
                line = line.split()
                line = [int(x) for x in line]
                ratio = line[1] / line[2]
                line.append(ratio)
                weights.append(line[2])
                numbers.append(tuple(line))
            instances = len(numbers)
            W = instances*((min(weights)+max(weights))/2)*(0.3)
            opcion_seguir = False
            return numbers, W
        except IOError:
            salir = False
            while salir == False:
                opc = int(input("\nError: The file does not exists\n1.- Yes\n2.- No (Close program)\nDo you want to try again with another name?: "))
                if opc == 1:
                    opcion_seguir = True
                    salir = True
                    file_name = ""
                elif opc == 2:
                    opcion_seguir = False
                    salir = True
                else:
                    print("\nPlease select any of the options")

# A function that do the heuristic by value
def heuristic_1(numbers,V,W,show):
    index = []
    numbers = sorted(numbers, key=itemgetter(1), reverse=True)
    for i in range(len(numbers)):
        if numbers[i][2] <= W:
            V += numbers[i][1]
            index.append(numbers[i][0])
            W -= numbers[i][2]
        else:
            break
    print("\nV by value = ",V, "\n")
    if show == 'y':
        print("Items in the knapsack by value: ",index )

# A function that do the heuristic by weight
def heuristic_2(numbers,V,W,show):
    index = []
    numbers = sorted(numbers, key=itemgetter(2))
    for i in range(len(numbers)):
        if numbers[i][2] <= W:
            V += numbers[i][1]
            index.append(numbers[i][0])
            W -= numbers[i][2]
        else:
            break
    print("\nV by weight = ",V, "\n")
    if show == 'y':
        print("Items in the knapsack by weight: ",index )

# A function that do the heuristic by ratio
def heuristic_3(numbers,V,W,show):
    index = []
    numbers = sorted(numbers, key=itemgetter(3), reverse=True)
    for i in range(len(numbers)):
        if numbers[i][2] <= W:
            V += numbers[i][1]
            index.append(numbers[i][0])
            W -= numbers[i][2]
        else:
            break
    print("\nV by ratio = ",V, "\n")
    if show == 'y':
        print("Items in the knapsack by ratio: ",index )

def ciclo():
    opcion_salir = True
    while opcion_salir == True:
        salir = int(input(("====Do you want to perform some heuristics again?==== \n 1.- Yes \n 2.- No \n A: ")))
        if(salir == 1):
            opcion_seguir = True
            opcion_salir = False
        elif salir == 2:
            opcion_seguir = False
            opcion_salir = False
        else:
            opcion_salir = True
            print("\nPlease select any of the options")
    print("\n")
    return opcion_seguir

file_name = start()
numbers, W = read_file(file_name) 

V = 0
opcion_seguir = True

# Heuristics
while opcion_seguir == True:
    opcion = int(input("\n 1.-By value \n 2.- By weight \n 3.- By ratio \n 4.- Show the 3 heuristics \n Which heuristic?: "))
    show = input("Show items in the knapsack? (y/n): ")
    if opcion == 1:
        heuristic_1(numbers,V,W,show)
        
    elif opcion == 2:
        heuristic_2(numbers,V,W,show)

    elif opcion == 3:
        heuristic_3(numbers,V,W,show)

    elif opcion == 4:
        heuristic_1(numbers,V,W,show)
        heuristic_2(numbers,V,W,show)
        heuristic_3(numbers,V,W,show)
    else:
        print("\nDid not select any opcion")
    
    opcion_seguir = ciclo()