"""
Eric Pastó

Examen UF3
"""

import logging
import os
import paraules
import paraulesquantitat

# Configuración del registro de eventos
logging.basicConfig(filename='main.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Llamadas a las funciones de los módulos paraules y paraulesvocals
try:
    paraules.guardar_paraules_per_cua("paraules.txt", "paraules_lletres", "sortida")
    logging.info("Se han guardado las palabras por letras correctamente.")
except Exception as e:
    logging.error(f"Error al guardar las palabras por letras: {str(e)}")

try:
    paraulesquantitat.copiar_i_afegir_lletres("paraules.txt", "paraulesQuantitat.txt")
    logging.info("Se ha creado el archivo 'paraulesQuantitat.txt' correctamente.")
except Exception as e:
    logging.error(f"Error al crear el archivo 'paraulesQuantitat.txt': {str(e)}")
