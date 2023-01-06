### Библиотеки ###
import discord, requests, random
from discord.ext import commands
from discord import option

### Подключение модуля ###
class Misc(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	### Сообщения ###
	@commands.command()
	@commands.has_permissions(administrator = True)
	async def say(self, ctx, channel: discord.TextChannel, *, message):
		if message == None:
			await ctx.reply('Введи сообщение.')
			return
		await channel.send(message)

	### Порядочные анимешки ###
	@commands.slash_command(description = 'Взглянуть на милую картинку')
	@option('category', description = 'Выберите категорию', choices = ['waifu', 'neko', 'megumin'])
	async def sfw(self, ctx, category):
		response = requests.get(f'https://api.waifu.pics/sfw/{category}')
		image = response.json()['url']
		await ctx.respond(image)

	### Непорядочные анимешки ###
	@commands.dm_only()
	@commands.slash_command(description = 'Взглянуть на эротическую картинку')
	@option('category', description = 'Выберите категорию', choices = ['waifu', 'neko', 'trap'])
	async def nsfw(self, ctx, category):
		response = requests.get(f'https://api.waifu.pics/nsfw/{category}')
		image = response.json()['url']
		await ctx.respond(image)

	### Монетка ###
	@commands.slash_command(description = 'Обмануть судьбу')
	async def coin(self, ctx):
		value = random.randint(0, 1)
		if value == 0:
			await ctx.respond(embed = discord.Embed(description = 'Выпала **решка**! 🪙', color = discord.Colour.green()))
		else:
			await ctx.respond(embed = discord.Embed(description = 'Выпал **орёл**! 🪙', color = discord.Colour.green()))

def setup(bot):
	bot.add_cog(Misc(bot))
