#-*-coding:cp949
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('login')
    print(client.user.name)
    print(client.user.id)
    print('------------------')
    await client.change_presence(game=discord.Game(name='¤¾¤·', type=1))

@client.event
async def on_message(message):
    if message.content.startswith('Ã»¼Ò'):
        await client.send_message(message.channel, '!Ã»¼Ò 99')

client.run('NTU4NTMzOTQ0NzM2NDgxMjgz.D3oqdQ.GLCET0Drk9IOn1I0OR44G-JNGMk')
