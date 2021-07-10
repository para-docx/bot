import discord
import requests 
import json
import os
from discord.ext import commands, tasks
from random import choice
import aiohttp


client = commands.Bot(command_prefix="&")

statuses = ["sus","hey hey","your so sussy", "19$ fortnite card", "sheeeeesh", "lessssgooo"]


@client.event
async def on_ready():
  change_status.start()
  print ('we have logged in as {0.user}'.format(client))
	
	
@client.event
async def on_message(message):
    if message.content.startswith('&greet'):
        channel = message.channel
        await channel.send('Say hello!')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send('Hello {.author}!'.format(msg))
	


@client.command(name= 'inspire', help='you need it')
async def inspire(ctx):
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    await ctx.send(quote)

@client.command(name='tiger', help= 'custom command') 
async def tiger(ctx):
    await ctx.send('The Mama Bean')    

@client.command(name='skugg', help= 'custom command') 
async def skugg(ctx):
    await ctx.send('Aeyo Sexy Man')

@client.command(name= 'fatal', help= 'custom command')
async def fatal(ctx):
    laughter = ['Yo that injury looks fatal', 'uwu senpaii', 'sexy mans sexy friend']
    await ctx.send(choice (laughter))

@client.command(name='jedi', help= 'custom command') 
async def jedi(ctx):
    await ctx.send('Dripped out in swag, flooded in sadness') 

@client.command(name='crimsonwolf', help= 'custom command') 
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

@client.command(name= 'pikachu', help= 'try it you will like it')
async def pikachu(ctx):
    async with aiohttp.ClientSession() as session:
        requests = await session.get('https://some-random-api.ml/img/pikachu') #requests
        pikajson = await requests.json() #json file comversion
    embed = discord.Embed(title = "pika pika!!!", color=discord.Colour.purple())    
    embed.set_image(url=pikajson['link'])
    await ctx.send(embed=embed) #send message   

@client.command(name= 'kanye', help= 'does it need any expaining')
async def kanye(ctx):
   response = requests.get("https://api.kanye.rest")
   json_data = json.loads(response.text)
   quote = json_data['quote'] 
   await ctx.send(quote)

@client.command(name= 'friends', help= 'try it you will like it')   
async def friends(ctx):
   response = requests.get("https://friends-quotes-api.herokuapp.com/quotes/random")
   json_data = json.loads(response.text)
   quote = json_data['quote']+ " -" + json_data['character']
   await ctx.send(quote)
	

@client.command(name= 'neko', help='kawaii neko')
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

@client.command(name= "toge", help= 'Shake')
async def toge(ctx):
    inumaki = ['Shake', 'Okaka', 'Tsunamayo', 'Tsuna', 'Takana', 'Mentaiko', 'Konbu', 'Ikura', 'Sujiko', 'https://tenor.com/view/toge-inumaki-jujutsu-kaisen-anime-gif-20440927', 'https://tenor.com/view/toge-inumaki-okaka-jujutsu-kaisen-gif-19663987']
    await ctx.send(choice (inumaki)) #send message
	
@client.command(name= "atlas", help= 'Shitland Official')  
async def atlas(ctx):
    so = ['https://im2.ezgif.com/tmp/ezgif-2-aba1e271f6e7.gif', 'Onii-chan', 'My brother from another Mother', 'stay safe from markass atlas']
    await ctx.send(choice (so))


@client.command(name= "batman", help= 'batman fortnite')
async def batman(ctx):
	bruce = ['https://cdn.discordapp.com/attachments/779580860935831613/841895402931355648/video0.mp4', 'https://cdn.discordapp.com/attachments/779572154567622682/841097690841743370/3337CF3B-203E-46A5-903B-17430819B3CA.mov', 'Batman Fortnite', 'I am Batman']
	await ctx.send(choice (bruce))	 
	
@client.command(name = "julius_caesar", help= "Words of wisdom from who played a critical role in the events that led to the demise of the Roman Republic and the rise of the Roman Empire. (Do people even read these!!!)")
async def julius_caesar(ctx):
    cezza = ['Experience is the teacher of all things.', 'I love treason but hate a traitor.', 'What we wish, we readily believe, and what we ourselves think, we imagine others think also.', 'If you must break the law, do it to seize power: in all other cases observe it.', 'Which death is preferably to every other? ’The unexpected’.', 'I have lived long enough both in years and in accomplishments.', 'Et tu, Brute?', 'The fault, dear Brutus, is not in our stars/ But in ourselves.', 'ceeesaaaaasrrrr'] 
    await ctx.send(choice (cezza))

@client.command(name= "floppa", help=" the mighty") 
async def floppa(ctx):
    flop = ['https://i.kym-cdn.com/entries/icons/original/000/034/421/cover1.jpg', 'https://i.ytimg.com/vi/G_u44siEyJo/mqdefault.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGLW2RBDI3MjeNUU473wSBvEZjBUxWIABkRw&usqp=CAU', 'https://i.imgflip.com/4oigcn.jpg', 'https://i.pinimg.com/736x/33/2d/b1/332db19ba58081bfc51ca37ec9c88de3.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2bQkPDsUkS6dT6Qbg5GbtSgzo-uUF5ZsTvvq7l_ewZvEJKS3xLrUKgA9L7WdtJxqV4Gk&usqp=CAU', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMCpekbaqcHag6V65-BUeeWI_yM8M6HlKQu-d6MLB3tBh2p7dNewErs1jqCB630omfJ5E&usqp=CAU', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQP1nZkQIqNKHad7Xx9t2oxVlTGW-liWQPUr0UGcc177ABNQQ4_R3MbRyvZvcvHe7jwiXY&usqp=CAU', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZMNJdj6iV1Y32Rz80_KNamMsis6G1ekvlAtd--va09xx7aWvZFNvvYAxrOEDp00_4Zic&usqp=CAU', 'https://preview.redd.it/jpga1s11vhk61.png?width=1440&format=png&auto=webp&s=74807deb7fc03c51174044b1e132885bef5333af', 'https://cdn.discordapp.com/attachments/779581058495807518/843802136324472862/FB_IMG_1612176430416-2-1.png']
    await ctx.send(choice (flop))

@client.command(name= "yesorno", help="are you that dumb") 
async def yesorno(ctx):
    cho = ['yes', 'no']
    await ctx.send(choice (cho))

	
@client.command(name = 'markass', help= 'Custom command for my friend Markass')
async def markass(ctx):
    Browmlee= ['https://cdn.discordapp.com/attachments/779577666197389343/837355894304014416/Screenshot_2021-04-29-21-23-16-88_572064f74bd5f9fa804b05334aa4f912.jpg', 'markyboo', 'https://cdn.discordapp.com/attachments/788741047386767390/844204881241309184/image0-185.jpg', 'hes the one.', 'https://i.imgur.com/7DshJqE.jpg', 'https://cdn.discordapp.com/attachments/779577666197389343/836933658412843028/unknown.png', 'https://cdn.discordapp.com/attachments/825762563450208347/844208504460804177/unknown.png', 'Brownass Marklee', 'https://cdn.discordapp.com/attachments/825762563450208347/850809778616008754/unknown.png', 'https://cdn.discordapp.com/attachments/779577666197389343/801196044070551572/image0.png', 'Ryzen Girl', 'https://cdn.discordapp.com/attachments/779577666197389343/791162558249172992/unknown.png']
    await ctx.send(choice (Browmlee))  

	
@client.command(name='hanako', help='custom command for my friend snugg')  
async def hanako(ctx):
    amane = ['https://tenor.com/view/smiling-hanako-anime-hanakokun-smile-gif-16236551', 'https://tenor.com/view/tsukaza-toilet-bound-hanakokun-gif-21061643', 'https://tenor.com/view/hanako-toilet-bound-kun-gif-18134872', 'Hey snugg youre awesome', 'https://tenor.com/view/heart-love-anime-hanakokun-heart-shape-gif-16852717', 'https://ih1.redbubble.net/image.1712095670.1074/flat,750x,075,f-pad,750x1000,f8f8f8.jpg', 'https://pm1.narvii.com/7774/2e53535d400717ee501656a515950801ec434b64r1-694-461v2_hq.jpg', 'https://media.tenor.com/images/b95644c56e27ce8e244458c94c0e0f3d/tenor.png']
    await ctx.send(choice (amane))    
	
@client.command(name='persona', help= 'atlus teen fantasy') 
async def persona(ctx):
    Zoker = ['https://tenor.com/view/morgana-fortnite-chug-jug-with-you-gif-20562744', 'https://tenor.com/view/persona-dancing-dance-moves-video-game-gif-17945073', 'IZANAGIIII', 'https://cdn.discordapp.com/attachments/825762563450208347/845297788689580122/RDT_20210521_1921151844502508137153738jpg.jpg', 'https://cdn.discordapp.com/attachments/825762563450208347/845298590196563968/RDT_20210521_1924334488963785709934944jpg.jpg', 'https://cdn.discordapp.com/attachments/825762563450208347/845299312871473182/RDT_20210521_192725587641235393546664jpg.jpg', 'https://www.youtube.com/watch?v=wz65xOwKd9s', 'https://cdn.discordapp.com/attachments/825762563450208347/845300590740897822/RDT_20210521_1931452105787096126387883jpg.jpg', 'https://cdn.discordapp.com/attachments/825762563450208347/845300590317404190/RDT_20210521_1929053187109223972681431jpg.jpg', 'https://cdn.discordapp.com/attachments/825762563450208347/845300589804912650/RDT_20210521_1928481543871330396996020jpg.jpg', 'https://steamuserimages-a.akamaihd.net/ugc/829077318575835900/49D77B03D4EB4B7D0CEA0B0DF7D8434AD17C167D/', 'https://preview.redd.it/n97leva41gu61.jpg?width=640&crop=smart&auto=webp&s=de65e12403ab567f667e76819529e9d8fc39449f', 'https://cdn.discordapp.com/attachments/825762563450208347/845302730208575538/iwato_dormitory.mp3', 'https://cdn.discordapp.com/attachments/665833993249488908/845308877875707904/meme.png', 'https://tenor.com/view/icant-cum-persona3-persona4-persona-icant-gif-18113782', 'https://cdn.discordapp.com/attachments/665833993249488908/845308957799350362/unknown.png', 'https://cdn.discordapp.com/attachments/779572154567622683/845710809971294278/video0-16-1.mp4', 'https://cdn.discordapp.com/attachments/682082597156945977/846017523148259369/536316c.jpg']    
    await ctx.send(choice(Zoker))
   	
	
	
@tasks.loop(seconds=20)
async def change_status():
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="Livinn life Keith Amamiya style, watching jedi grinding P5R", url='https://www.twitch.tv/exokn'))
	
    ## game = discord.Game("Updates and Upgrades")
    ## await client.change_presence(status=discord.Status.dnd, activity=game)
  

client.run(os.getenv('token'))
