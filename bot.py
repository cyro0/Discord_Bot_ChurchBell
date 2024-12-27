import datetime
import discord
import asyncio
from discord.ext import tasks, commands
from constants import TOKEN

# fill list with every datetime hour for join_vc loop
times = []
for i in range(24):
    times.append(datetime.time(hour=i))

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
        print("Wie auf dem Jahrmarkt")
        all_guilds = client.guilds

        v_channels = []
        for i in all_guilds:
            for y in i.categories:
                if len(y.voice_channels) > 0:
                    v_channels.extend(y.voice_channels)
        
        channels_with_members = []
        for channel in v_channels:
            if len(channel.members) > 0:
                channels_with_members.append(channel)

        for channel in channels_with_members:
            voice_client = await channel.connect()
            bell_sound_effect = discord.FFmpegOpusAudio(source="church_bell.ogg", executable="ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg.exe")

            voice_client.play(bell_sound_effect)
            await asyncio.sleep(5)

            await voice_client.disconnect()

    client.run(BOT_TOKEN)