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
