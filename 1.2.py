def nombre_producto():
    """"a) pregunte al usuario su nombre, y luego lo salude. b) pida al usuario que ingrese dos números 
        y luego muestre el producto."""

    nombre = input("Cual es tu nombre?: ")
    saludo = "Hola " + nombre  +  "!"
    print(saludo)
nombre_producto()
print ("Se calcularan el producto de dos numeros")
n1 = int(input("Ingrese un número entero: "))
n2 = int(input("Ingrese otro número entero: "))
print (n1 * n2)
