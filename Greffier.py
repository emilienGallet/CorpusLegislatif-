from discord.ext import tasks
from discord.ext import commands
import discord
from discord.ext.commands import bot


class Greffier(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.channels = kwargs['channels']
        # an attribute we can access from our task
        self.counter = 0

    # async def setup_hook(self) -> None:
    #     # start the task to run in the background
    #     self.my_background_task.start()

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
        # Récupération des anciens messages dans un canal spécifique
        channel = self.get_channel(self.channels[0])  # Remplacez YOUR_CHANNEL_ID par l'ID du canal
        if channel:
            async for message in channel.history(limit=None):  # Limit est le nombre de messages à récupérer
                # Faites quelque chose avec chaque message
                print(f"Message de {message.author}: {message.content}")

    # @tasks.loop(seconds=1)
    # async def my_background_task(self):
    #     channel = self.get_channel(self.channels[0])  # channel ID goes here
    #     self.counter += 1
    #     print(self.counter)
    #     await channel.send(self.counter)

    # async def on_message(self, message):
    #     print(f"Message de {message.author}: {message.content}")

    # @my_background_task.before_loop
    # async def before_my_task(self):
    #     await self.wait_until_ready()  # wait until the bot logs in
