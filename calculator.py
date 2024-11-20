def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

numero1 = 5
numero2 = 4

print("Suma:", suma(numero1, numero2))
print("Resta:", resta(numero1, numero2))
print("Multiplicación:", multiplicacion(numero1, numero2))
print("División:", division(numero1, numero2))