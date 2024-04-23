#convertir de fahrenheit a celsius 
#c= (f-32) x 5/9

def convertir(f):
    c=(f-32)*5/9
    return c

f= float (input("ingresa los grados fahrenheit"))
print(f"la conversion a grados celsius es:{convertir(f)}°") 