import discord
import env

Client = discord.Client(intents=discord.Intents.default())

@Client.event #on ready (Bot start)
async def on_ready():
    print("Bot is ready!")

Client.run(env.TOKEN) 
