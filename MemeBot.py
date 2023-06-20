import discord 
import discord.message
import env
intents = discord.Intents.default()
intents.message_content = True
Client = discord.Client(intents=intents)

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
        await message.channel.send("try 'meme'")


Client.run(env.TOKEN) 
