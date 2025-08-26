# AUGUST 26
# SAMIP REGMI

# VIEW CHANNEL , READ MESSAGE HISTORY , SEND MESSAGES->BOT PERMISSION

import os
from dotenv import load_dotenv
load_dotenv()
# DJANGO CONNECT GARNE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dsproject.settings")

import django
django.setup()
# AFTER DJANGO SQL MODELS
import discord
from discord.ext import commands
from sql_db.models import DiscordMember

import asyncio
from asgiref.sync import sync_to_async

# ENV SHIT
DISCORD_BOT_TOKEN = os.environ.get('DISCORD_BOT_TOKEN')
GUILD_ID = int(os.environ.get('GUILD_ID'))
USER_ID = int(os.environ.get('USER_ID'))

intents = discord.Intents.default()
# FETCH MEMBERS
intents.members = True
# READ MESSAGE HISTORY
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# USER SESSION
user_sessions = {}
USER_PATH = 'user.json'
QUESTION_PATH = 'categories/'

async def fetch_and_save_members():
    guild = bot.get_guild(GUILD_ID)
    async for member in guild.fetch_members(limit=None):
        roles = [role.name for role in member.roles if role.name != "@everyone"]
        # SAVE DATA TO SQL
        await sync_to_async(DiscordMember.objects.update_or_create)(
            discord_id=member.id,
            defaults={
                'name': member.name,
                'global_name': member.global_name,
                'discriminator': member.discriminator,
                'joined_at': member.joined_at,
                'roles': ",".join(roles),
                'avatar_url': member.display_avatar.url
            }
        )
    print("SAVED")
# PERIODICALLY UPDATE MEMBER LIST EVERY 10 MINUTES
# ----------------------------------------
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    bot.loop.create_task(periodic_member_update())

async def periodic_member_update():
    await bot.wait_until_ready()
    while not bot.is_closed():
        try:
            await fetch_and_save_members()
        except Exception as e:
            print(f"Error updating members: {e}")
        await asyncio.sleep(600)

bot.run(DISCORD_BOT_TOKEN)