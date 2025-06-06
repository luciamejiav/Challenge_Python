# Challenge_Python

## Objetivo
**Diseñar un sistema en Python que utilice agentes de IA para:** <br>
1. Analizar una secuencia genética (formato FASTA proporcionado).<br>
2. Identificar genes clave presentes en la secuencia.<br>
3. Predecir enfermedades asociadas a estos genes utilizando un modelo preentrenado o una API externa.<br>
4. Generar un informe automatizado con los resultados del análisis.<br><br>

## Requisitos:

### 1. Entrada del usuario:<br>
  - Un archivo en formato **FASTA** con una secuencia genética.<br><br>
### 2. Tareas de los agentes:<br>
  - **Agente 1**: Leer y analizar el archivo FASTA, identificando genes clave (utilizando un diccionario de genes predefinido o un recurso en línea).<br>
  - **Agente 2**: Consultar una API (puede ser ficticia o real, como la de NCBI o Ensembl) para buscar enfermedades asociadas a los genes detectados.<br>
  - **Agente 3**: Generar un informe en formato PDF o Markdown con los resultados, incluyendo:<br>
    - Lista de genes encontrados.<br>
    - Enfermedades asociadas.<br>
    - Resumen del análisis.<br><br>

## Modo de ejecución:
La ejecución de este challenge es muy sencilla. Cada agente tiene una función independiente, pero todos ellos se unen en el fichero main. <br><br>
En el **fichero main** es donde ejecutaremos el proyecto completo. Esto se puede hacer de **dos formas** en Visual Studio Code: 
 1. En la esquina superior derecha del fichero main hay un **símbolo play ▶︎**, al pulsarlo se ejecuta automaticamente el fichero en la terminal. Además genera los informes en formato .pdf o .md, depende de lo que hayamos puesto, en un fichero independiente.
 2. En el menú superior izquierdo hacemos click en *Run*, se despliega un segundo menú en el que tenemos que seleccionar *Run Without Debugging*.

