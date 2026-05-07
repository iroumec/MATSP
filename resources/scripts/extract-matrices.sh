#!/bin/bash

ORIGEN="./resources/atsp-instances/raw-instances"
DESTINO="./resources/atsp-instances/cleaned-instances"

# Creación del directorio destino por si no existe.
mkdir -p "$DESTINO"

for archivo in "$ORIGEN"/*; do

    # Verificación de que es un archivo.
    [ -f "$archivo" ] || continue

    nombre_archivo=$(basename "$archivo")

    # Se usa awk para la extracción:
    # - Se busca la línea 'EDGE_WEIGHT_SECTION'.
    # - A partir de ahí, imprime las líneas siguientes.
    # - Se detiene si encuentra 'EOF' o llega al final del archivo.
    awk '
        /EDGE_WEIGHT_SECTION/ { flag=1; next } 
        /EOF/ { flag=0 } 
        flag { print }
    ' "$archivo" > "$DESTINO/$nombre_archivo"

done

echo "Matrices extraidas en '$DESTINO'."