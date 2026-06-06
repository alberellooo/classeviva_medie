from ClasseVivaAPI import Utente, RequestURLs


def login(username: str, password: str) -> Utente:
    """
    Effettua il login a ClasseViva e restituisce l'oggetto Utente autenticato.
    Lancia un'eccezione se le credenziali sono errate.
    """
    utente = Utente(uid=username, pwd=password)
    risposta = utente.login()

    if not getattr(utente, "is_logged_in", False):
        dettaglio = ""
        if risposta is not None:
            try:
                dettaglio = risposta.text.strip()
            except Exception:
                dettaglio = ""

        messaggio = "Login fallito. Controlla username e password."
        if dettaglio:
            messaggio = f"{messaggio} Dettagli API: {dettaglio}"
        raise RuntimeError(messaggio)

    return utente
