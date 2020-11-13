from discord.ext import commands
import os
import json
import asyncio
import discord

if os.path.isfile("channels.json"):
    with open('channels.json', encoding='utf-8') as f:
        channels = json.load(f)
else:
    channels = {}
    with open('channels.json', 'w') as f:
        json.dump(channels, f, indent=4)

bot = commands.Bot(command_prefix="v!")
botcolor = 0xffffff

bot.remove_command("help")

# ---------------------------------------------------------------------


tempchannels = []
admins = []
# if ctx.author.id in admins:

# ---------------------------------------------------------------------

@bot.command(pass_context=True)
async def addtempchannel(ctx, channelid):
    if ctx.author.bot:
        return
    if ctx.author.guild_permissions.administrator:
        if channelid:
            for vc in ctx.guild.voice_channels:
                if vc.id == int(channelid):
                    if str(ctx.channel.guild.id) not in channels:
                        channels[str(ctx.channel.guild.id)] = []
                    channels[str(ctx.channel.guild.id)].append(int(channelid))
                    with open('channels.json', 'w') as f:
                        json.dump(channels, f, indent=4)
                    embed = discord.Embed(title='{} ist nun ein JoinHub'.format(vc.name),
                                          description = "",
                                          color=0xfefefe)
                    await ctx.channel.send(embed=embed)
                    return
            embed = discord.Embed (title= "{} ist kein Voicechannel".format(channelid),
                                   description = "",
                                   colour = 0xfefefe)
            await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(title="Bitte gebe eine ChannelID an",
                                  description="",
                                  colour=0xfefefe)
            await ctx.channel.send(embed=embed)
    else:
        embed = discord.Embed(title="Du brauchst das Recht Administrator um das zu tun",
                              description="",
                              colour=0xfefefe)
        await ctx.channel.send(embed=embed)


@bot.command(pass_context=True)
async def removetempchannel(ctx, channelid):
    if ctx.author.bot:
        return
    if ctx.author.guild_permissions.administrator:
        if channelid:
            guildS = str(ctx.channel.guild.id)
            channelidI = int(channelid)
            for vc in ctx.guild.voice_channels:
                if vc.id == int(channelid):
                    if channels[guildS]:
                        if channelidI in channels[guildS]:
                            channels[guildS].remove(channelidI)
                            with open('channels.json', 'w') as f:
                                json.dump(channels, f, indent=4)
                                embed = discord.Embed(title="{} ist kein JoinHub mehr".format(vc.name),
                                                      description="",
                                                      colour=0xfefefe)
                                await ctx.channel.send(embed=embed)
                                return
                        else:
                            embed = discord.Embed(title="Dieser Channel existiert hier nicht",
                                                  description="",
                                                  colour=0xfefefe)
                            await ctx.channel.send(embed=embed)
                            return
            embed = discord.Embed(title="Du besitzt noch keine JoinHubs",
                                  description="",
                                  colour=0xfefefe)
            await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(title="Keine Channelid angegeben",
                                  description="",
                                  colour=0xfefefe)
            await ctx.channel.send(embed=embed)
    else:
        embed = discord.Embed(title="Du brauchst das Recht Administrator um das zu tun",
                              description="",
                              colour=0xfefefe)
        await ctx.channel.send(embed=embed)


@bot.command(pass_context=True)
async def info(ctx):
    if ctx.author.bot:
        return
    membercount = 0
    guildcount = 0
    for guild in bot.guilds:
        membercount += guild.member_count
        guildcount += 1
    embed = discord.Embed(title='Informationen', description=f'Der Bot ist derzeit auf {guildcount-1} anderen '
                                                                 f'Servern und sieht {membercount} Members.',
                            color=0xfefefe)
    await ctx.channel.send(embed=embed)


#help command

@bot.command(pass_context=True)
async def help(ctx):
    if ctx.author.bot:
        return
    embed = discord.Embed(title='Befehle für die Tempchannel', description=f'v!addtempchannel <channelid> - '
                                                                           f'Fügt den Channel als Tempchannel hinzu.\r\n'
                                                                           f'v!removetempchannel <channelid> - '
                                                                           f'Entfernt den Tempchannel.\r\n'
                                                                           f'v!botinfo - zeigt dir die Information für den Temp Voice an.\r\n'
                                                                           f'v!links - schickt Links des Temp Voice.\r\n'
                                                                           f'v!info - Zeigt allgemeine Statistiken.\r\n'
                                                                           f'\r\n'
                                                                           f'Besuche den [Entwickler Discord](https://discord.gg/PwtCQzn)',
                              color=0xfefefe)
    if ctx.author.guild_permissions.administrator:
        embed.add_field(name='Adminbefehle', value='v!leave <guildid> - Der Bot leaved von der Guild.', inline=False)
    await ctx.channel.send(embed=embed)


@bot.command(pass_context=True)
async def leave(ctx, serverid):
    if ctx.author.bot:
        return
    if ctx.author.guild_permissions.administrator:
        guild = bot.get_guild(serverid)
        if guild:
            embed = discord.Embed(title=f'{guild.name} geleaved.',
                                  description="",
                                  colour=0xfefefe)
            await ctx.channel.send(embed=embed)
            await guild.leave()
        else:
            embed = discord.Embed(title=f'Keine Guild mit der ID {serverid} gefunden.',
                                  description="",
                                  colour=0xfefefe)
            await ctx.channel.send(embed=embed)


# Bot info command
@bot.command(pass_context=True)
async def botinfo(ctx):
    if ctx.author.bot:
        return
    embed = discord.Embed(title="Der Temp Voice:",
                          description='''> Der Temp Voice Bot eröffnet einen neuen Sprachkanal,
                                  > sobald du auf einen als Join Channel abgespeicherten Sprachkanal klickst.
                                  > Dann wird ein Neuer Sprachkanal eröffnet, indem du dich bequem mit anderen Usern unterhalten kannst.
                                  > Sobald alle User den Chanel verlassen haben, wird der Sprachkanal wieder gelöscht 
                                  > Und das Beste: Wenn du mit dem Bot einen Channel erstellst, kannst du den Channel beliebig 
                                  > einstellen (Name, Benutzerlimit etc.)

                                  Besuche den [Entwickler Discord](https://discord.gg/PwtCQzn)''',
                          color=0xfefefe)
    await ctx.channel.send(embed=embed)


#link command
@bot.command(pass_context=True)
async def links(ctx):
    if ctx.author.bot:
        return
    embed = discord.Embed(title="🔗 Links'", color=0xfefefe)
    embed.add_field(inline=True, name='Entwickler Discord', value='[click here](https://discord.gg/PwtCQzn)')
    embed.add_field(inline=True, name='Invite me', value='[click here](https://discord.com/oauth2/authorize?client_id=745923048510849054&scope=bot&permissions=8)')
    embed.add_field(inline=True, name='Source code', value='[click here](https://github.com/Bluppy-git/Discord-Bots)')
    await ctx.channel.send(embed=embed)

# ---------------------------------------------------------------------

@bot.event
async def on_ready():
    print('--------------------------------------')
    print('Bot is ready.')
    print('Eingeloggt als')
    print(bot.user.name)
    print(bot.user.id)
    print('VoiceTEMP')
    print('©by Bluppy')
    print('--------------------------------------')
    bot.loop.create_task(status_task())


async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game('Hilfe » v!help'), status=discord.Status.online)
        await asyncio.sleep(20)
        await bot.change_presence(activity=discord.Game(bot.user.name), status=discord.Status.online)
        await asyncio.sleep(20)
        await bot.change_presence(activity=discord.Game('Developer Discord: https://discord.gg/PwtCQzn'), status=discord.Status.online)
        await asyncio.sleep(20)
        await bot.change_presence(activity=discord.Game('Developer: Bluppy'), status=discord.Status.online)
        await asyncio.sleep(20)



@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel:
        if isTempChannel(before.channel):
            bchan = before.channel
            if len(bchan.members) == 0:
                await bchan.delete(reason="No member in tempchannel")
    if after.channel:
        if isJoinHub(after.channel):
            overwrite = discord.PermissionOverwrite()
            overwrite.manage_channels = True
            overwrite.move_members = True
            name = "│⏳ {}".format(member.name)
            output = await after.channel.clone(name=name, reason="Joined in joinhub")
            if output:
                tempchannels.append(output.id)
                await output.set_permissions(member, overwrite=overwrite)
                await member.move_to(output, reason="Created tempvoice")


# ---------------------------------------------------------------------

async def getChannel(guild, name):
    for channel in guild.voice_channels:
        if name in channel.name:
            return channel
    return None


def isJoinHub(channel):
    if channels[str(channel.guild.id)]:
        if channel.id in channels[str(channel.guild.id)]:
            return True
    return False


def isTempChannel(channel):
    if channel.id in tempchannels:
        return True
    else:
        return False

# ---------------------------------------------------------------------

bot.run("")
