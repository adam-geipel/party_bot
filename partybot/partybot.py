import os
import discord
import discord.ext
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.all()

bot = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(bot)

@bot.event
async def on_ready():
	# Syncs the command tree with the guild(s)	
	await tree.sync()

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	print("Party Bot is ready to party.")
	
@bot.event
async def on_message(message):
	if (message.author.name == "party_bot"):
		return
	
	if message.content == "hello":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		await message.channel.send("Howdy!")


@bot.event
async def on_voice_state_update(member, before, after): 
	
	if (after.channel == None): 
		return

	gotChannel = bot.get_channel(after.channel.id)
	currentlyOnline = gotChannel.members
	
	if (len(currentlyOnline) >= 2 and len(currentlyOnline) < 4):
		print("There's room in the party")
		
		guildChannels = bot.get_guild(currentlyOnline[0].guild.id).channels
		generalChannelFilter = filter(lambda x: x.name.lower() == "general", guildChannels)
		for channel in generalChannelFilter:
			print("Sending message to channel", channel)
			await channel.send("@everyone There's {} members in the party. Get in there!".format(len(currentlyOnline)))
	
	

@tree.command(name="subscribe", description="Subscribe to be notified when a squad has an opening")
async def subscribe(interaction: discord.Interaction): 
	await interaction.response.send_message("You've subscribed.")


bot.run(os.getenv('DISCORD_TOKEN'))