# ClasseViva Voti

Piccola app desktop per accedere a ClasseViva con username e password, scegliere il quadrimestre e visualizzare le medie dei voti in una finestra grafica.

> Progetto realizzato in stile **vibecoding**: iterazione rapida, refactor progressivi e verifica pratica dell'eseguibile finale.

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
.\.venv\Scripts\python.exe files\main.py
```

Se non usi il virtualenv già presente, installa prima le dipendenze:

```powershell
pip install -r files\requirements.txt
```

## Creazione dell'exe

Il progetto include uno script di build:

```powershell
.\build_exe.ps1
```

L'eseguibile viene generato in:

```powershell
dist\ClasseVivaVoti.exe
```

In alternativa puoi usare PyInstaller direttamente:

```powershell
pyinstaller --noconfirm --clean ClasseVivaVoti.spec
```

## Struttura

- `files/main.py` — entry point dell'app
- `files/gui.py` — interfaccia grafica
- `files/auth.py` — login ClasseViva
- `files/voti.py` — recupero e calcolo medie
- `files/display.py` — formattazione risultati
- `build_exe.ps1` — script di compilazione
- `ClasseVivaVoti.spec` — configurazione PyInstaller

## Note

- Le credenziali vengono inserite localmente nella finestra dell'app.
- L'app dipende dai servizi ClasseViva: se il servizio non risponde, il login o il recupero voti possono fallire.
- L'`.exe` può essere segnalato da alcuni antivirus perché generato con PyInstaller.

