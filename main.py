from os import listdir, path
import app.funzioni as fx


if __name__ == "__main__":
    
    file_ini = 'config/parametri.ini'
    input_directory_path, output_directory_path = fx.leggi_parametri(file_ini)
    
    lista_files = fx.lista_cartella(input_directory_path)

    for p in lista_files:
        print("\n{}: inizio conversione...".format(p))

        pdf_text = fx.pdf_to_text(path.join(input_directory_path, p))
        file_convertito = path.join(output_directory_path, p.split(".")[0] + ".txt")

        # print("\tscrivo file {}".format(p.split(".")[0] + ".txt"))
        # file = open(file_convertito, "w")
        # file.write(pdf_text)
        # file.close

        fx.salva_txt(pdf_text, file_convertito)

        print("\n{}: fine conversione\n".format(p))