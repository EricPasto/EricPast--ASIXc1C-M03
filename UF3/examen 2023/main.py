import paraules
import paraulesvocals
import logging
import os
try:
    log_dir = "log"
    paraules.calcular_paraules()
    #paraulesvocals.calcular_vocals()
    logging.basicConfig(filename=os.path.join(log_dir, "paraules.log"),
                        level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.info("Archivo procesado: paraules.py")
except Exception as e:
    # Loggear error general
    logging.error("Error al procesar archivo %s: %s", "paraules.log", str(e))


