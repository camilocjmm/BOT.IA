import discord
import random
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hi!")

@bot.command()
async def bye(ctx):
    await ctx.send(">:/")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)  
    await message.channel.send(message.content)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))
    
@bot. command()
async def check(ctx) :
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment. filename
            file_url = attachment.url
            await attachment.save(file_name)
            await ctx.send("Archivo guardado correctamente")
            try:
                class_name = get_class("keras_model.h5","labels.txt", file_name)

                if class_name[0] == "Class 1":
                    await ctx.send("esto es un edificio..........")
                elif class_name[0] == "Class 2":
                    await ctx.send("esto es la selva........")
    
            except:
                await ctx.send("No se pudo hacer la clasificación revisa los formatos de la imagen")

        else:
            await ctx.send("Olvidaste subir una imagen")

bot.run("Token")