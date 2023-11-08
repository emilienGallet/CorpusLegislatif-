import importlib
import subprocess
import sys

class RequestsInstaller:
    def __init__(self):
        self.check_and_install_requests('requests')
        self.check_and_install_requests('json')
        self.check_and_install_requests('pathlib')
        self.check_and_install_requests('os')
        self.check_and_install_requests('discord')

    def check_and_install_requests(self, x):
        # Vérifier si le module requests est installé
        try:
            importlib.import_module(x)
        except ImportError:
            # Le module requests n'est pas installé, nous allons l'installer
            print("Le module 'requests' n'est pas installé. Installation en cours...")

            # Utiliser pip pour installer requests
            subprocess.check_call([sys.executable, "-m", "pip", "install", x])

            print(f"Le module {x} a été installé avec succès.")
        else:
            print(f"Le module {x} est déjà installé.")

