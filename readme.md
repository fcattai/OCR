# Scansione OCR
questo programma converte un file PDF in uno TXT, estraendo il testo contenuto nelle pagine.

## Tesseract
il programma richiede Tesseract installato sul PC
* installa versione nella cartella `tesseract\WIN INSTALLER`, ad esempio nel percorso `tesseract\WIN EXE`
* aggiungi `tesseract\WIN EXE` alla variabile d'ambiente `Path`
* riavvia PC

## dipendenze Python
* packaging==23.2
* pdf2image==1.16.3
* Pillow==10.1.0
* pytesseract==0.3.10

## pyinstaller

```
pyinstaller --hidden-import=pdf2image --add-binary "D:\Autarchia\OCR\tesseract\WIN EXE;." main.py
```

## utilizzo Python con virtualenv
```
env\Scripts\activate
python main.py
deactivate
```

oppure lancia il file `avvia_OCR.bat`