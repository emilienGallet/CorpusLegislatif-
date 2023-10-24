class CurlLaw:



    def __init__(self, url):
        import requests

        # Effectuer la requête GET
        response = requests.get(url)

        # Vérifier si la requête a réussi (code de statut 200)
        if response.status_code == 200:
            # Extraire les données JSON de la réponse
            self.data = response.json()


        else:
            print("La requête a échoué avec le code de statut :", response.status_code)

