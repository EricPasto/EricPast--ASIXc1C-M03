
def getAppleSongStanza(applesCount):
    if (applesCount == 0):
        print("Final.")
    else:
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
        print(stanza)
        return applesCount - 1
        getAppleSongStanza(applesCount)

getAppleSongStanza(2)