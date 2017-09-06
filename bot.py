import discord
import asyncio
from discord.ext import commands
from modules import games
from modules import music
import config

description = 'Discord bot to manage one\'s discord server.'

bot = commands.Bot(command_prefix = commands.when_mentioned_or('!'),
                   description = description,
                   owner_id = config.OWNER_ID,
                   pm_help = True)

@bot.event
async def on_ready():
    print('Logged in as: ' + bot.user.name)
    print('Id: ' + bot.user.id)
    print('Using discord version: ' + discord.__version__)
    print('----------------------------')
    print('To add ' + bot.user.name + ' to your server use: ')
    print(discord.utils.oauth_url(bot.user.id))

    await bot.change_presence(game = discord.Game(name = '!help'))

bot.add_cog(music.Music(bot))

bot.run(config.TOKEN)
