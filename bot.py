import datetime
import discord
from discord.ext import tasks, commands
from constants import TOKEN

# fill list with every datetime hour for join_vc loop
times = []
for i in range(24):
    for y in range(60):
        times.append(datetime.time(hour=i, minute=y))

def run_bot():
    BOT_TOKEN = TOKEN

    intents = discord.Intents.all()

    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print(f"{client.user} is running!")
        join_vc.start()
    
    @client.event
    async def on_message(message):
        if len(message.mentions) > 0 and message.mentions[0].id == 1316768540572782643:

            author = str(message.author)
            channel = str(message.channel)

            print(f"{author} mentioned {client.user} in {channel}")
            try:
                response = str(datetime.datetime.now())
                await message.channel.send(response)
            
            except Exception as e:
                print(e)

    @tasks.loop(time=times)
    async def join_vc():
        print("Die Stunde hat geschlagen")

    client.run(BOT_TOKEN)