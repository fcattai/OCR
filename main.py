from os import listdir, path
from art import tprint
from pdf2image import convert_from_path
from pytesseract import image_to_string

def pdf_to_text(pdf_path):
    # print("\n\tacquisisco file...".format(pdf_path))

    images = convert_from_path(pdf_path)
    text = ""

    n = 1
    nn = len(images)

    for image in images:
        print("\tconverto pagina {0} di {1}".format(n, nn))
        text += image_to_string(image)
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

if __name__ == "__main__":
    
    tprint("\nscansione OCR", font="cybermedium")

    file_da_convertire = input("\ntrascina qui il file da convertire e premi <INVIO>:\t")
    file_da_convertire = file_da_convertire.replace("& ", "")
    file_da_convertire = file_da_convertire.replace("'", "")
    file_da_convertire = file_da_convertire.replace('"', '')
    file_da_convertire = path.normpath(file_da_convertire)

    output_directory_path = path.split(file_da_convertire)[0]
    nome_file = path.split(file_da_convertire)[1].split('.')[0]

    print("\ninizio conversione {}\n".format(nome_file))

    pdf_text = pdf_to_text(file_da_convertire)
    file_convertito = path.join(output_directory_path, nome_file + ".txt")
    salva_txt(pdf_text, file_convertito)

    print("\nfine conversione {}\n".format(nome_file))

    input("premere <INVIO> per concludere")