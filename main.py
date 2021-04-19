import discord
import requests 
import json
import os
from discord.ext import commands, tasks
from random import choice
import aiohttp
import youtube_dl

client = commands.Bot(command_prefix="#")

status = ["sus","hey hey","your so sussy", "19$ fortnite card", "sheeeeesh", "lessssgooo"]


@client.event
async def on_ready():
  change_status.start()
  print ('we have logged in as {0.user}'.format(client))


@client.command(name= 'inspire', help='you need it')
async def inspire(ctx):
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    await ctx.send(quote)

@client.command(name='tiger') 
async def tiger(ctx):
    await ctx.send('The Mama Bean')    

@client.command(name='skugg') 
async def skugg(ctx):
    await ctx.send('Aeyo Sexy Man')

@client.command(name='jedi') 
async def jedi(ctx):
    await ctx.send('Dripped out in swag, flooded in sadness') 

@client.command(name='crimsonwolf') 
async def crimsonwolf(ctx):
    await ctx.send('Aeyo its the wolf :wolfpoggers:go check him out at twitch.tv/twitch_chase05')  
                   

@client.command(name= 'dogpics', help='you need dog pics just use it')
async def dogpics(ctx):
    async with aiohttp.ClientSession() as session:
        requests = await session.get('https://some-random-api.ml/img/dog') #requests
        dogjson = await requests.json() #json file comversion
    embed = discord.Embed(title = "heres a cute dog pic for you!!!", color=discord.Colour.purple())    
    embed.set_image(url=dogjson['link'])
    await ctx.send(embed=embed) #send message

@client.command(name= 'pikachu')
async def pikachu(ctx):
    async with aiohttp.ClientSession() as session:
        requests = await session.get('https://some-random-api.ml/img/pikachu') #requests
        pikajson = await requests.json() #json file comversion
    embed = discord.Embed(title = "pika pika!!!", color=discord.Colour.purple())    
    embed.set_image(url=pikajson['link'])
    await ctx.send(embed=embed) #send message   

@client.command(name= 'kanye')
async def kanye(ctx):
   response = requests.get("https://api.kanye.rest")
   json_data = json.loads(response.text)
   quote = json_data['quote'] 
   await ctx.send(quote)

@client.command(name= 'friends')   
async def friends(ctx):
   response = requests.get("https://friends-quotes-api.herokuapp.com/quotes/random")
   json_data = json.loads(response.text)
   quote = json_data['quote']+ " -" + json_data['character']
   await ctx.send(quote)
	

@client.command(name= 'neko')
async def neko(ctx):
    async with aiohttp.ClientSession() as session:
        requests = await session.get("https://some-random-api.ml/img/cat") #requests
        nekojson = await requests.json() #json file comversion
    embed = discord.Embed(title = "kore nani kore nani kore nani!!!", color=discord.Colour.purple())    
    embed.set_image(url=nekojson['link'])
    await ctx.send(embed=embed) #send message   	
	
@client.command(name= "play")
async def play(ctx, url : str, channel):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel)
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3")) 

@client.command(name= 'dc')
async def dc(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")
	
@client.command(name= 'pause')
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        await voice.pause()
    else:    
        await ctx.send("you dum dum")    
	
@client.command(name= 'resume')
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        await voice.resume()
    else:
       await ctx.send("you dum dum") 

	
	
	
	

@tasks.loop(seconds=20)
async def change_status():
	await client.change_presence(activity=discord.Game(choice(status)))

  

client.run(os.getenv('token'))
