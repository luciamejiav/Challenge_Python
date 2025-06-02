# Importar funciones de cada agente
from agente1_analizador import extraer_genes
from agente2_enfermedades import extraer_enfermedades

if __name__ == "__main__":

    fasta_file = "data/sample.fasta"  # Ruta del archivo sample.fasta

    # Lee la secuencia y detecta los genes
    genes = extraer_genes(fasta_file)

    enfermedades = extraer_enfermedades(genes)

    # Imprime los genes que aparecen el sample.fasta
    print(genes, "\n", enfermedades)
