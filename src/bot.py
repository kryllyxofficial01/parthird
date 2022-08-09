import os
from dotenv import load_dotenv
from typing import Union
import discord
from discord.ext import commands

# Creates the bot.
intents = discord.Intents.all()
client = commands.Bot(command_prefix="//", intents=intents)
client.remove_command("help")

# Gets the bot's token.
load_dotenv("src/.env")
TOKEN = os.getenv("TOKEN")

# Notifier that the bot is online.
@client.event
async def on_ready():
	print(f"Logged on as {client.user}")

# Check for errors.
@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.send("You don't permission to use that command.")
		return

# Help command
@client.command()
async def help(ctx, command=None):
	if command == None:
		embed = discord.Embed(
			title = "__**Parthird Help**__",
			description = "*List of all the commands Parthird has to offer.*\n---------------------------------------------------------------------------------------------------",
			colour = discord.Colour.from_rgb(0,150,90)
		)
	
		embed.add_field(
			name = "`//help [command]`",
			value = "Shows this message. If a command is specified, it gives a more in-depth explanantion.",
			inline = False
		)
		
		embed.add_field(
			name = "`//kick <user> [reason]`",
			value = "Kicks the given user.",
			inline = False
		)
	
		embed.add_field(
			name = "`//ban <user> [reason]`",
			value = "Bans the given user.",
			inline = False
		)
	
		embed.add_field(
			name = "`//unban <user>`",
			value = "Unbans the given user.",
			inline = False
		)

		
		embed.add_field(
			name = "`//stats <user>`",
			value = "Gets the technical details of a user.",
			inline = False
		)


	else:
		embed = discord.Embed(
			title = "__**Parthird Help**__",
			colour = discord.Colour.from_rgb(0,150,90)
		)

		if command == "help":
			embed.add_field(
				name = "`//help [command]`",
				value = "Shows a list of all commands. If a command is specified, then a more detailed message about the command will show.\n\nExample: *//help kick*"
			)
		
		elif command == "kick":
			embed.add_field(
				name = "`//kick <user> [reason]`",
				value = "Kicks the given user. The `<user>` parameter must be a mention or a user ID.\n\nExample: *//kick* <@960253793063301120> *example use*"
			)

		elif command == "ban":
			embed.add_field(
				name = "`//ban <user> [reason]`",
				value = "Bans the given user. The `<user>` parameter must be a mention or a user ID.\n\nExample: *//ban* <@960253793063301120> *example use*"
			)

		elif command == "unban":
			embed.add_field(
				name = "`//unban <user>`",
				value = "Unbans the given user. The `<user>` parameter must be the username followed by the tag.\n\nExample: *//unban TheFakeKryllyx#0000*"
			)

		elif command == "stats":
			embed.add_field(
				name = "`//stats <user>`",
				value = "Gets the technical details of the given user.\n\n__Details:__\n- Username\n- Tag\n- User ID\n- Nickname\n- Status\n- Roles\n- Date Joined\n\nThe `<user>` parameter must be a mention or a user ID.\n\nExample: *//stats* <@960253793063301120>"
			)

		else:
			raise commands.BadArgument

	embed.set_footer(text="<> = Required; [] = Optional")

	await ctx.send(embed=embed)

@help.error
async def help_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		await ctx.send("That command either does not exist or has been formatted incorrectly.")
		return

# Kicks the given user.
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: Union[discord.Member, int], *, reason=""):
	if isinstance(user, int):
		user = client.get_user(user)
	
	if reason:
		await user.kick(reason=reason)
		await ctx.send(f"User \"{user}\" has been kicked.\nReason: {reason}")
	else:
		await user.kick()
		await ctx.send(f"User \"{user}\" has been kicked.")

	return

# Errors raised by the kick command will be handled here.
@kick.error
async def kick_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		await ctx.send("That user either does not exist or the username has not been formatted correctly. See `//help kick` for more info.")
		return

# Bans the given user.
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: Union[discord.Member, int], *, reason=""):
	if isinstance(user, int):
		user = client.get_user(user)
	
	if reason:
		await user.ban(reason=reason)
		await ctx.send(f"User \"{user}\" has been banned.\nReason: {reason}")
	else:
		await user.ban()
		await ctx.send(f"User \"{user}\" has been banned.")

	return

# Errors raised by the ban command will be handled here.
@ban.error
async def ban_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		await ctx.send("That user either does not exist or the username has not been formatted correctly. See `//help ban` for more info.")
		return

# Unbans the given user.
@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, user):
	banned = await ctx.guild.bans()

	if "#" in user:
		i = 0
		for ban in banned:
			usr = ban.user

			ban_name = f"{usr.name}#{usr.discriminator}"
			banned[i] = ban_name

		i = 0
		while True:
			if banned[i] == user:
				await ctx.guild.unban(usr)
				await ctx.send(f"User \"{usr}\" has been unbanned.")
				return
				
			else:
				i += 1

	else:
		raise commands.BadArgument
	
	return

# Errors raised by the unban command will be handled here.
@unban.error
async def unban_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		await ctx.send("You must provide the username with the tag. See `//help unban` for more info.")
		return

	elif isinstance(error, commands.CommandInvokeError):
		await ctx.send("That user either does not exist or has not been banned.")
		return

# Stats command
@client.command()
async def stats(ctx, user: Union[discord.Member, int]):
	if isinstance(user, int):
		user = client.get_user(user)

	embed = discord.Embed(
		title = "__**User Stats**__",
		description = "*All of the technical information of a given user.*\n------------------------------------------------------------",
		colour = discord.Colour.from_rgb(0,150,90)
	)

	roles = ""
	for role in user.roles:
		roles += role.name + ", "

	embed.add_field(
		name = "Username:",
		value = user.name,
		inline = False
	)

	embed.add_field(
		name = "Tag:",
		value = user.discriminator,
		inline = False
	)

	embed.add_field(
		name = "User ID:",
		value = user.id,
		inline = False
	)

	embed.add_field(
		name = "Nickname:",
		value = user.nick if user.nick != None else "No nickname",
		inline = False
	)

	embed.add_field(
		name = "Status:",
		value = user.status,
		inline = False
	)

	embed.add_field(
		name = "Roles:",
		value = roles.strip(", "),
		inline = False
	)

	time = user.joined_at.strftime("%H:%M:%S %p on %A, %B %d, %Y")
	embed.set_footer(text=f"Joined: {time}")

	await ctx.send(embed=embed)
	return

# Stats error handler
@stats.error
async def stats_error(ctx, error):
	if isinstance(error, commands.MemberNotFound):
		await ctx.send("That user either does not exist or has not been formatted correctly. See `//help stats` for more info.")
		return

# Starts the bot.
client.run(TOKEN)
