import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import json
from nltk.corpus import wordnet as wn
import random

nouns = list(wn.all_synsets(wn.NOUN))
adjectives = list(wn.all_synsets(wn.ADJ))

client = commands.Bot(description="Art Bot", command_prefix="!")
@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')

@client.event
async def on_message(message):
    msg = message.content
    if msg.lower() == 'go' and is_admin(message.author.id):
        await client.send_message(client.get_channel('545331566881144833'), get_random_options(nouns, adjectives))

def is_admin(user_id) :
    admin_list = ['82969926125490176', '131957603252043776']
    for admin_id in admin_list:
        if user_id == admin_id:
            return True
    return False

def get_random_options(noun_list, adj_list):
    num_options = 3
    
    noun_choices = random.sample(noun_list, num_options)
    adjective_choices = random.sample(adj_list, num_options)

    to_return = '```\n'
    
    for i in range(num_options):
        noun_name = (noun_choices[i].name()).split('.')[0]
        adjective_name = (adjective_choices[i].name()).split('.')[0]
    
        to_return += f'Option {i + 1}: {adjective_name} {noun_name}\n'
        to_return += f'{adjective_name} Definition: {adjective_choices[i].definition()}\n'
        to_return += f'{noun_name} Definition: {noun_choices[i].definition()}\n'
        to_return += '\n'

    to_return += '```'

    return to_return


with open('config.json') as f:
    json_data = json.load(f)

print(json_data['discordToken'])
client.run(json_data['discordToken'])
