import discord
import responses
import os
import random
from dotenv import load_dotenv

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        if not response == "":
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} je reku: '{user_message}' ({channel})")

        if user_message == '/sexy':
            random_file=random.choice(os.listdir("./src/sexy"))
            path = './src/sexy/' + random_file
            await message.channel.send(file=discord.File(path))
        elif user_message == '?/sexy':
            random_file=random.choice(os.listdir("./src/sexy"))
            path = './src/sexy/' + random_file
            await message.author.send(file=discord.File(path))  

        if user_message == '/zlebnik':
            random_file=random.choice(os.listdir("./src/zlebnik"))
            path = './src/zlebnik/' + random_file
            await message.channel.send(file=discord.File(path))
        elif user_message == '?/zlebnik':
            random_file=random.choice(os.listdir("./src/zlebnik"))
            path = './src/zlebnik/' + random_file
            await message.author.send(file=discord.File(path))  

        if user_message == '/tomo':
            random_file=random.choice(os.listdir("./src/tomo"))
            path = './src/tomo/' + random_file
            await message.channel.send(file=discord.File(path))
        elif user_message == '?/tomo':
            random_file=random.choice(os.listdir("./src/tomo"))
            path = './src/tomo/' + random_file
            await message.author.send(file=discord.File(path))            

        if user_message in ['gorila', 'mog', 'Gorila', 'Mog']:
            await message.channel.send(file=discord.File("./src/gorila/gorila.gif"))  
        elif user_message in ['?gorila', '?mog', '?Gorila', '?Mog']:
            await message.author.send(file=discord.File("./src/gorila/gorila.gif"))                       

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)

