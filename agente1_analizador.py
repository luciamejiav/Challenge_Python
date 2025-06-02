from Bio import SeqIO # Librería para leer el archivo .fasta

# Ejemplo de diccionario de ADN, he cogido 3 secuencias aleatorias del archivo sample.fasta
diccionario_genes = {
    "ATGGCC": "Gen1", 
    "GGTGGA": "Gen2", 
    "GCGCTA": "Gen3"
}


# Definir la función que extrae los genes
def extraer_genes(fasta_path):
    registro = next(SeqIO.parse(fasta_path, "fasta")) # Lee la primera línea del archivo
    secuencia = str(registro.seq) # Convertir la secuencia en un string 

    encontrar_genes = [] # Lista para almacenar genes encontrados

    # Comparar el diccionario con la secuencia de sample.fasta para ver si alguno coincide
    for patron, gen in diccionario_genes.items():
        if patron in secuencia:
            encontrar_genes.append(gen)

    return encontrar_genes # Devuelve la lista con los genes que ha encontrado
    
