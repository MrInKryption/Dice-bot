import discord
import random
TOKEN='NDk3Mzg5NzUwODk5MTc5NTMx.DpeeMA.FR6aeIqjsyAH-2y8Q-nlmCDnSB8'

client=discord.Client()

@client.event
async def on_message(message):
    #so the bot doesn't talk to itself
    if message.author == client.user:
        return

    if message.content.startswith('!roll20'):
        num=str(random.randrange(0,20,1)%20+1)
        msg='You have rolled {0.author.mention} '.format(message)+num
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!roll6'):
        num=str(random.randrange(0,6,1)%6+1)
        msg='You have rolled {0.author.mention} '.format(message)+num
        await client.send_message(message.channel,msg)
    elif message.content.startswith('!roll100'):
        num=str(random.randrange(0,100,1)%100+1)
        msg='You have rolled {0.author.mention} '.format(message)+num
        await client.send_message(message.channel,msg)

@client.event
async def on_ready():
    print("logged in as")
    print(client.user.name)
    print(client.user.id)
    print('-----------')

client.run(TOKEN)
