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

@client.command()
async def help(ctx, command=None):
    embed = discord.Embed(
		title="Parthird Help",
		description="test",
		colour=discord.Colour.dark_gray()
	)
        
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