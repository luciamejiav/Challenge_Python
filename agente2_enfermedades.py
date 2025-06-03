# Diccionario para asociar los genes anteriores con enfermedades conocidas, simula una pequeña api ficticia
gen_a_enfermedad = {
    "Gen1": ["Cancer", "Anemia"],
    "Gen2": ["Sindrome de Down"],
    "Gen3": ["Diabetes"]
}

# Creamos un diccionario que almacena las enfecmedades según su gen
def extraer_enfermedades(genes):
    resultado = {} 

    for gen in genes:
        # Sacar las enfermedades del diccionario, si hay, y si no está que ponga "Sin identificar"
        resultado[gen] = gen_a_enfermedad.get(gen, ["Sin identificar"])

    return resultado


