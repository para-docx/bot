import discord
import os
import requests 
import json

client = discord.Client()

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
  


client.run(os.getenv('token'))
