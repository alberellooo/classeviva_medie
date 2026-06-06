from ClasseVivaAPI import RequestURLs


def get_voti_raw(utente):
    """Recupera il JSON grezzo dei voti, sopprimendo l'output della libreria."""
    import io
    import contextlib

    # Sopprime qualsiasi print della libreria
    with contextlib.redirect_stdout(io.StringIO()):
        risposta = utente.request(RequestURLs.voti)

    if risposta is None:
        raise RuntimeError(
            "La richiesta dei voti non ha restituito dati. "
            "Verifica che il login sia riuscito e che ClasseViva risponda correttamente."
        )

    return risposta.json()


def calcola_medie(utente, quadrimestre: int) -> tuple:
    """
    Calcola le medie per materia filtrando per quadrimestre (1 o 2).
    Restituisce (medie, conteggio).
    """
    dati = get_voti_raw(utente)

    # Parole chiave per riconoscere il periodo
    keyword = "primo" if quadrimestre == 1 else "secondo"

    voti_per_materia = {}

    for voto in dati.get("grades", []):
        # Filtra per quadrimestre usando periodDesc
        period = voto.get("periodDesc", "").lower()
        if keyword not in period:
            continue

        materia = voto.get("subjectDesc", "SCONOSCIUTA").strip().upper()
        valore = voto.get("decimalValue")

        if valore is None:
            continue

        voti_per_materia.setdefault(materia, []).append(float(valore))

    medie = {
        materia: round(sum(vals) / len(vals), 2)
        for materia, vals in voti_per_materia.items()
        if vals
    }

    conteggio = {
        materia: len(vals)
        for materia, vals in voti_per_materia.items()
    }

    return medie, conteggio
