import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="$") #Prefixの設定

@bot.event
async def on_ready():
    print("起動しました。")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run("Njc3ODM5MTUyODg0MjE5OTE1.XkaFZQ.4A3AozQP9e_mvUwU65qo4Hf5CbQ")