import discord
import random
import json
import os
from discord.ext import commands, tasks

b = commands.Bot(command_prefix = '?')
os.chdir(r'C:\Users\formw\Desktop\Python\DC bots')
@b.event
async def on_member_join(channel):
    await channel.send(f'Welcome to the Ωμεηα Support server.')

@b.event
async def on_member_join(member):
    with open('users.json', 'r') as f:
        users = json.load(f)

    #code
    await update_data(users, member)
    
    with open('users.json', 'w') as f:
        json.dump(users, f)

@b.event
async def on_message(message):
    with open('users.json', 'r') as f:
        users = json.load(f)

    #code
    await update_data(users, message.author)
    await add_money(users, message.author, 2)
    
    with open('users.json', 'w') as f:
        json.dump(users, f)

async def update_data(users, user):
    if not user.id in users:
        users[user.id] = {}
        users[user.id]['money'] = 0

async def add_money(users, user, chng):
    users[user.id]['money'] += chng

b.run()
