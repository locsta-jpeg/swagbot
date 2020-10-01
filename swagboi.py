import discord
import random
from discord.ext import commands


client = commands.Bot(command_prefix = "$")

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game(name=f"on {len(Bot.users)} users"))
  print("swag is online")

@client.event
async def on_member_join(member):
  print(f"{member} has joined the server jiggas")

@client.event
async def on_member_remove(member):
  print(f"{member} just left bye jigga")  

@client.command()
async def swag(ctx):
  await ctx.send("leave me alone")

@client.command()
async def ping(ctx):
  await ctx.send(f"pong and {round(client.latency * 1000)}ms")

@client.command()
async def owner(ctx):
  await ctx.send("my daddy is @£ocsta#9109")

@client.command()
async def iztibabes(ctx):
  await ctx.send("sultans slave uwu")

@client.command()
async def kashif(ctx):
  await ctx.send("gay bro i love no homo")

@client.command()
async def talha(ctx):
  await ctx.send("fake corona")

@client.command()
async def amaar(ctx):
  await ctx.send("fellow afghan and beast")

@client.command()
async def akram(ctx):
  await ctx.send("why u bully me and call me gae")

@client.command()
async def isabella(ctx):
  await ctx.send("oh that hot cheeto girl thats a man")       

@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
  responses = ["As I see it yes.",
               "Ask again later.",
               "Better not tell you now.",
               "Cannot predict now.",
               "Concentrate and ask again.",
               "Don’t count on it.",
               "It is certain.",
               "It is decidedly so.",
               "Most likely.",
               "My reply is no.",
               "My sources say no",
               "Outlook not so good.",
               "Outlook good.",
               "Reply hazy, try again.",
               "Signs point to yes.",
               "Very doubtful",
               "Without a doubt",
               "Yes.",]
 
  await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")


@client.command()
async def alemran(ctx):
  await ctx.send("oh that gay boi who left the server")

@client.command()
async def kira(ctx):
  await ctx.send("the bith we all hate")

@client.command()
async def yzarc(ctx):
  await ctx.send("the beast :pensive:")

@client.command()
async def maddie(ctx):
  await ctx.send("oh the pretty but claims to be ugly girl")  

@client.command()
async def brendan(ctx):
  await ctx.send("the alpha male also knows the owner of the bot")  

@client.command()
async def hoeslayer(ctx):
  await ctx.send("£ocsta's personal friend :smiling_imp:")
  
@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send("command isn't found retard :exploding_head:")

@client.command()
async def crate(ctx):
  choices = ("10/10, very big boi :smiling_imp:",
               "9/10",
               "8/10",
               "7/10",
               "6/10",
               "5/10",
               "4/10",
               "3/10",
               "2/10",
               "1/10, lmao you virgin go water your pp",)

  rcrate = random.choice(choices)
  await ctx.send(crate)

  

             

client.run("NzU5NDc5MzQ4MjM0Mjg5MjEz.X2-GQw.LuNxZNcndV9-V-fRgpIbVMBFwW0")  
