# INTERFAZ GRÁFICA

import streamlit as st
from Bio import SeqIO 
from agente1_analizador import extraer_genes
from agente2_enfermedades import extraer_enfermedades
from agente3_informe import generar_informe
import os

# Ruta archivo fasta 
fasta_file = "data/sample.fasta"

st.title("🧬 Análisis Genético - Interfaz Gráfica Simple")

# Verificamos que el archivo exista
if not os.path.exists(fasta_file):
    st.error("No se encontró el archivo sample.fasta")
    st.stop()

# Función para obtener secuencia de ADN completa
def leer_secuencia(fasta_path):
    record = next(SeqIO.parse(fasta_path, "fasta"))
    return str(record.seq)

# Leer y mostrar la secuencia
secuencia = leer_secuencia(fasta_file)
st.subheader("🔠 Secuencia de ADN")
st.code(secuencia, language="text")

# AGENTE 1: Analizar
genes_detectados = extraer_genes(fasta_file)
st.subheader("📍 Genes encontrados en la secuencia")

if genes_detectados:
    for gen in genes_detectados:
        # Buscar posición del patrón en la secuencia
        if gen == "Gen1":
            patron = "ATGGCC"
        elif gen == "Gen2":
            patron = "GGTGGA"
        elif gen == "Gen3":
            patron = "GCGCTA"
        else:
            patron = ""

        #Bucle para encontrar las posiciones de la secuencia
        if patron:
            posiciones = []
            inicio = 0
            while True:
                pos = secuencia.find(patron, inicio)
                if pos == -1:
                    break
                posiciones.append(pos) # Guardamos la posición encontrada
                inicio = pos + 1 # Avanzamos el índice para seguir buscando

            for p in posiciones:
                st.markdown(f"- **{gen}** encontrado en posición `{p}`")
else:
    st.warning("No se detectaron genes conocidos.")

# AGENTE 2: Enfermedades
enfermedades = extraer_enfermedades(genes_detectados)
st.subheader("🩺 Enfermedades asociadas")

# Lista de enfermedades
for gen, lista in enfermedades.items():
    st.markdown(f"**{gen}**:")
    for enf in lista:
        st.markdown(f"- {enf}")

# AGENTE 3: Informe
generar_informe(enfermedades, "informe.md")

# Mostrar informe
with open("informe.md", "r") as f:
    contenido = f.read()
    st.markdown(contenido)

# Botón para descargar
with open("informe.md", "rb") as file:
    st.download_button("📥 Descargar informe Markdown", file.read(), file_name="informe.md")
