# Función para leer la gramática desde el archivo de texto
def leer_gramatica(ruta_archivo):
    gramatica = {}
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if '->' in linea:
                cabeza, producciones = linea.split('->')
                cabeza = cabeza.strip()
                # Reemplazar 'lambda' por 'ε' para representar la cadena vacía
                producciones = [prod.strip().replace('lambda', 'ε').split() for prod in producciones.split('|')]
                if cabeza not in gramatica:
                    gramatica[cabeza] = []
                gramatica[cabeza].extend(producciones)
    return gramatica

# Función para calcular el conjunto de primeros
def calcular_primeros(gramatica):
    primeros = {nt: set() for nt in gramatica}

    def obtener_primeros(simbolo):
        if simbolo not in gramatica:  # Es un terminal
            return {simbolo}
        if primeros[simbolo]:  # Ya fue calculado
            return primeros[simbolo]
        for produccion in gramatica[simbolo]:
            for prod_simbolo in produccion:
                prod_primeros = obtener_primeros(prod_simbolo)
                primeros[simbolo].update(prod_primeros - {'ε'})
                if 'ε' not in prod_primeros:
                    break
            else:
                primeros[simbolo].add('ε')
        return primeros[simbolo]

    for nt in gramatica:
        obtener_primeros(nt)
    return primeros

# Función principal 
def calcular_primeros_unicamente(ruta_archivo):
    gramatica = leer_gramatica(ruta_archivo)
    primeros_resultado = calcular_primeros(gramatica)
    return primeros_resultado

ruta_archivo = 'Ejemplo.txt' 
primeros_resultado = calcular_primeros_unicamente(ruta_archivo)

# Mostrar los resultados
print("Primeros:")
for nt, primeros in primeros_resultado.items():
    print(f"Primeros({nt}): {primeros}")