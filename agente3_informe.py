def generar_informe(enfermedades, informe = "informe.pdf"):  # Dependiendo del formato que queramos ponemos pdf o md (markdown)

    # Abro el archivo para escribir el informe
    with open(informe, "w") as f: 
        f.write("# INFORME DEL ANALISIS GENETICO\n\n") # Título

        # Bucle para encontrar las enfermedades asociadas a los genes
        for gen, enfermedad in enfermedades.items():
            f.write(f"## Gen: {gen}\n")
            f.write("Enfermedades asociadas:\n")

            for e in enfermedad:
                f.write(f"- {e}\n")

            f.write("\n")