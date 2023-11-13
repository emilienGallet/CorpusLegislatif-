"""
Corpus Législatif

Permet aux magistrats de la RPD d'avoir l'ensemble du corpus législatif dans leur main.


Auteur : GALLET Émilien
Date : 7 novembre 2023
"""
import CurlLaw
import DwldLaw
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import RequestsInstaller
import Traitement
import TupleToHTML
#import ActualiterEtMAJ

import webbrowser
import sys
import os


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    print_hi('Corpus législatif de la RPD')
    # Install les dépendances
    if getattr(sys, 'frozen', False):
        print("soyons fou")
    else:
        RequestsInstaller.RequestsInstaller()
    # Télécharge sur le site de la république les PC
    dataExportPVD = CurlLaw.CurlLaw(url="https://rpd.dirtybiologistan.com/exportPVD").data
    # dataFromDiscordChannel = ActualiterEtMAJ.ActualiterEtMAJ().data
    # Traite les données récoltée
    cleanedData = Traitement.Traitement.traiterDataExportPVD(dataExportPVD)
    dataFromVerifiyingSources, dataToFindSources = DwldLaw.DwldLaw(cleanedData=cleanedData).data()
    for url in dataToFindSources:
        webbrowser.open(url)


    # Affichage des résultats
    TupleToHTML.TupleToHTML(cleanedData).build(None, None)
    

    if getattr(sys, 'frozen', False):
        # L'exécutable a été généré par PyInstaller
        script_directory = os.path.dirname(sys.executable)
    else:
        # L'exécutable est exécuté en tant que script Python
        script_directory = os.path.dirname(os.path.abspath(__file__))
    print("Chemin du répertoire du script :", script_directory)
    # Spécifiez un fichier ou un répertoire relatif par rapport au répertoire du script
    relative_path = "default.html"  # Vous pouvez spécifier un fichier ou un répertoire ici

    # Composez le chemin complet du fichier relatif
    file_path = os.path.join(script_directory, relative_path)


    # URL de la page que vous souhaitez ouvrir
    url = "file://"+file_path

    # Ouvrir le navigateur par défaut avec l'URL spécifiée
    webbrowser.open(url)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
