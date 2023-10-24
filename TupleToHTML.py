import pathlib
import os
from  pathlib import PurePath

class TupleToHTML:
    defaulName = "defaut.html"
    defaulPath = os.getcwd()
    def __init__(self, data_tuple):
        # Créez une chaîne de caractères HTML pour le tableau
        html_table = "<table>"
        for row in data_tuple:
            html_table += "<tr>"
            for item in row:
                html_table += "<td>" + str(item) + "</td>"
            html_table += "</tr>"
        html_table += "</table>"
        self.content = html_table

    def build(self, nameFile, path):
        # Obtenir le répertoire de travail actuel
        current_directory = path
        if path is None:
            current_directory = os.getcwd()

        # Spécifier le nom du fichier que vous voulez créer
        file_name = nameFile
        if nameFile is None :
            file_name = TupleToHTML.defaulName

        # Combiner le répertoire de travail actuel avec le nom de fichier
        file_path: PurePath= pathlib.PurePath(current_directory, file_name)

        # Convertissez le chemin en une chaîne de caractères
        str_file_path = file_path.as_posix()

        # Ouvrez le fichier en mode écriture pour le créer
        with open(str_file_path, 'w') as file:
            file.write(self.content)
