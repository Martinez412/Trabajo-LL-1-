# Trabajo Algoritmos, Primeros, Siguientes Y Predicción

* Manuel Cardenas

* Andres Toledo

* Bryan Ariza

* Juan Wilches


Introduccion
En este trabajo se busco calcular los conjuntos de primeros, los conjutos de siguientes de una gramatica a partir de un archivo txt y calcular los conjuntos de prediccion de las reglas de la gramatica gramatica

* PASOS A SEGUIR

  1) Instalacion de Python
     Estos codigos se ejecutaron en Phyton desde la terminal de Ubuntu para ello se debeActualizar el sistema esto sirve para una buena 
     práctica  y asegurarse de que nuestro sistema esté actualizado. para ello ejecuta el siguiente comando:

          sudo apt update
          sudo apt upgrade
2) Dependiendo de la versión de Ubuntu, Python puede estar preinstalado pero para instalar Python 3 es solo ejecutar:

        sudo apt install python3
   
3) Si también necesitas el gestor de paquetes pip para Python, puedes instalarlo con el siguiente comando:

       sudo apt install python3-pip

4) Por ultimo debemos comprobar que Python se ha instalado correctamente para ello solo se escribe el siguiente comando:

        python3 --version

* EJECUTAR EL PROGRAMA

  1) Para ejecutar el programa solo debes descargar los 3 codigos .py y el archivo txt luego guardalos en una carpeta y alamcena esa carpeta en el escritorio o las descargas o en cualquier sitio que prefiera para acceder a esa carpeta nomas es acceder con el siguiente comando
 
            cd Descargas (Downloads)
            ls  (combrobar si la carpeta de conjuntos esta ahi)
            cd Conjuntos (o cualquier nombre que le puso a la carpeta)
            ls (combrobar que estan los 3 codigos.py de los conjuntos y el archivo txt)

  2) luego solo debes ingresar los siguientes comandos una vez estes dentro de la carpeta de de conjuntos dentro de la terminal de ubuntu

          Python3 Primeros.py  (Ejecutar el codigo que calcula el conjunto de primeros)
          Python3 Siguientes.py (Ejecutar el codigo que calcula el conjunto de Siguientes)
          Phyton3 Prediccion.py (Ejecutar el codigo que calcula el conjunto de prediccion)

  3) la gramatica que esta guardada en el txt es la siguientes:

          A -> B C 
          A -> ant A all
          B -> big C
          B -> bus A boss
          B -> lambda
          C -> cat
          C -> cow
si quieres cambiar la gramaticas solo debes esjecutar este comando en donde ejecutaste los codigos de conjuntos

       nano Ejemplo.txt

esto dejara cambiar la gramatica para volver a ejecutar el codigo con diferentes gramaticas o tambien es recomendable solo entra al archivo desde el bloc de notas y guardalo con la teclas ctrl + s y colver a ejecutar los codigos de conjuntos cabe aclarar que si cambia el nombre del archivo txt por otro tambien debera cambiarlo desde los codigos con el comando 

         nano  Primeros.py
         
con esto solo cambia el nombre del archivo txt por el que se modifico en caso tal de cambiar el txt 


