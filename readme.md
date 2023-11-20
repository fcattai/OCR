# Scansione OCR
questo programma converte un file **PDF** in uno **TXT**, estraendo il testo contenuto nelle pagine:

* avviare il programma
  * vedi sezione [**utilizzo Python con virtualenv**](#utilizzo-python-con-virtualenv)
* trascinare nella finestra del terminale il file **PDF** da convertire
* il file **TXT** viene scritto nella posizione dove è salvato il file **PDF** trascinato

## Tesseract
il programma richiede Tesseract installato sul PC
* installa versione nella cartella `tesseract\WIN INSTALLER`, ad esempio nel percorso `tesseract\WIN EXE`
* aggiungi `tesseract\WIN EXE` alla variabile d'ambiente `Path`
* riavvia PC

## Dipendenze Python
* packaging==23.2
* pdf2image==1.16.3
* Pillow==10.1.0
* pytesseract==0.3.10

## Utilizzo Python con virtualenv

### Ambiente Windows
```
env\Scripts\activate
python main.py
deactivate
```
>in alternativa lancia il file `avvia_OCR.bat`

### Ambiente Linux/Mac
```
source venv/bin/activate
python main.py
deactivate
```

## Compilazione eseguibile Windows con pyinstaller

```
pyinstaller --hidden-import=pdf2image --add-binary "D:\Autarchia\OCR\tesseract\WIN EXE;." main.py
```