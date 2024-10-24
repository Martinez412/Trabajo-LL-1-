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

# Función para calcular el conjunto de predicciones por regla
def calcular_predicciones(gramatica):
    primeros = calcular_primeros(gramatica)
    predicciones = {cabeza: {} for cabeza in gramatica}

    for cabeza, producciones in gramatica.items():
        for produccion in producciones:
            prediccion = set()
            if produccion:  # Asegurarse de que la producción no esté vacía
                for simbolo in produccion:
                    if simbolo in primeros:  # Si es un no terminal
                        prediccion.update(primeros[simbolo] - {'ε'})
                        if 'ε' not in primeros[simbolo]:  # Si no es ε, se detiene
                            break
                    else:  # Si es un terminal, añadir directamente
                        prediccion.add(simbolo)
                        break
                else:
                    # Si todos los símbolos en la producción pueden derivar en ε,
                    # se puede agregar a los siguientes.
                    if cabeza == 'S': 
                        prediccion.add('$')
            predicciones[cabeza][tuple(produccion)] = prediccion  # Tupla para tener un identificador de la producción

    return predicciones

# Función principal para calcular solo predicciones
def calcular_predicciones_de_gramatica(ruta_archivo):
    gramatica = leer_gramatica(ruta_archivo)
    return calcular_predicciones(gramatica)

# Ejecutar el código
ruta_archivo = 'Ejemplo.txt'  
predicciones_resultado = calcular_predicciones_de_gramatica(ruta_archivo)

# Mostrar los resultados
print("Predicciones:")
for nt, reglas in predicciones_resultado.items():
    for produccion, predicciones in reglas.items():
        print(f"Predicciones({nt} -> {' '.join(produccion)}): {predicciones}")
