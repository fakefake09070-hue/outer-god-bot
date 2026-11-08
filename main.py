import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

current_glory = 0
last_updated_by = "No one yet"

@bot.event
async def on_ready():
    print(f'{bot.user.name} online ho gaya hai aur Outer God Guild ke liye taiyar hai!')

@bot.command()
async def glory(ctx):
    global current_glory, last_updated_by
    embed = discord.Embed(
        title="💀 **GUILD STATUS - OUTER GOD** 💀", 
        description="Here is the latest live status of our Free Fire Guild!", 
        color=0xff0000
    )
    embed.add_field(name="🛡️ Guild Name", value="**OUTER GOD**", inline=True)
    embed.add_field(name="👑 Guild Leader", value="OG KAISER", inline=True)
    embed.add_field(name="🏆 Total Glory", value=f"**{current_glory:,}**", inline=False)
    embed.add_field(name="🎯 Friday Target", value="**1800 Dog Tags**", inline=True)
    embed.add_field(name="📝 Last Updated By", value=f"{last_updated_by}", inline=True)
    embed.set_footer(text="Join the legacy or face the gods!")
    await ctx.send(embed=embed)

@bot.command()
async def update(ctx, new_glory: int):
    global current_glory, last_updated_by
    current_glory = new_glory
    last_updated_by = ctx.author.name
    await ctx.send(f"✅ **Glory Updated!** Outer God ki nayi glory ab **{new_glory:,}** set ho gayi hai.")

bot.run('MTU2ODk0MzIxNzcwODIzNzUx.Gvt4h7.OLE4pIsusuLTGdwiifIxBRuYmHfcqjosiI')
