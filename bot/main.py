import os
import random
from datetime import datetime
import discord
from discord.ext import commands
import json
import requests
bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

txt = requests.get("https://raw.githubusercontent.com/AsianIncest/discord-py-heroku/master/bot/fillter.txt").text

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
async def ping(ctx):
    if ctx.message.author == bot.user:
        return
    await ctx.message.delete()
    await ctx.send("Привет медвед!")

@bot.command()
async def fox(ctx):
    if ctx.message.author == bot.user:
        return
    await ctx.message.delete()
    response = requests.get('https://some-random-api.ml/img/fox')
    json_data = json.loads(response.text)
    embed = discord.Embed(color=0xff9900, title='Рандомная лисичка')
    embed.set_image(url=json_data['link'])
    await  ctx.send(embed=embed)

@bot.command()
async def mat(ctx):
    if ctx.message.author == bot.user:
        return
    await ctx.message.delete()
    author = ctx.message.author.mention
    #    fillter = open("fillter.txt", "r", encoding="utf-8")
    #    txt = fillter.read()
    txt_list = txt.split(", ")
    mat = txt_list[random.randint(0, len(txt_list) - 1)]
    await ctx.send(f"{author}, твоё слово: {mat}")

@bot.command()
async def cls(ctx):
    if ctx.message.author == bot.user:
        return
    await ctx.channel.purge(limit=None)

@bot.command()
async def git(ctx):
    if ctx.message.author == bot.user:
        return
    await ctx.send("Мой Git https://github.com/AsianIncest/discord-py-heroku")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    print(f"{message.author} {datetime.now()} {message.channel}# {message.content}")
    await bot.process_commands(message)


if __name__ == "__main__":
    bot.run(TOKEN)
