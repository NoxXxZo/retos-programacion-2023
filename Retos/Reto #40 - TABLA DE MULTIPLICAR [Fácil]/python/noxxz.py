"""
 # Crea un programa que sea capaz de solicitarte un número y se
 # encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 # - Debe visualizarse qué operación se realiza y su resultado.
 #   Ej: 1 x 1 = 1
 #       1 x 2 = 2
 #       1 x 3 = 3
 #       ... 
 """
def main():
    while True:
        try:
            num = int(input("Ingrese un numero: "))
            for i in range(1,11):
                result = num*i
                print(f"{num} x {i} = {result}")
   
            next = input("¿Desea continuar? (s/n): ")
            if next.lower() != 's':
                break
        except ValueError:
            print("La entrada no es valida.")

if __name__ == "__main__":
    main()
