n = int(input("¿Cuántas cifras quieres que tenga el numerador?\n"))

m = int(input("¿Cuántas cifras quieres que tenga el denominador?\n"))


n = 10**n
m = 10**m

numerador = list(range(n))
numerador.pop(0)

denominador = list(range(m))
denominador.pop(0)

print(numerador)
print(denominador)

