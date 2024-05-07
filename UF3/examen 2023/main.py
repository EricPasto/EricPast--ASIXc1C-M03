import paraules
import paraulesvocals
import logging
import os

paraules.guardar_paraules_per_longitud("paraules.txt", "paraules_longitud", "sortida")

paraulesvocals.copiar_i_afegir_vocals("paraules.txt", "paraulesQuantitatVocals.txt")



