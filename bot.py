#-*-coding:cp949
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('login')
    print(client.user.name)
    print(client.user.id)
    print('------------------')
    await client.change_presence(game=discord.Game(name='����', type=1))

@client.event
async def on_message(message):
    if message.content.startswith('û��'):
        await client.send_message(message.channel, '!û�� 99')

client.run('NTU4NTMzM2NDgxMjgx.D3oqdQ.GLCETDrk9IOn1I0OR44G-JNGMk')