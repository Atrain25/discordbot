from discord import Client
from discord.ext import commands
import discord
import asyncio

client = Client()

# change keyword here
    

@client.event
async def on_message(message):
      if message.author == client.user:  
            return
      
      UserID = message.author.id
      print(UserID)
      channel = client.get_channel("YOUR CHANNEL HERE")
        
      #This allows a user to not be affected by the bot
      godmode = 730188241956765768

      #user=await client.get_user_info(UserID)
      if godmode != 730188241956765768:
            for i in range(1000):
                  await message.author.send("You've Been Served!!")
      


client.run('YOUR TOKEN HERE')
