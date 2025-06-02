# Importar funciones de cada agente, prueba del agente 1
from agente1_analizador import extraer_genes

if __name__ == "__main__":

    fasta_file = "data/sample.fasta"  # Ruta del archivo sample.fasta

    # Lee la secuencia y detecta los genes
    genes = extraer_genes(fasta_file)

    # Imprime los genes que aparecen el sample.fasta
    print(genes)
