### Библиотеки ###
import discord, datetime, os
from discord.ext import commands
from discord import Option

### Подключение модуля ###
class Moderation(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	### Кик ###
	@commands.has_permissions(kick_members = True)
	@commands.slash_command(description = 'Выгнать свинью')
	async def kick(self, ctx, user: Option(discord.Member, description = 'Кличка свиньи', required = True), reason: Option(str, description = 'Причина изгнания', required = True)):
		channel = self.bot.get_channel(int(os.getenv('LOG_CHANNEL_ID')))
		embed = discord.Embed(title = 'Свинья депортирована!', color = discord.Colour.red(), timestamp = datetime.datetime.now())
		embed.set_thumbnail(url = 'https://raw.githubusercontent.com/TrashDoxx/Overlord/master/images/overlord-logo.png')
		embed.add_field(name = 'Администратор', value = f'{ctx.author.mention}', inline = True)
		embed.add_field(name = 'Осужденный', value = f'{user.mention}', inline = True)
		embed.add_field(name = 'Причина', value = f'**{reason}**', inline = False)
		await ctx.respond(embed = discord.Embed(description = '**Исполнено, червь!** 🤖', color = discord.Colour.dark_blue()))
		await channel.send(embed = embed)
		await user.kick(reason = reason)

	### Свинка ###
	@commands.has_permissions(administrator = True)
	@commands.slash_command(description = 'Отправить в свинолуфку')
	async def pig(self, ctx, user: Option(discord.Member, description = 'Кличка свиньи', required = True), reason: Option(str, description = 'Причина изгнания', required = True)):
		channel = self.bot.get_channel(int(os.getenv('LOG_CHANNEL_ID')))
		role = user.guild.get_role(int(os.getenv('MUTE_ROLE_ID')))
		embed = discord.Embed(title = 'Свинья арестована!', color = discord.Colour.red(), timestamp = datetime.datetime.now())
		embed.set_thumbnail(url = 'https://raw.githubusercontent.com/TrashDoxx/Overlord/master/images/overlord-logo.png')
		embed.add_field(name = 'Администратор', value = f'{ctx.author.mention}', inline = True)
		embed.add_field(name = 'Осужденный', value = f'{user.mention}', inline = True)
		embed.add_field(name = 'Причина', value = f'**{reason}**', inline = False)
		await ctx.respond(embed = discord.Embed(description = '**Исполнено, червь!** 🤖', color = discord.Colour.dark_blue()))
		await channel.send(embed = embed)
		await user.add_roles(role)

	### Не-свинка ###
	@commands.has_permissions(administrator = True)
	@commands.slash_command(description = 'Вернуть из свинолуфки')
	async def unpig(self, ctx, user: Option(discord.Member, description = 'Кличка свиньи', required = True)):
		channel = self.bot.get_channel(int(os.getenv('LOG_CHANNEL_ID')))
		role = user.guild.get_role(int(os.getenv('MUTE_ROLE_ID')))
		embed = discord.Embed(title = 'Свинья помилована!', color = discord.Colour.green(), timestamp = datetime.datetime.now())
		embed.set_thumbnail(url = 'https://raw.githubusercontent.com/TrashDoxx/Overlord/master/images/overlord-logo.png')
		embed.add_field(name = 'Администратор', value = f'{ctx.author.mention}', inline = True)
		embed.add_field(name = 'Помилованный', value = f'{user.mention}', inline = True)
		await ctx.respond(embed = discord.Embed(description = '**Исполнено, червь!** 🤖', color = discord.Colour.dark_blue()))
		await channel.send(embed = embed)
		await user.remove_roles(role)

	### Бан ###
	@commands.has_permissions(ban_members = True)
	@commands.slash_command(description = 'Отправить в свинячий рай')
	async def ban(self, ctx, user: Option(discord.Member, description = 'Кличка свиньи', required = True), reason: Option(str, description = 'Причина блокировки', required = True)):
		channel = self.bot.get_channel(int(os.getenv('LOG_CHANNEL_ID')))
		embed = discord.Embed(title = 'Свинья уничтожена!', color = discord.Colour.red(), timestamp = datetime.datetime.now())
		embed.set_thumbnail(url = 'https://raw.githubusercontent.com/TrashDoxx/Overlord/master/images/overlord-logo.png')
		embed.add_field(name = 'Администратор', value = f'{ctx.author.mention}', inline = True)
		embed.add_field(name = 'Осужденный', value = f'{user.mention}', inline = True)
		embed.add_field(name = 'Причина', value = f'**{reason}**', inline = False)
		await ctx.respond(embed = discord.Embed(description = '**Исполнено, червь!** 🤖', color = discord.Colour.dark_blue()))
		await channel.send(embed = embed)
		await user.ban(reason = reason)

def setup(bot):
	bot.add_cog(Moderation(bot))
