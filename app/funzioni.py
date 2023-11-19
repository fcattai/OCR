from pdf2image import convert_from_path
import pytesseract
from os import listdir, path
import configparser

def leggi_parametri(file_ini):
    # Creazione di un oggetto ConfigParser
    config = configparser.ConfigParser()

    # Lettura del file .ini
    config.read(file_ini)

    # Ottenere i valori dai parametri
    sezione = 'Parametri'  # Sostituisci con il nome della sezione nel tuo file .ini
    p1 = config.get(sezione, 'input_directory_path')
    p2 = config.get(sezione, 'output_directory_path')

    # Restituire i valori letti
    return p1, p2

def pdf_to_text(pdf_path):
    print("\n\tacquisisco file...".format(pdf_path))

    images = convert_from_path(pdf_path)
    text = ""

    n = 1
    nn = len(images)

    for image in images:
        print("\tconverto pagina {0} di {1}".format(n, nn))
        text += pytesseract.image_to_string(image)
        n += 1

    return text

def lista_cartella(dir_path):
    lista = [f for f in listdir(dir_path) if path.isfile(path.join(dir_path, f))]
    return lista

def salva_txt(x, output_path):
    print("\tsalvo file {}".format(path.split(output_path)[1]))
    file = open(output_path, "w")
    file.write(x)
    file.close

    return True