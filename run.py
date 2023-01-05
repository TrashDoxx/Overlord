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

### Подключение модулей ###
@bot.command
@commands.is_owner()
async def load(extension):
	bot.load_extension(f'cogs.{extension}')
	print(f'Модуль {extension} подключён.')

### Перезагрузка модулей ###
@bot.command
@commands.is_owner()
async def reload(extension):
	bot.reload_extension(f'cogs.{extension}')
	print(f'Модуль {extension} перезагружен.')

### Отключение модулей ###
@bot.command
@commands.is_owner()
async def unload(extension):
	bot.unload_extension(f'cogs.{extension}')
	print(f'Модуль {extension} отключён.')

### Загрузка модулей по-умолчанию ###
for filename in os.listdir('cogs'):
	if filename.endswith('py'):
		bot.load_extension(f'cogs.{filename[:-3]}')

### Запуск ###
bot.run(os.getenv('TOKEN'))
