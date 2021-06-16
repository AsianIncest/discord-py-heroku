import os

import discord
from discord.ext import commands
import json
import requests
bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
async def ping(ctx):
    await ctx.send("Привет медвед!")

@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox')
    json_data = json.loads(response.text)
    embed = discord.Embed(color=0xff9900, title='Рандомная лисичка')
    embed.set_image(url=json_data['link'])
    await  ctx.send(embed=embed)

if __name__ == "__main__":
    bot.run(TOKEN)
