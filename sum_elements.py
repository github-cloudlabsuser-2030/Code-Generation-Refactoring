def obtener_enteros(n):
    arr = []
    print(f"Introduce {n} enteros:")
    for _ in range(n):
        while True:
            try:
                numero = int(input())
                arr.append(numero)
                break
            except ValueError:
                print("Entrada no válida. Por favor, introduce un entero válido.")
    return arr

def sumar_elementos(arr):
    return sum(arr)

def main():
    n = int(input("¿Cuántos enteros deseas introducir? "))
    enteros = obtener_enteros(n)
    suma = sumar_elementos(enteros)
    print(f"La suma de los elementos es: {suma}")

if __name__ == "__main__":
    main()