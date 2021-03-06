import os
import discord
import asyncio
import datetime
import time
import sys

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

async def my_background_task():
    await client.wait_until_ready()
    timeToRelease = datetime.datetime.strptime("August 14 2018", '%B %d %Y')
    while not client.is_closed:
        timeNow = datetime.datetime.utcnow() + datetime.timedelta(hours=2)
        if timeNow.time() > timeToRelease.time():
            countdown = "Ingen tid at spilde, nu skal der spilles!"
        else:
            delta = timeToRelease - timeNow
            hours, remainder = divmod(delta.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            countdown ="BFA RELEASE IN " + str(delta.days) + " DAYS, " + str(hours) + " HOURS AND " + str('%02d' % minutes) + " MINUTES! (ish)"
        try:
            await client.edit_channel(client.get_channel(id=os.environ['channel']), topic=countdown)
        except:
            print("Some error: ", sys.exc_info()[0])
        await asyncio.sleep(60) # task runs every 60 seconds



client.loop.create_task(my_background_task())


client.run(os.environ['token'])

