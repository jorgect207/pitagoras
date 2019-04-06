from math import sqrt

i=1
while i==1:
    print("TEOREMA DE PITAGORAS\n")
    print("PARA HALLAR HIPOTENUSA ----> 1\n")
    print("PARA HALLAR CATETO ---> 2\n")
    deseo = int(input("R:"))
    if deseo == 1:
        a = float(input("digite cateto:"))
        b = float(input("digite cateto:"))
        e = (a**2) + (b**2)
        f = sqrt(e)
        print("la hiotenusa es: ",f,"\n")
        print ("DESEA HALLAR NUEVO CATETO O HIPOTENUSA?\n")
        print ("PRESIONE 1 SI QUIERE VOLVER A HALLAR\n")
        print ("PRESIONE 2 PARA SALIR\n")
        i = int(input("R:"))
    elif deseo == 2:
        c = float(input("digite hipotenusa:"))
        g = float(input("digite cateto:"))
        h = (c**2) - (g**2)
        f = sqrt(h)
        print("su cateto es:",f,"\n")
        print ("DESEA HALLAR NUEVO CATETO O HIPOTENUSA?\n")
        print ("PRESIONE 1 SI QUIERE VOLVER A HALLAR\n")
        print ("PRESIONE 2 PARA SALIR\n")
        i = int(input("R:"))
    else:
        print("WRONG NUMBER")
        print ("DESEA HALLAR NUEVO CATETO O HIPOTENUSA?\n")
        print ("PRESIONE 1 SI QUIERE VOLVER A HALLAR\n")
        print ("PRESIONE 2 PARA SALIR\n")
        i = int(input("R:"))
    