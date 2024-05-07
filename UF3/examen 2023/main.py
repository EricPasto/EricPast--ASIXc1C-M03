import logging
import os
import paraules
import paraulesvocals

# Configuración del registro de eventos
logging.basicConfig(filename='main.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Llamadas a las funciones de los módulos paraules y paraulesvocals
try:
    paraules.guardar_paraules_per_longitud("paraules.txt", "paraules_longitud", "sortida")
    logging.info("Se han guardado las palabras por longitud correctamente.")
except Exception as e:
    logging.error(f"Error al guardar las palabras por longitud: {str(e)}")

try:
    paraulesvocals.copiar_i_afegir_vocals("paraules.txt", "paraulesQuantitatVocals.txt")
    logging.info("Se ha creado el archivo 'paraulesQuantitatVocals.txt' correctamente.")
except Exception as e:
    logging.error(f"Error al crear el archivo 'paraulesQuantitatVocals.txt': {str(e)}")
