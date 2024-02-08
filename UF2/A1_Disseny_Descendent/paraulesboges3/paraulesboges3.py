import random
import datetime
import os
import logging

def fer_aleatories():
    with open("paraules.txt", "r") as f:
        text = f.read()

    paraules = text.split()
    paraulesboges = []
    caractersespecials = [",", ".", "?", "¿", "'", "!", "¡", ":", ";"]
    for p in paraules:
        if len(p) <= 3:
            paraulesboges.append(p)
        elif p[-1] in caractersespecials:
            paraulesboges.append(p[0] + ''.join(random.sample(p[1:-2], len(p)-3)) + p[-2] + p[-1])
        else:
            paraulesboges.append(p[0] + ''.join(random.sample(p[1:-1], len(p)-2)) + p[-1])

    with open("boges.txt", "w") as f:
        f.write(' '.join(paraulesboges))

def fer_aleatories_entrada():
    input_dir = "entrada"
    output_dir = "sortida"
    log_dir = "log"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Configurar logging
    logging.basicConfig(filename=os.path.join(log_dir, "boges.log"),
                        level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    for filename in os.listdir(input_dir):
        try:
            with open(os.path.join(input_dir, filename), "r") as f:
                text = f.read()

            paraules = text.split()
            paraulesboges = []
            caractersespecials = [",", ".", "?", "¿", "'", "!", "¡", ":", ";"]
            for p in paraules:
                if len(p) <= 3:
                    paraulesboges.append(p)
                elif p[-1] in caractersespecials:
                    paraulesboges.append(p[0] + ''.join(random.sample(p[1:-2], len(p) - 3)) + p[-2] + p[-1])
                else:
                    paraulesboges.append(p[0] + ''.join(random.sample(p[1:-1], len(p) - 2)) + p[-1])

            new_filename = os.path.splitext(filename)[0] + "_boges" + os.path.splitext(filename)[1]
            with open(os.path.join(output_dir, new_filename), "w") as f:
                f.write(' '.join(paraulesboges))

            # Loggear evento exitoso
            logging.info("Archivo procesado: %s", filename)

        except Exception as e:
            # Loggear error
            logging.error("Error al procesar archivo %s: %s", filename, str(e))

try:
    fer_aleatories()
    fer_aleatories_entrada()
except Exception as e:
    # Loggear error general
    logging.error("Error general: %s", str(e))


