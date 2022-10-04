import os
from typing import Union
import base64
import requests
from webserver import runServer
import utils
import discord
from discord.ext import commands
from discord.utils import get

# Creates the bot.
intents = discord.Intents.all()
client = commands.Bot(command_prefix="//", intents=intents)
client.remove_command("help")

# Gets the bot's token.
TOKEN = os.environ.get("TOKEN")

# Required info for Geometry Dash API.
headers = {
	"Content Type": "application/x-www-form-urlencoded",
	"User-Agent": ""
}
mod_level = {"0": "Not a Mod", "1": "Normal", "2": "Elder"}
difficulties = {
	"": {
		"0": "No Difficulty",
		"10": "Easy",
		"20": "Normal",
		"30": "Hard",
		"40": "Harder",
		"50": "Insane"
	},
	"1": {
		"3": "Easy Demon",
		"4": "Medium Demon",
		"0": "Hard Demon",
		"5": "Insane Demon",
		"6": "Extreme Demon"
	}
}
length = {"0": "Tiny", "1": "Short", "2": "Medium", "3": "Long", "4": "XL"}

# Notifier that the bot is online.
@client.event
async def on_connect():
	print(f"Logged on as {client.user}")

# Gives users roles when they react to the message in #roles
@client.event
async def on_raw_reaction_add(payload):
	guild = client.get_guild(payload.guild_id)
	
	if payload.channel_id == 1026867916337074196:
		if payload.message_id == 1026867976739233823:
			if payload.emoji.name == "python":
				python = guild.get_role(1008789957848072272)
				await payload.member.add_roles(python)

			elif payload.emoji.name == "java":
				java = guild.get_role(1008790437743570974)
				await payload.member.add_roles(java)

			elif payload.emoji.name == "cplusplus":
				cpp = guild.get_role(1008794149421584515)
				await payload.member.add_roles(cpp)

			elif payload.emoji.name == "src":
				programming_helper = guild.get_role(1008794453651226756)
				await payload.member.add_roles(programming_helper)

			elif payload.emoji.name == "💻":
				tech_helper = guild.get_role(1008789423443427338)
				await payload.member.add_roles(tech_helper)

	return

@client.event
async def on_raw_reaction_remove(payload):
	guild = client.get_guild(payload.guild_id)
	member = get(guild.members, id=payload.user_id)
	
	if payload.channel_id == 1026867916337074196:
		if payload.message_id == 1026867976739233823:
			if payload.emoji.name == "python":
				python = guild.get_role(1008789957848072272)
				await member.remove_roles(python)

			elif payload.emoji.name == "java":
				java = guild.get_role(1008790437743570974)
				await member.remove_roles(java)

			elif payload.emoji.name == "cplusplus":
				cpp = guild.get_role(1008794149421584515)
				await member.remove_roles(cpp)

			elif payload.emoji.name == "src":
				programming_helper = guild.get_role(1008794453651226756)
				await member.remove_roles(programming_helper)

			elif payload.emoji.name == "💻":
				tech_helper = guild.get_role(1008789423443427338)
				await member.remove_roles(tech_helper)

	return

# General error handler
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
  
		embed.add_field(
			name = "`//gduser <player>`",
			value = "Gets the stats of a Geometry Dash player.",
			inline = False
		)

		embed.add_field(
			name = "`//gdsearch <level> [difficulty]`",
			value = "Searches for a Geometry Dash level. Returns the top 5 results.",
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
	
		elif command == "gduser":
			embed.add_field(
				name = "`//gduser <player>`",
				value = "Gets the stats of a Geometry Dash player. `<player>` can be either a username or an account ID.\n\n__Stats:__\n- Username\n- Stars\n- Diamonds\n- Secret Coins\n- User Coins\n- Demons\n- Creator Points\n- Global Rank\n- Mod Status\n\nExample: *//gduser KryllyxGaming*"
			)

		elif command == "gdsearch":
			embed.add_field(
				name = "`//gdsearch <level> [difficulty]`",
				value = "Searches for a Geometry Dash level. `<level>` can be either a level name or level ID. If the level has a name with spaces, put the level name in quotation marks. You can also provide a specific difficulty.\n\n__Stats:__\n- Name\n- Author\n- Description\n- Difficulty\n- Stars\n- Downloads\n- Likes\n- Length\n- Rating\n- Coins\n- Song\n\n__Difficulties__:\n- any\n- auto\n- easy\n- normal\n- hard\n- harder\n- insane\n- easy_demon\n- medium_demon\n- hard_demon\n- insane_demon\n- extreme_demon\n\nExample: *//gdsearch Bloodbath*",
			)

		else:
			raise commands.BadArgument

	embed.set_footer(text="<> = Required; [] = Optional")

	await ctx.send(embed=embed)

# Error handler for //help
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

# Error handler for //kick
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

# Error handler for //ban
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

# Error handler for //unban
@unban.error
async def unban_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		await ctx.send("You must provide the username with the tag. See `//help unban` for more info.")
		return

	elif isinstance(error, commands.CommandInvokeError):
		await ctx.send("That user either does not exist or has not been banned.")
		return

# Gets the stats for a Discord user
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

# Error handler for //stats
@stats.error
async def stats_error(ctx, error):
	if isinstance(error, commands.MemberNotFound):
		await ctx.send("That user either does not exist or has not been formatted correctly. See `//help stats` for more info.")
		return

# Gets info about a Geometry Dash player
@client.command()
async def gduser(ctx, user):
	try:
		accountID = int(user)
		username = False
	except ValueError:
		username = True
		user_data = {
			"secret": "Wmfd2893gb7",
			"str": user
		}
		user_response = requests.post(
			"http://www.boomlings.com/database/getGJUsers20.php",
			data=user_data,
			headers=headers
		)

		user_values = utils.getValues(user_response.text, "user")

	data = {
		"secret": "Wmfd2893gb7",
		"targetAccountID": user_values["16"] if username else accountID
	}
	response = requests.post(
		"http://www.boomlings.com/database/getGJUserInfo20.php",
		data=data,
		headers=headers
	)

	values = utils.getValues(response.text, "user")

	embed = discord.Embed(
		title = "__**Geometry Dash Player Stats**__",
		description = "*All of the stats for a given Geometry Dash player.*\n------------------------------------------------------------",
		colour = discord.Colour.from_rgb(0,150,90)
	)

	embed.add_field(
		name = "Username:",
		value = values["1"],
		inline = False
	)

	embed.add_field(
		name = "Stars:",
		value = values["3"],
		inline = False
	)

	embed.add_field(
		name = "Diamonds:",
		value = values["46"],
		inline = False
	)

	embed.add_field(
		name = "Secret Coins:",
		value = values["13"],
		inline = False
	)

	embed.add_field(
		name = "User Coins:",
		value = values["17"],
		inline = False
	)

	embed.add_field(
		name = "Demons:",
		value = values["4"],
		inline = False
	)

	embed.add_field(
		name = "Creator Points:",
		value = values["8"],
		inline = False
	)

	embed.add_field(
		name = "Global Rank:",
		value = values["30"],
		inline = False
	)

	mod_index = values["49"]

	embed.add_field(
		name = "Mod Level:",
		value = mod_level[str(mod_index)],
		inline = False
	)

	embed.set_footer(text="Account ID: " + values["16"])

	await ctx.send(embed=embed)
	return

# Error handler for //gduser
@gduser.error
async def gduser_error(ctx, error):
	if isinstance(error, commands.CommandInvokeError):
		await ctx.send("That user does not exist.")
		return

# Searches for a Geometry Dash level
@client.command()
async def gdsearch(ctx, level, difficulty="any"):
	data = {
		"secret": "Wmfd2893gb7",
		"count": 5,
		"type": 0,
		"str": level
	}

	if difficulty == "any":
		pass
	elif difficulty == "auto":
		data["diff"] = -3
	elif difficulty == "easy":
		data["diff"] = 1
	elif difficulty == "normal":
		data["diff"] = 2
	elif difficulty == "hard":
		data["diff"] = 3
	elif difficulty == "harder":
		data["diff"] = 4
	elif difficulty == "insane":
		data["diff"] = 5
	elif difficulty == "demon":
		data["diff"] = -2
	elif difficulty == "easy_demon":
		data["diff"] = -2
		data["demonFilter"] = 1
	elif difficulty == "medium_demon":
		data["diff"] = -2
		data["demonFilter"] = 2
	elif difficulty == "hard_demon":
		data["diff"] = -2
		data["demonFilter"] = 3
	elif difficulty == "insane_demon":
		data["diff"] = -2
		data["demonFilter"] = 4
	elif difficulty == "extreme_demon":
		data["diff"] = -2
		data["demonFilter"] = 5
	else:
		raise commands.BadArgument

	response = requests.post(
		"http://www.boomlings.com/database/getGJLevels21.php",
		data=data,
		headers=headers
	)

	values, creators = utils.getValues(response.text, "levels")

	i = 0
	for level in values:
		data["str"] = str(level["1"])
		
		response = requests.post(
			"http://www.boomlings.com/database/getGJLevels21.php",
			data=data,
			headers=headers
		)

		level_info, song = utils.getValues(response.text, "level")
		
		embed = discord.Embed(
			title = "**" + level_info["2"] + "**",
			description = "*By " + creators[i] + "*\n------------------------------------------------------------",
			colour = discord.Colour.from_rgb(0,150,90)
		)

		embed.add_field(
			name = "Description:",
			value = base64.urlsafe_b64decode(level_info["3"].encode()).decode(),
			inline = False
		)

		if level_info["17"] == "1":
			levelDifficulty = difficulties[level_info["17"]][level_info["43"]]
		else:
			if level_info["25"] == "1":
				levelDifficulty == "Auto"
			else:
				levelDifficulty = difficulties[level_info["17"]][level_info["9"]]

		embed.add_field(
			name = "Difficulty:",
			value = levelDifficulty,
			inline = False
		)

		embed.add_field(
			name = "Stars:",
			value = level_info["18"],
			inline = False
		)

		embed.add_field(
			name = "Downloads:",
			value = level_info["10"],
			inline = False
		)

		embed.add_field(
			name = "Likes:",
			value = level_info["14"],
			inline = False
		)

		embed.add_field(
			name = "Length:",
			value = length[level_info["15"]],
			inline = False
		)

		if int(level_info["19"]) > 0:
			rating = "Featured"
		else:
			if level_info["42"] == "1":
				rating = "Epic"
			else:
				rating = "None"

		embed.add_field(
			name = "Rating:",
			value = rating,
			inline = False
		)

		embed.add_field(
			name = "Coins:",
			value = level_info["37"],
			inline = False
		)

		embed.add_field(
			name = "Song:",
			value = "*" + song["2"] + "* by " + song["4"],
			inline = False
		)

		embed.set_footer(text="Level ID: " + level_info["1"] + "\nSong ID: " + song["1"])

		await ctx.send(embed=embed)

		i += 1

# Error handler for //gdsearch
@gdsearch.error
async def gdsearch_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		await ctx.send("Invalid level difficulty.")
	
# Starts the bot.
# runServer()
client.run(TOKEN)