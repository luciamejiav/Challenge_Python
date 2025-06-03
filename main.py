# Importar funciones de cada agente
from agente1_analizador import extraer_genes
from agente2_enfermedades import extraer_enfermedades
from agente3_informe import generar_informe

def main():
    fasta_file = "data/sample.fasta"  # Ruta del archivo sample.fasta

    # Lee la secuencia y detecta los genes
    genes = extraer_genes(fasta_file)

    enfermedades = extraer_enfermedades(genes)

    generar_informe(enfermedades)

    # Imprime los genes que aparecen el sample.fasta
    print("\n\n AGENTE 1: ",genes, "\n AGENTE 2: ", enfermedades, "\n", "AGENTE 3: informe.pdf", "\n\n")

# Pide que se haga de manera modular, por lo que definimos y llamamos
if __name__ == "__main__":
    main()
    