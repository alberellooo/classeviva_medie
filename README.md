# ClasseViva Voti

**SE VUOI USARLO SUBITO, SCARICA L'.`exe` ED ESEGUILO**

> Progetto *vibecoded*

Piccola app desktop per accedere a ClasseViva con username e password, scegliere il quadrimestre e visualizzare le medie dei voti in una finestra grafica.

## Funzionalità

- Login ClasseViva da interfaccia grafica
- Scelta tra primo e secondo quadrimestre
- Tabella con medie per materia
- Riepilogo con media generale, numero voti e numero materie
- Creazione di un `.exe` per Windows

## Requisiti

- Windows
- Python 3.14 o compatibile
- Connessione internet

## Avvio da sorgente

Da cartella progetto:

```powershell
.\.venv\Scripts\python.exe Codice\main.py
```

Se non usi il virtualenv già presente, installa prima le dipendenze:

```powershell
pip install -r Codice\requirements.txt
```

## Creazione dell'exe

Il progetto include uno script di build:

```powershell
.\Codice\build_exe.ps1
```

L'eseguibile viene generato in:

```powershell
ClasseVivaVoti.exe
```

In alternativa puoi usare PyInstaller direttamente:

```powershell
pyinstaller --noconfirm --clean Codice\ClasseVivaVoti.spec
```

## Struttura

- `ClasseVivaVoti.exe` — eseguibile pronto all'uso
- `Codice/main.py` — entry point dell'app
- `Codice/gui.py` — interfaccia grafica
- `Codice/auth.py` — login ClasseViva
- `Codice/voti.py` — recupero e calcolo medie
- `Codice/display.py` — formattazione risultati
- `Codice/build_exe.ps1` — script di compilazione
- `Codice/ClasseVivaVoti.spec` — configurazione PyInstaller

## Note

- Le credenziali vengono inserite localmente nella finestra dell'app.
- L'app dipende dai servizi ClasseViva: se il servizio non risponde, il login o il recupero voti possono fallire.
- L'`.exe` può essere segnalato da alcuni antivirus perché generato con PyInstaller.
