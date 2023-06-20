import discord.message
import env

Client = discord.Client(intents=discord.Intents(messages=True,guilds=True))

test = "lol"

@Client.event #on ready (Bot start)
async def on_ready():
    print("Bot is ready!")

@Client.event
async def on_message(message):
    if message.author == Client.user:
        return
    if message.content == "meme":
        await message.channel.send("https://images7.memedroid.com/images/UPLOADED443/64050d8ccf075.webp")
    else :
        await message.channel.send("https://images7.memedroid.com/images/UPLOADED443/64050d8ccf075.webp")


Client.run(env.TOKEN) 
