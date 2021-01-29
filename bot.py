import discord
from core import booze
client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$drink'):
        drink = message.content[6:]
        drinks = booze(drink, 0, 0)
        if(len(drinks) == 0): await message.channel.send("Beep.Boop. No drinks found! 🥺")
        else:
            for drink in drinks: 
                await message.channel.send("```CSS\n"+drink[0] + " --> " + drink[1]+"\n```")
            await message.channel.send("Happy Drinking! 🍻")

    if message.content.startswith('$rngdrink'):
        text = message.content[9:].split()
        low = text[0]
        high = text[1]
        drink = " ".join(text[2:])
        drinks = booze(drink, low, high)
        if(len(drinks) == 0): await message.channel.send("Beep.Boop. No drinks found! 🥺")
        else:
            for drink in drinks: 
                await message.channel.send("```CSS\n"+drink[0] + " --> " + drink[1]+"\n```")
            await message.channel.send("Happy Drinking! 🍻")

client.run('ODA0NTkwMDczNjAwNjcxNzU0.YBOi5g.3RV2cQVcSRCo8OXMmPuFhy_VPss')