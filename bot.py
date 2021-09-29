import discord
import json
bot = discord.Bot()


with open("conf.json", "r") as conf: 
	data = json.load(conf)
  token = data["token"]
	pref = data["pref"]
  
# Slash Commands
@bot.slash_command()
async def hello(ctx, name: str = None):
    name = name or ctx.author.name
    await ctx.respond(f"Hello {name}!")

    
# Message Commands

@bot.user_command(name="Come here boi!")
async def cu(ctx, user):
    await ctx.respond(f"Yes?")

# Normal Commands

@bot.command()
async def ping(ctx):
    await ctx.send("pong")
    
bot.run(token)
