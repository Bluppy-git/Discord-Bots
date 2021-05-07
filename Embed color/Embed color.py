import discord
from discord.ext import commands

# ---------------------------------------------------------------------

bot = commands.Bot(command_prefix="!")
bot.remove_command("help")

# ---------------------------------------------------------------------
#Colors:
red = 0xF44336
pink = 0xE91E63
purple = 0x9C27B0
deeppurple = 0x673AB7
indigo = 0x3F51B5
blue = 0x2196F3
lightblue = 0x03A9F4
cyan = 0x00BCD4
teal = 0x009688
green = 0x4CAF50
lightgreen = 0x8BC34A
lime = 0xCDDC39
yellow = 0xFFEB3B
amber = 0xFFC107
orange = 0xFF9800
deeporange = 0xFF5722
brown = 0x795548
grey = 0x9E9E9E
bluegrey = 0x607D8B
black = 0x000000
white = 0xfefefe

# ---------------------------------------------------------------------

#log in Prozess
@bot.event
async def on_ready():
    print('--------------------------------------')
    print('Bot is ready.')
    print('Eingeloggt als')
    print(bot.user.name)
    print(bot.user.id)
    print('Color Bot')
    print('©by Bluppy')
    print('--------------------------------------')

# ---------------------------------------------------------------------

@bot.command(pass_context=True)
async def color(ctx):
    if ctx.author.bot:
        return
    embed = discord.Embed(title="red", color=red)
    await ctx.channel.send(embed=embed)
    embed = discord.Embed(title="pink", color=pink)
    await ctx.channel.send(embed=embed)
    embed = discord.Embed(title="purple", color=purple)
    await ctx.channel.send(embed=embed)
    embed = discord.Embed(title="deeppurple", color=deeppurple)
    await ctx.channel.send(embed=embed)
    embed = discord.Embed(title="indigo", color=indigo)
    await ctx.channel.send(embed=embed)
    embed = discord.Embed(title="blue", color=blue)
    await ctx.channel.send(embed=embed)
    embed = discord.Embed(title="lightblue", color=lightblue)
    await ctx.channel.send(embed=embed)
    embed = discord.Embed(title="cyan", color=cyan)
    await ctx.channel.send(embed=embed)
    embed = discord.Embed(title="teal", color=teal)
    await ctx.channel.send(embed=embed)
    embed = discord.Embed(title="green", color=green)
    await ctx.channel.send(embed=embed)
    embed = discord.Embed(title="lightgreen", color=lightgreen)
    await ctx.channel.send(embed=embed)
    embed = discord.Embed(title="lime", color=lime)
    await ctx.channel.send(embed=embed)
    embed = discord.Embed(title="yellow", color=yellow)
    await ctx.channel.send(embed=embed)
    embed = discord.Embed(title="amber", color=amber)
    await ctx.channel.send(embed=embed)
    embed = discord.Embed(title="orange", color=orange)
    await ctx.channel.send(embed=embed)
    embed = discord.Embed(title="deeporange", color=deeporange)
    await ctx.channel.send(embed=embed)
    embed = discord.Embed(title="brown", color=brown)
    await ctx.channel.send(embed=embed)
    embed = discord.Embed(title="grey", color=grey)
    await ctx.channel.send(embed=embed)
    embed = discord.Embed(title="bluegrey", color=bluegrey)
    await ctx.channel.send(embed=embed)
    embed = discord.Embed(title="black", color=black)
    await ctx.channel.send(embed=embed)

# ---------------------------------------------------------------------

bot.run("")
