import discord
import os
import requests 
import json

client = discord.Client()

keyword = ["sus"]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)


@client.event
async def on_ready():
  print ('we have logged in as {0.user}'.format(client) )



@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$springtrap'):
    await message.channel.send('yo that furry who killed 5 children at a pizzeria')
  
  if message.content.startswith('$motivate'):
    quote = get_quote()
    await message.channel.send(quote)

  if message.content.startswith('$jedi'):
    await message.channel.send(' Dripped out in swag, flooded in sadness')  

  if message.content.startswith('$exokn'):
   await message.channel.send('shut up jedi-prime was way better')
  
  if message.content.startswith('$tiger'):
   await message.channel.send('the mama bean')

  if message.content.startswith('$Bam'):
   await message.channel.send('Vroom is best') 

  if message.content.startswith('$skugg'):
   await message.channel.send('Yo SEXY man')  
  
  
@client.event
async def my_message(message):
  for i in range(len(keyword)):
    if keyword in message.content:
      for j in range(10):
        await message.channel.sent('STOP POSTING ABOUT AMONG US,IM TIRED OF SEEING THIS')
  

client.run(os.getenv('token'))
