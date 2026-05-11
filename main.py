# This example requires the 'members' and 'message_content' privileged intents to function.
# bot.commands.py

import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension


There are a number of utility commands being showcased here.'''


intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)


@bot.event
async def on_ready():
    # Tell the type checker that User is filled up at this point
    assert bot.user is not None

    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    # Joined at can be None in very bizarre cases so just handle that as well
    if member.joined_at is None:
        await ctx.send(f'{member} has no join date.')
    else:
        await ctx.send(f'{member} joined {discord.utils.format_dt(member.joined_at)}')


@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')
    bot.run('TOKEN')

# bot_logic.py

import random
def gen_pas(pass_length):
    elements = "+-/*!&$#?=@<>qwertyuiopasdfghjklzxcvbnm[]}{|1234567890"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password
def coin_toss():
    coin = ["orzeł", "reszka"]
    toss = random.choice(coin)
    if toss == "orzeł":
        print(" orzeł.")
    else:
        print(" reszka")
    return toss 
def emoi():
    e = "😀😃😄😁🥚😆🫠😇🥰😜😍🙃😋🫥😶‍🌫️🤑🙂‍↔️🥵🥶🤠😎🥳🧐😲🥱💀👻😻💗💌🌶️❤️💯👋🌹🍄🍇👍🍋‍🟩🫛🍞🥐👊🕷️🍒👏🌭🥞🐟🍣🧊🍲🌳🇸🇦🦞🐒🌯🦍🧊🦧🦝🐺🦏🦚🐟🦖"
    emoij = random.choice(e)
    print(emoij)
    return emoij
    
# bot.py

from bot_logic import coin_toss 
from bot_logic import gen_pas
from bot_logic import emoi
import discord
# Zmienna intents przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej client i przekazanie mu uprawnień
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {client.user}')

@client.event
async def on_message(message):
    for guild in client.guilds:
        for channel in guild.text_channels:
            if channel.name == "#ogólny":
                await channel.send("Cześć wszystkim 😊")
                return
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Cześć!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('?haslo'):
        await message.channel.send("Twoje hasło: " + gen_pas(10))
    elif message.content.startswith('rzut moneta'):
        await message.channel.send("Wypadł/Wypadła " + coin_toss())
    elif message.content.startswith('emoj'):
        await message.channel.send(emoi())
    else:
        await message.channel.send(message.content)
client.run("")
