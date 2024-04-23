num1=int (input("ingresa un número"))
num2=int (input("ingresa otro numero"))

eleccion= 0

while eleccion!=6:
    print("""
          indique la operación que desea realizar:
          1)Suma
          2)Resta
          3)Multiplicacio0n
          4)Division
          5)Cambiar Valores
          6)Salir
          """)
    
    eleccion = int(input())

    if eleccion== 1:
        print(" ")
        print("resultado: ", num1,"+",num2,"=", num1+num2)
    if eleccion== 2:
            print("")
            print("resultado:", num1,"-",num2,"=",num1-num2)
    if eleccion== 3:
         print("")
         print("resultado", num1,"*",num2,"=", num1*num2)
    if eleccion== 4:
         print("")
         print("resultado:",num1,"/",num2,"=",num1/num2)
    if eleccion== 5: 
         num1=int (input("ingresa un número"))
         num2=int (input("ingresa otro numero"))
    if eleccion== 6:
         print("gracias por utilizar esta calculadora, espero te haya sido efectiva")

         
     
     
