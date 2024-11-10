import discord
from discord.ext import commands
import os
from dotenv import load_dotenv


# load secret constants
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = os.getenv("GUILD_ID")


# setup
bot = commands.Bot()


# screenshot command
@bot.slash_command(name="screenshot",description="sends a screenshot", guild_ids=[GUILD_ID])
@discord.option("guidelines", type=discord.SlashCommandOptionType.boolean,
        description="add red guidelines to help with mouse location")
async def screenshot(ctx, guidelines: bool):
    print(guidelines)
    if guidelines:
        await ctx.respond("<screenshot.png> with guidelines")
    else:
        await ctx.respond("<screenshot.png> without guidelines")


# /move_mouse
@bot.slash_command(name="move_mouse", description="moves the mouse", guild_ids=[GUILD_ID])
@discord.option("x_position", type=discord.SlashCommandOptionType.integer,
        description="the x-position to set the mouse")
@discord.option("y_position", type=discord.SlashCommandOptionType.integer,
        description="the y-position to set the mouse")
async def move_mouse(ctx, x_position: int, y_position: int):
    await ctx.respond("moved mouse to: "+str((x_position, y_position)))

# /left_click
@bot.slash_command(name="left_click", description="Left clicks the mouse <clicks> number of times",
        guild_ids=[GUILD_ID])
@discord.option("clicks", type=discord.SlashCommandOptionType.integer,
        description="Number of times to click, must be between 1-3")
async def left_click(ctx, clicks: int):
    if not (1 <= clicks <= 3):
        await ctx.respond("Invalid number of clicks, clicks must be between 1-3")
        return
    await ctx.respond("Left clicked mouse " + str(clicks) + " times")

# /right_click
@bot.slash_command(name="right_click", description="Right clicks the mouse <clicks> number of times",
        guild_ids=[GUILD_ID])
@discord.option("clicks", type=discord.SlashCommandOptionType.integer,
        description="Number of times to click, must be between 1-3")
async def right_click(ctx, clicks: int):
    if not (1 <= clicks <= 3):
        await ctx.respond("Invalid number of clicks, clicks must be between 1-3")
        return
    await ctx.respond("Right clicked mouse " + str(clicks) + " times")


# /type
@bot.slash_command(name="type", description="types text", guild_ids=[GUILD_ID])
@discord.option("text", type=discord.SlashCommandOptionType.string, description="text to be typed")
async def type(ctx, text:str):
    await ctx.respond("typed: \""+text+"\" with the keyboard")

'''
# /hotkey
@bot.slash_command(name="type", description="types text", guild_ids=[GUILD_ID])
@discord.option("ctrl", type=discord.SlashCommandOptionType.boolean, description="use Ctrl key?")
@discord.option("alt", type=discord.SlashCommandOptionType.boolean, description="use Alt key?")
@discord.option("shift", type=discord.SlashCommandOptionType.boolean, description="use Shift key?")
@discord.option("letter", type=discord.SlashCommandOptionType.string, description="Letter to use")
async def hotkey(ctx, ctrl:bool, alt:bool, shift:bool, letter:str):
    if not (ctrl or alt or shift):
        await ctx.respond("You must use atleast 1 special key (Ctrl, Alt, Shift)")
    elif len(letter) != 1:
        await ctx.respond("<letter> must be 1 character long")
    else:
        hotkey_str = [ "ctrl" if ctrl ]
        await ctx.respond("used hotkey: ")
'''


# setup + run
@bot.event
async def on_ready():
    print("logged in as " + str(bot.user))

bot.run(DISCORD_TOKEN)
