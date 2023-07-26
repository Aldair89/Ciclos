# Ciclo for: Iterar sobre una lista
lista = [1, 2, 3, 4, 5]
print("Ciclo for:")
for elemento in lista:
    print(elemento)
print()

# Ciclo while: Contar hasta un número específico
numero_limite = 10
contador = 1
print("Ciclo while:")
while contador <= numero_limite:
    print(contador)
    contador += 1
print()

# Ciclo do-while (emulado): Pedir un número al usuario hasta que sea mayor a 10
print("Ciclo do-while (emulado):")
numero = 0
while True:
    numero = int(input("Ingrese un número mayor a 10: "))
    if numero > 10:
        break
print("Número válido:", numero)
