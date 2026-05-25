import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

    channel = bot.get_channel(1498365960153989284)  # ID kanału

    if channel:
        await channel.send(
            f'Cześć, jestem bot {bot.user}!\n'
            'Jeżeli chcesz się dowiedzieć, jakie śmieci wrzucamy do konkretnego kontenera, to wyślij któryś z tych znaków odpowiadających kolorom kontenerów: 🟨 🟩 🟦 🟫 ⬛')
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == '🟨':
        await message.channel.send('''Żółty kontener - metale i tworzywa sztuczne
✅ Do tego kontenera wrzucamy: 
- plastikowe butelki,
- puszki,
- nakrętki, o ile nie ma akcji dobroczynnych związanaych z oddawaniem nakrętek,
- metalowe elementy,
- opakowania plastikowe, 
- elementy plastikowe
❌ Do tego pojemnika nie wrzucamy:
- szklanych butelek,
- części samochdowych,
- tekstylii,
- innych rzeczy niebędącymi metalem lub tworzywami sztucznymi ''')

    elif message.content == '⬛':
        await message.channel.send('''Czarny lub pomarańczowy kontener - odpady zmieszane
✅ Do tego kontenera wrzucamy: 
- wszystko, czego nie da się odzyskać w procesie recyklingu
❌ Do tego pojemnika nie wrzucamy:
- odpadów niebezpiecznych,
- części samochodowych,
- zużytych baterii,
- tekstylii,
- innych rzeczy, które da się odzyskać w procesie recyklingu ''')


    elif message.content == '🟩':
        await message.channel.send('''Zielony kontener - szkło
✅ Do tego kontenera wrzucamy: 
- szklane butelki,
- słoiki
❌ Do tego pojemnika nie wrzucamy:
- słoików z nakrętkami,
- innych rzeczy niebędącymi szkłem''')
    
    elif message.content == '🟦':
        await message.channel.send('''Niebieski kontener - papier i tektura
✅ Do tego kontenera wrzucamy: 
- papier ( różne rodzaje ),
- tekturę ( różne rodzaje ),
- kartonowe opakowania,
❌ Do tego pojemnika nie wrzucamy:
- zabrudzonego papieru i tektury,
- zabrudzonych opakowań,
- innych rzeczy niebędącymi papierem lub tekturą''')

    elif message.content == '🟫':
        await message.channel.send('''Brązowy kontener - odpady biodegradowalne
✅ Do tego kontenera wrzucamy: 
- resztki żywności,
- bio
❌ Do tego pojemnika nie wrzucamy:
- innych rzeczy niebędącymi resztkami żywności lub bio''')

bot.run("TOKEN")
