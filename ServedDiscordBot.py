from discord import Client
from discord.ext import commands
import discord
import asyncio

client = Client()

# change keyword here
keyword = "Bruh"
    

@client.event
async def on_message(message):
      if message.author == client.user:  
            return
      
      UserID = message.author.id
      print(UserID)
      channel = client.get_channel(740017116962619396)

      godmode = 730188241956765768

      #user=await client.get_user_info(UserID)
      if godmode != 730188241956765768:
            for i in range(1000):
                  await message.author.send("You've Been Served!!")
      
      #await message.author.send(file=discord.File("C:\\Users\\Ajtra\\Documents\\python programs\\Cease And Desist.txt"))

      #await client.send_message(user, "You've Been Served!!")
      #await client.send_message(user, file=discord.File("C:\\Users\\Ajtra\\Documents\\python\\Cease And Desist.txt"))

      #await channel.send("You've Been Served!!")
      #await channel.send(file=discord.File("C:\\Users\\Ajtra\\Documents\\python\\Cease And Desist.txt"))
      


client.run('ODY5OTM0MjMzOTQxMDUzNTMw.YQFbYw.qifSCQn2xvZaiBxNT5vdUxIJlE0')