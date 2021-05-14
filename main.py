import discord
import requests 
import json
import os
from discord.ext import commands, tasks
from random import choice
import aiohttp


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

@client.command(name='tiger' help= 'custom command') 
async def tiger(ctx):
    await ctx.send('The Mama Bean')    

@client.command(name='skugg' help= 'custom command') 
async def skugg(ctx):
    await ctx.send('Aeyo Sexy Man')

@client.command(name='jedi' help= 'custom command') 
async def jedi(ctx):
    await ctx.send('Dripped out in swag, flooded in sadness') 

@client.command(name='crimsonwolf' help= 'custom command') 
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

@client.command(name= 'pikachu' help= 'try it you will like it')
async def pikachu(ctx):
    async with aiohttp.ClientSession() as session:
        requests = await session.get('https://some-random-api.ml/img/pikachu') #requests
        pikajson = await requests.json() #json file comversion
    embed = discord.Embed(title = "pika pika!!!", color=discord.Colour.purple())    
    embed.set_image(url=pikajson['link'])
    await ctx.send(embed=embed) #send message   

@client.command(name= 'kanye' help= 'does it need any expaining')
async def kanye(ctx):
   response = requests.get("https://api.kanye.rest")
   json_data = json.loads(response.text)
   quote = json_data['quote'] 
   await ctx.send(quote)

@client.command(name= 'friends' help= 'try it you will like it')   
async def friends(ctx):
   response = requests.get("https://friends-quotes-api.herokuapp.com/quotes/random")
   json_data = json.loads(response.text)
   quote = json_data['quote']+ " -" + json_data['character']
   await ctx.send(quote)
	

@client.command(name= 'neko' help='kawaii neko')
async def neko(ctx):
    async with aiohttp.ClientSession() as session:
        requests = await session.get("https://some-random-api.ml/img/cat") #requests
        nekojson = await requests.json() #json file comversion
    embed = discord.Embed(title = "kore nani kore nani kore nani!!!", color=discord.Colour.purple())    
    embed.set_image(url=nekojson['link'])
    await ctx.send(embed=embed) #send message   	
	
@client.command(name= 'nasa', help='nasa pic of the day')
async def nasa(ctx):
    async with aiohttp.ClientSession() as session:
        requests = await session.get('https://api.nasa.gov/planetary/apod?api_key=7xKltd5lPuRF7sgqb5ADJFRsma0gFaB6BosJ9nsA') #requests
        nasajson = await requests.json() #json file comversion
    embed = discord.Embed(title = "Nasa pic of the day", color=discord.Colour.purple())    
    embed.set_image(url=nasajson['hdurl'])
    await ctx.send(embed=embed) #send message	


@client.command(name= 'inu', help='doge')
async def inu(ctx):
    doge = ['https://image.shutterstock.com/image-vector/kawaii-shiba-inu-dogs-various-600w-1280941399.jpg', 'https://image.shutterstock.com/image-vector/cute-shiba-inu-head-emotions-600w-731808382.jpg', 'https://image.freepik.com/free-vector/cute-shiba-inu-dog-astronaut-sitting-cartoon-icon-illustration_138676-2797.jpg', 'https://akm-img-a-in.tosshub.com/indiatoday/images/story/202105/dog1.jpg?bwcnVhNjzF2qX4wcVgHjvdr1qrqTMmMB&size=770:433']
    reply = choice (doge)
    await ctx.send(reply) #send message

@client.command(name= "toge")
async def toge(ctx):
    inumaki = ['Shake', 'Okaka', 'Tsunamayo', 'Tsuna', 'Takana', 'Mentaiko', 'Konbu', 'Ikura', 'Sujiko', 'https://tenor.com/view/toge-inumaki-jujutsu-kaisen-anime-gif-20440927', 'https://tenor.com/view/toge-inumaki-okaka-jujutsu-kaisen-gif-19663987']
    await ctx.send(choice (inumaki)) #send message
	
@client.command(name= "atlas" help= 'Shitland Official')  
async def atlas(ctx):
    so = ['https://im2.ezgif.com/tmp/ezgif-2-aba1e271f6e7.gif', 'Onii-chan', 'My brother from another Mother', 'stay safe from markass atlas']
    await ctx.send(choice (so))


@client.command(name= "batman" help= 'batman fortnite')
async def batman(ctx):
	bruce = ['https://cdn.discordapp.com/attachments/779580860935831613/841895402931355648/video0.mp4', 'https://cdn.discordapp.com/attachments/779572154567622682/841097690841743370/3337CF3B-203E-46A5-903B-17430819B3CA.mov', 'Batman Fortnite', 'I am Batman']
	await ctx.send(choice (bruce))	 
	
@tasks.loop(seconds=20)
async def change_status():
	await client.change_presence(activity=discord.Game(choice(status)))

  

client.run(os.getenv('token'))
