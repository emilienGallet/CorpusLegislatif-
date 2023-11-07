import json
import math


class Traitement:
    ValidePCCriteria = 3

    choixVote = {'CINQ': 5, 'QUATRE': 4, 'TROIS': 3, 'DEUX': 2, 'UN': 1}

    # TODO taitement du json pour crée un corpus législatif

    @classmethod
    def traiterData(cls, data: dict):
        # manque d'effectifcode civil
        print("Traitement des données relatives au PC qui on été accepter")
        s = """Due a un problème au niveau du site, les PC dans le répertoire onValidatePc est Vide, pour cela on va 
        utiliser directement le répertoire onResultPC et calculer les PC qui ont été acceptée"""
        print(s)

        onresultPC: list = data.get("onResultPC")
        validatedPCVR = list()
        # on récupère les PCVR
        onVotePCReponses: list = data.get("onVotePCReponse")
        for unePcResult in onresultPC:
            # Dans le cas où il n'y avait pas d'affichage de résultat (fait main)
            if (unePcResult.get("resultat") == '{}'):
                # on définit une liste qui va renvoyer les identifiants des PCVR par rapport à cette PC
                pairIdPCVREtidPC: list = []
                for unePCVR in unePcResult.get("reponses2"):
                    pairIdPCVREtidPC.append(unePCVR.get("idPCVR"))
                # on récupère l'ensemble des votes
                onVote: list = data.get("votes")
                somme = 0
                participant = 0
                for vote in onVote:
                    vote: dict = vote
                    # Si l'identifiant est présent dans la liste
                    print(pairIdPCVREtidPC.__contains__(vote.get('idPCVR')), vote.get('idPCVR'))
                    if pairIdPCVREtidPC.__contains__(vote.get('idPCVR')):
                        print("todo")
                        somme += Traitement.choixVote.get(vote.get('choixVote'))
                        participant += 1

            # else:
                # # print("récupéré le résultat")
                # resultDict: dict = json.loads(unePcResult.get("resultat"))
                # for (idPCVR, valuePCVR) in resultDict.items():
                #     # a vérifier si il n'y a pas un bug qui risque de survenir
                #     print(valuePCVR.get('val0') / valuePCVR.get('val1'))
                #     print(valuePCVR.get('val0') / valuePCVR.get('val1') >= Traitement.ValidePCCriteria)
                #     res = valuePCVR.get('val0') / valuePCVR.get('val1')
                #     if res >= Traitement.ValidePCCriteria:
                #         validatedPCVR.append((idPCVR, unePcResult.get('question2'), valuePCVR.get('val3'), res))
        return validatedPCVR
