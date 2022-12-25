### Библиотеки ###
import discord
from discord.ext import commands

### Подключение модуля ###
class Error(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	### Сообщения об ошибках для пользователей ###
	@commands.Cog.listener()
	async def on_application_command_error(self, ctx: discord.ApplicationContext, error: discord.DiscordException):
		if isinstance(error, commands.MissingPermissions):
			await ctx.respond(embed = discord.Embed(description = '**Недостаточно прав для использования!** 🤖', color = discord.Colour.red()))
		elif isinstance(error, commands.UserInputError):
			await ctx.respond(embed = discord.Embed(description = '**Неверно указан один из аргументов!** 🤖', color = discord.Colour.red()))
		elif isinstance(error, commands.NotOwner):
			await ctx.respond(embed = discord.Embed(description = '**Доступно лишь моему владельцу!** 🤖', color = discord.Colour.red()))
		else:
			await ctx.respond(embed = discord.Embed(description = '**Что-то пошло не так!** 🤖', color = discord.Colour.red()))
			raise error

	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.reply(embed = discord.Embed(description = '**Недостаточно прав для использования!** 🤖', color = discord.Colour.red()))
		elif isinstance(error, commands.UserInputError):
			await ctx.reply(embed = discord.Embed(description = '**Неверно указан один из аргументов!** 🤖', color = discord.Colour.red()))
		elif isinstance(error, commands.NotOwner):
			await ctx.reply(embed = discord.Embed(description = '**Доступно лишь моему владельцу!** 🤖', color = discord.Colour.red()))
		elif isinstance(error, commands.CommandNotFound):
			await ctx.reply(embed = discord.Embed(description = '**Такая команда не найдена!** 🤖', color = discord.Colour.red()))
		else:
			await ctx.reply(embed = discord.Embed(description = '**Что-то пошло не так!** 🤖', color = discord.Colour.red()))
			raise error

def setup(bot):
	bot.add_cog(Error(bot))
