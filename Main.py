import discord
from discord import app_commands
import os

# Bot-Initialisierung
intents = discord.Intents.default()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

# Event: Bot ist online
@bot.event
async def on_ready():
    await tree.sync()  # Slash-Commands aktivieren
    print(f"{bot.user} ist online!")  # Bestätigung in der Konsole

# Slash-Command: /test → Antwortet "Test Test"
@tree.command(name="test", description="Testbefehl")
async def test(interaction: discord.Interaction):
    await interaction.response.send_message("Test Test")

# Bot starten (Token aus .env)
bot.run(os.getenv("DISCORD_TOKEN"))  # NICHT den Token hier direkt eintragen!
