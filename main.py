# This is a sample Python script.
import CurlLaw
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import RequestsInstaller
import Traitement
import TupleToHTML


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Corpus législatif de la RPD')
    RequestsInstaller.RequestsInstaller()
    data = CurlLaw.CurlLaw(url="https://rpd.dirtybiologistan.com/exportPVD").data
    cleanerData = Traitement.Traitement.traiterData(data)
    TupleToHTML.TupleToHTML(cleanerData).build(None, None)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
