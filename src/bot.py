import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Creates the bot.
client = commands.Bot(command_prefix="//")
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
			value = "Kicks the given user (formatted as a mention).",
			inline = False
		)
	
		embed.add_field(
			name = "`//ban <user> [reason]`",
			value = "Bans the given user (formatted as a mention).",
			inline = False
		)
	
		embed.add_field(
			name = "`//unban <user>`",
			value = "Unbans the given user (formatted as the username with the tag).",
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
				value = "Kicks the given user. The `<user>` parameter must be a mention/ping.\n\nExample: *//kick* <@960253793063301120> *example use*"
			)

		elif command == "ban":
			embed.add_field(
				name = "`//ban <user> [reason]`",
				value = "Bans the given user. The `<user>` parameter must be a mention/ping.\n\nExample: *//ban* <@960253793063301120> *example use*"
			)

		elif command == "unban":
			embed.add_field(
				name = "`//unban <user>`",
				value = "Unbans the given user. The `<user>` parameter must be the username followed by the tag.\n\nExample: *//unban TheFakeKryllyx#0000*"
			)

	embed.set_footer(text="<> = Required; [] = Optional")

	await ctx.send(embed=embed)

# Kicks the given user.
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason):
	await user.kick(reason=reason)
	await ctx.send(f"User \"{user}\" has been kicked.\nReason: {reason}")
	return

# Bans the given user.
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason):
	await user.ban(reason=reason)
	await ctx.send(f"User \"{user}\" has been banned.\nReason: {reason}")
	return

# Unbans the given user.
@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, user):
	banned = await ctx.guild.bans()
	username, tag = user.split("#")

	for ban in banned:
		usr = ban.user
		if (usr.name, usr.discriminator) == (username, tag):
			await ctx.guild.unban(usr)
			await ctx.send(f"User \"{usr}\" has been unbanned.")
	
	return

# Starts the bot.
client.run(TOKEN)