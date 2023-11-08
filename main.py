"""
Corpus Législatif

Permet aux magistrats de la RPD d'avoir l'ensemble du corpus législatif dans leur main.


Auteur : GALLET Émilien
Date : 7 novembre 2023
"""
import CurlLaw
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import RequestsInstaller
import Traitement
import TupleToHTML
import ActualiterEtMAJ


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    print_hi('Corpus législatif de la RPD')
    # Install les dépendances
    RequestsInstaller.RequestsInstaller()
    # Télécharge sur le site de la république les PC
    dataExportPVD = CurlLaw.CurlLaw(url="https://rpd.dirtybiologistan.com/exportPVD").data
    dataFromDiscordChannel = ActualiterEtMAJ.ActualiterEtMAJ().data
    # Traite les données récoltée
    ###cleanerData = Traitement.Traitement.traiterDataExportPVD(dataExportPVD)
    # Affichage des résultats
    ###TupleToHTML.TupleToHTML(cleanerData).build(None, None)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
