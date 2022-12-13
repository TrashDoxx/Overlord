### Библиотеки ###
import discord, config, os
from discord.ext import commands
from dotenv import load_dotenv

bot = commands.Bot(command_prefix = config.PREFIX, intents = discord.Intents.all())

### Подключение .env ###
load_dotenv('.env')

### Подключение бота ###
@bot.event
async def on_ready():
	await bot.change_presence(activity = discord.Activity(name = config.WATCHING_STATUS, type = discord.ActivityType.watching))
	print(f'{bot.user} подключился.')

### Запуск ###
bot.run(os.getenv('TOKEN'))
