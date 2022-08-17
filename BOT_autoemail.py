from http import client
import discord
client = discord.Client()

@client.event
async def on_massage(message):
    message.content = message.content.lower()
    if message.author = client.user:
        return
    if message.author.startwith("hello")

        if str(message.author) == 
