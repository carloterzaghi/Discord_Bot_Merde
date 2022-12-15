from nextcord.ext import commands 
import os 
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("merde-6d567-firebase-adminsdk-ys45v-31b47664b2.json")
firebase_admin.initialize_app(cred)

bot = commands.Bot(command_prefix= 'm!')

@bot.event
async def on_ready():
    print(f"{bot.user.name} está online!")
    
def load_cogs(bot):
    for file in os.listdir("commands"):
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f"commands.{cog}")

load_cogs(bot)

with open("./.env") as f:
    _token = f.read().strip()

if __name__ == "__main__":
    bot.run(_token)