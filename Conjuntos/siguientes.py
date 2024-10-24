

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

# Función para calcular el conjunto de siguientes
def calcular_siguientes(gramatica):
    siguientes = {nt: set() for nt in gramatica}
    siguiente_inicial = next(iter(gramatica))  # El primer no terminal
    siguientes[siguiente_inicial].add('$')  # Regla 1: el símbolo inicial contiene $

    def obtener_siguientes(nt):
        for cabeza, producciones in gramatica.items():
            for produccion in producciones:
                for i, simbolo in enumerate(produccion):
                    if simbolo == nt:
                        # Regla 2: Si hay algo después del símbolo actual en la producción
                        if i + 1 < len(produccion):
                            siguiente_simbolo = produccion[i + 1]
                            if siguiente_simbolo in gramatica:  # Es un no terminal
                                siguientes[nt].update(primeros_de(siguiente_simbolo) - {'ε'})
                                if 'ε' in primeros_de(siguiente_simbolo):
                                    siguientes[nt].update(siguientes[cabeza])
                            else:  # Es un terminal
                                siguientes[nt].add(siguiente_simbolo)
                        # Regla 3: Si el símbolo está al final de la producción o lo que sigue puede derivar ε
                        if i + 1 == len(produccion) or 'ε' in primeros_de(produccion[i + 1]):
                            siguientes[nt].update(siguientes[cabeza])

    # Función para obtener los primeros de un símbolo esencial solo para siguientes
    def primeros_de(simbolo):
        if simbolo not in gramatica:
            return {simbolo}  # Si es un terminal, devolverlo como conjunto
        primeros = set()
        for produccion in gramatica[simbolo]:
            for prod_simbolo in produccion:
                primeros.update(primeros_de(prod_simbolo) - {'ε'})
                if 'ε' not in primeros_de(prod_simbolo):
                    break
            else:
                primeros.add('ε')
        return primeros

    cambiando = True
    while cambiando:
        cambiando = False
        copia_siguientes = {nt: conjunto.copy() for nt, conjunto in siguientes.items()}
        for nt in gramatica:
            obtener_siguientes(nt)
        if copia_siguientes != siguientes:
            cambiando = True

    return siguientes

# Función principal
def calcular_conjunto_de_siguientes(ruta_archivo):
    gramatica = leer_gramatica(ruta_archivo)
    return calcular_siguientes(gramatica)

# Ejecucion
if __name__ == "__main__":
    ruta_archivo = 'Ejemplo.txt'
    siguientes_resultado = calcular_conjunto_de_siguientes(ruta_archivo)

    # Mostrar los resultados
    for nt, siguientes in siguientes_resultado.items():
        print(f"Siguientes({nt}): {siguientes}")
