import discord
import responses
import os
import random
import requests
import datetime
from dotenv import load_dotenv
import button_paginator as pg

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
    async def page(embeds, ctx):
        paginator = pg.Paginator(client, embeds, ctx)
        paginator.add_button('prev', emoji='◀')
        paginator.add_button('delete', label='Close', emoji='⏹')
        paginator.add_button('next', emoji='▶')
        await paginator.start()

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} je reku: '{user_message}' ({channel})")

        if user_message == '/assets':
            url = "https://api.coincap.io/v2/assets"
            data = requests.get(url).json()
            assets = []
            for asset in data['data']:
                embeded = discord.Embed(title='Cryptocurrencies', color=0x0000ff, timestamp=datetime.datetime.now(datetime.UTC))
                for x in asset:
                    if x in ['supply', 'maxSupply', 'marketCapUsd']:
                        embeded.add_field(name=x, inline=True, value=round(float(asset[x]))) if x == 'maxSupply' and asset[x] is not None else embeded.add_field(name=x, inline=True, value='Not defined')
                    elif x in ['priceUsd', 'vwap24Hr', 'volumeUsd24Hr']:
                        embeded.add_field(name=x, inline=True, value=round(float(asset[x]), 5))
                    elif x in ['changePercent24Hr']:
                        embeded.add_field(name=x, inline=True, value=str(round(float(asset[x]), 2)) + ' 🔻') if float(asset[x]) < 0 else embeded.add_field(name=x, inline=True, value=str(round(float(asset[x]), 2)) + ' 🟩')
                    else:
                        embeded.add_field(name=x, inline=True, value=asset[x])
                embeded.set_footer(text=f'Replying to {message.author}', icon_url=message.author.avatar.url)
                assets.append(embeded)
            await page(assets, message.channel)

        if user_message[0:6] == '/stats':
            ticker = user_message[7:]
            url = 'https://api.coincap.io/v2/assets?search=' + ticker
            data = requests.get(url).json()
            embeded = discord.Embed(title='' + ticker + ' stats', color=0x0000ff, timestamp=datetime.datetime.now(datetime.UTC))
            for x in data['data'][0]:
                if x in ['supply', 'maxSupply', 'marketCapUsd']:
                    embeded.add_field(name=x, inline=True, value=round(float(data['data'][0][x])))
                elif x in ['priceUsd', 'vwap24Hr', 'volumeUsd24Hr']:
                    embeded.add_field(name=x, inline=True, value=round(float(data['data'][0][x]), 5))
                elif x in ['changePercent24Hr']:
                    embeded.add_field(name=x, inline=True, value=str(round(float(data['data'][0][x]), 2)) + ' 🔻') if float(data['data'][0][x]) < 0 else embeded.add_field(name=x, inline=True, value=str(round(float(data['data'][0][x]), 2)) + ' 🟩')
                else:
                    embeded.add_field(name=x, inline=True, value=data['data'][0][x])
            embeded.set_footer(text=f'Replying to {message.author}', icon_url=message.author.avatar.url)
            await message.channel.send(embed=embeded)

        if user_message[0:8] == '/markets':
            tmp_ticker = user_message[9:]
            tmp_url = 'https://api.coincap.io/v2/assets?search=' + tmp_ticker
            tmp_data = requests.get(tmp_url).json()
            ticker = tmp_data['data'][0]['id']
            url = 'https://api.coincap.io/v2/assets/' + ticker + '/markets'
            data = requests.get(url).json()
            markets = []
            markets_per_page = 6
            pages = [data['data'][i:i + markets_per_page] for i in range(0, len(data['data']), markets_per_page)]
            for p in pages:
                embeded = discord.Embed(title='Markets for ' + ticker, color=0x0000ff, timestamp=datetime.datetime.now(datetime.UTC))
                for market in p:
                    embeded.add_field(name=market['exchangeId'], inline=False, value=f"{market['baseSymbol']}/{market['quoteSymbol']}, {round(float(market['priceUsd']), 5)}$, {round(float(market['volumePercent']), 2)}%")
                embeded.set_footer(text=f'Replying to {message.author}', icon_url=message.author.avatar.url)
                markets.append(embeded)
            await page(markets, message.channel)

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

