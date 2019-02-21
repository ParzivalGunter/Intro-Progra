#Entradas
#Salidas
#Restricciones

def quiz(a,b,c):
    if (a+b>c):
        prom= a+b+c/3
        prod= a*b*c
        print ("Promedio de los valores es: " ,round(prom,2),"\nProducto de los valores es: ",prod)
    else:
        print ("No se pueda ejecutar la operación")
