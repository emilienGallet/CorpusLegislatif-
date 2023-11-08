"""
Gestion au niveau du channel discord a parsé
"""
salonASuivre = "https://discord.com/channels/904736069080186981/930041311992631317"
import discord
from Greffier import Greffier
class ActualiterEtMAJ:
    def __init__(self):
        # utilisation de https://github.com/Rapptz/discord.py
        # nécéssaire pour avoir le token du bot
        self.tokenOfBot = open("token.txt", 'r').read()
        self.permissionDuBotInteger = 66560
        self.GeneratedURL = ("https://discord.com/api/oauth2/authorize?client_id=1171397599694172210&permissions=66560&scope=bot")
        self.data = None
        self.intents = discord.Intents().all()
        self.intents.dm_messages = True
        # self.intents.value = self.permissionDuBotInteger
        #self.intents.reactions=True
        #self.intents.messages = True
        self.channels = [1171739888190758922, 904736069667397634, 930041311992631317]
        self.client = Greffier(intents=self.intents, channels=self.channels)
        self.client.run(self.tokenOfBot)
