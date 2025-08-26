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
# -------------------------------------------
@bot.command(name="namaste")
async def namaste(ctx):
    guild = ctx.guild
    member_count = guild.member_count
    await ctx.send(f"HEY I AM BOTU\nMANAGED BY DEVSPHERE\nINITIALIZED BY <@{USER_ID}>\nI AM SENDING MEMBER DATA TO OUR API ENDPOINT")

@bot.command(name="sanchai_chau")
async def sanchai_chau(ctx):
    guild = ctx.guild
    member_count = guild.member_count
    await ctx.send(f"EKDAM SANCHAI CHU HAI DHERAI MAYA HAI")

@bot.command(name="upcoming")
async def upcoming(ctx):
    message = (
        "The Compass is an upcoming event organized by devsphere, the event consists of various activites such as games but the major highlight of it is the panel discussion titled “Demystifying Tech: First Steps Into Web and AI”, with the aim to guide freshers and beginner level students in exploring opportunities and challenges in web development and artificial intelligence. We would be honored to have you join us as a panelist to share your insights and experiences with the students.\n"
        "**Event Details:**\n"
        "Topic: Demystifying Tech: First Steps Into Web and AI\n"
        "Format: Panel Discussion\n"
        "Date and Time: 27th August 2025 at 10:00 AM\n"
        "Venue: Biratnagar International College\n"
        "FORM VARA HAI\n"
        "## [CLICK HERE](https://docs.google.com/forms/d/e/1FAIpQLSfK_7Qwz-3CwY5HFPjZD0BZTOhUkqJ64NEeGSVAD9Q8FCEJ4g/viewform?pli=1)\n"
        "## BOTU WILL BE HAPPY IF YOU JOIN US"
    )
    await ctx.send(message)

@bot.command(name="teej")
async def teej(ctx):
    embed = discord.Embed(
        title="HAPPY TEEJ",
        description="LETS GOOO",
        color=0xFF69B4  
    )
    embed.set_image(url="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzI2bWo3bmNzM3J1MWQ0MXZiMHVpbmsyMm0wNW56dHBuNmc1Z3R1eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/KQs8OigaWhDP0mYUX8/giphy.gif")
    
    await ctx.send(embed=embed)

bot.run(DISCORD_BOT_TOKEN)  

# WHEN USER WRITES ASK
# BOTU WILL SAY YOU ARE NOW CONNECTED TO GEMINI
# BOTU WILL ASK FOR YOUR QUERY
# USER WRITES THE QUERY
# BOTU WILL SEND THE QUERY TO GEMINI
# BOTU WILL RETURN THE RESPONSE TO USER

