import discord
from core import booze
client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='$help'))

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
            await message.channel.send("Happy Drinking {0.author.mention}! 🍻".format(message))

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
            await message.channel.send("Happy Drinking {0.author.mention}! 🍻".format(message))
            

    if message.content.startswith('$help'):
        await message.channel.send("```\n For getting Price of a specific catagory or a specific drink \n write   $drink <Drink Name> \n\n For getting Price of a specific catagory or a specific drink within a specific price range \n write  $rngdrink <Lower Price Limit> <Higher Price Limit> <Drink Name> \n```")

client.run('ODA0NTkwMDczNjAwNjcxNzU0.YBOi5g.3RV2cQVcSRCo8OXMmPuFhy_VPss')