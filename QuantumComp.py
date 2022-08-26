import math

def suma(Real_P1,Img_P1,Real_P2,Img_P2):
    return (Real_P1+Real_P2,Img_P1+Img_P2)
def resta(Real_P1,Img_P1,Real_P2,Img_P2):
    return (Real_P1-Real_P2,Img_P1-Img_P2)
def producto(Real_P1,Img_P1,Real_P2,Img_P2):
    return (Real_P1*Real_P2-Img_P1*Img_P2,Real_P1*Img_P2+Real_P2*Img_P1)
def division(Real_P1,Img_P1,Real_P2,Img_P2):
    return (round((((Real_P1*Real_P2)+(Img_P1*Img_P2))/(Real_P2**2+Img_P2**2)),2),round((((Real_P2*Img_P1)-(Real_P1*Img_P2))/(Real_P2**2+Img_P2**2)),2))
def modulo(Real_P1,Img_P1):
    return(round(math.sqrt(Real_P1**2+Img_P1**2),2))
def conjugado(Real_P1,Img_P1):
    return(Real_P1,(-1)*Img_P1)
def conversCp(Real_P1,Img_P1):
    return(round(math.sqrt(Real_P1**2+Img_P1**2),2),round(math.atan(Img_P1/Real_P1)*180/math.pi))
def phase(Real_P1,Img_P1):
    return round(math.atan(Img_P1/Real_P1)*180/math.pi,2)

print("Bienvenido a la libreria de computacion cuantica.")

print("\nEl sistema acepta las siguientes operaciones:")
print("     1.Suma.")
print("     2.Resta.")
print("     3.Producto.")
print("     4.Division.")
print("     5.Modulo.")
print("     6.Conjugado.")
print("     7.Conversion de cartesianas a polares.")
print("     8.Retornar la fase del numero complejo.")

opcion=int(input("Ingrese el numero de la operacion que quiere ejecutar: "))

print("\nDame un numero complejo: ")
Real_P1=int(input("\nInserta la parte real: "))
Img_P1=int(input("Inserte la parte imaginaria: "))
if opcion<=4 and opcion!=0:    
    print("\nDame otro un numero complejo: ")
    Real_P2=int(input("\nInserta la parte real: "))
    Img_P2=int(input("Inserte la parte imaginaria: "))
    if opcion == 1 :
        if(suma(Real_P1,Img_P1,Real_P2,Img_P2)[1]>=0):
            print(suma(Real_P1,Img_P1,Real_P2,Img_P2)[0]," + ",suma(Real_P1,Img_P1,Real_P2,Img_P2)[1],"i")
        else:
            print(suma(Real_P1,Img_P1,Real_P2,Img_P2)[0]," - ",abs(suma(Real_P1,Img_P1,Real_P2,Img_P2)[1]),"i")
    elif opcion == 2 :
        if(resta(Real_P1,Img_P1,Real_P2,Img_P2)[1]>=0):
            print(resta(Real_P1,Img_P1,Real_P2,Img_P2)[0]," + ",resta(Real_P1,Img_P1,Real_P2,Img_P2)[1],"i")
        else:
            print(resta(Real_P1,Img_P1,Real_P2,Img_P2)[0]," - ",abs(resta(Real_P1,Img_P1,Real_P2,Img_P2)[1]),"i")
    elif opcion == 3 :
        if(producto(Real_P1,Img_P1,Real_P2,Img_P2)[1]>=0):
            print(producto(Real_P1,Img_P1,Real_P2,Img_P2)[0]," + ",producto(Real_P1,Img_P1,Real_P2,Img_P2)[1],"i")
        else:
            print(producto(Real_P1,Img_P1,Real_P2,Img_P2)[0]," - ",abs(producto(Real_P1,Img_P1,Real_P2,Img_P2)[1]),"i")
    else:
        if(division(Real_P1,Img_P1,Real_P2,Img_P2)[1]>=0):
            print(division(Real_P1,Img_P1,Real_P2,Img_P2)[0]," + ",division(Real_P1,Img_P1,Real_P2,Img_P2)[1],"i")
        else:
            print(division(Real_P1,Img_P1,Real_P2,Img_P2)[0]," - ",abs(division(Real_P1,Img_P1,Real_P2,Img_P2)[1]),"i")
elif opcion>=5:
    if opcion==5:
        print(modulo(Real_P1,Img_P1))
    elif opcion==6:
        if(conjugado(Real_P1,Img_P1)[1]>=0):
            print(conjugado(Real_P1,Img_P1)[0]," + ",conjugado(Real_P1,Img_P1)[1],"i")
        else:
            print(conjugado(Real_P1,Img_P1)[0]," - ",(conjugado(Real_P1,Img_P1)[1]),"i")
    elif opcion==7:
        print("(",conversCp(Real_P1,Img_P1)[0],",",conversCp(Real_P1,Img_P1)[1],"°)")
    else:
        print(phase(Real_P1,Img_P1),"°")
else:
    print("La opcion digitada no es admitida.")