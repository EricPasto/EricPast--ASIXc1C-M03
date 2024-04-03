
def getAppleSongStanza(applesCount):
    stanza = f"{applesCount} pometes té el pomer,\n" \
 \
             f"de {applesCount} una, de {applesCount} una,\n" \
 \
             f"{applesCount} pometes té el pomer,\n" \
 \
             f"de {applesCount} una en caigué.\n" \
 \
             f"Si mireu el vent d'on vé\n" \
 \
             f"veureu el pomer com dansa,\n" \
 \
             f"si mireu el vent d'on vé\n" \
 \
             f"veureu com dansa el pomer."

    return stanza

applesCount= input("Numero de pomes: ")

def getAppleSong(applesCount):
    if (applesCount == 0):
        print("final")
    else:
        return applesCount -1
        getAppleSongStanza()

getAppleSongStanza()