import os
import random
from urllib import response
import discord
from discord.ext import commands
from dotenv import load_dotenv
import openai
# 1


load_dotenv()
# imports os, discord and .env
secret = os.getenv('auth')
TOKEN = secret

# fetches the token from the .env
# 2

bot = commands.Bot(command_prefix=['Dennis ', 'dennis ','!'])
# bot prefix
@bot.event
async def on_ready():
    # this is executed when the bot is ready to run
    print(f'{bot.user.name} has connected to Discord!')



@bot.command(name='ping') #ping pong
async def pong(ctx):
    response = "Pong"
    await ctx.send(response)
"""
@bot.event
async def on_message(message: discord.Message):
    print('Message from {0.author}: {0.content}'.format(message))
    mentions = [str(m) for m in message.mentions]
    text = bot.text_message(message)
    if text == "":
        await message.channel.send("Bot was mentioned")
    else:
        await message.channel.send("Bot was mentioned with message", text)
"""

"""
@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        openai.api_key_path = '/home/endeavour/Github/Dennis-the-discord-bot/openai.env'
        api_key = os.getenv('key')
        openai.api_key =api_key
        #api key
        question = "are you alive?"
        start_sequence = "\nAI:"
        restart_sequence = "\nHuman: "
        #start and end sequences
        response = (openai.Completion.create(
            engine="text-davinci-001",
            prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\nHuman: Hello, what do you like to do?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: What do you like to do?\nAI: I enjoy spending time with friends and family, going on walks, reading, and listening to music.\nHuman: what is your age\nAI: I am 26 years old.\nHuman: do you like anime?\nAI: I do enjoy anime.\nHuman: what anime do you enjoy?\nAI: I enjoy Attack on Titan, Naruto, and Fullmetal Alchemist.\nHuman: what scenes did you like in naruto?\nAI: I enjoyed the fight scenes and the character development.\nHuman: what fight scenes did you like in particular?\nAI: I liked the fight scenes between Naruto and Sasuke the best.\nHuman: "+question+ "\nAi:",
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        ))
        # api call
        text = str(response.choices)
        # the .choices only gives the choices from the response, we make this a string.
        text = text.split("\n")[4]
        # split this along \n and use an index of 4 to only get the output text
        text = (text[12:-1])
        # The text gets sliced to remove any uneeded text in the front (eg, AI:)
        text = text.replace(r'\n', '. ').replace(r'\r', '')
        # This is to replace all \n's with a period and a space.
        n_t = text.split(".")
        # This is to split the string into a list
        if n_t[0] == "n": #checks if the list starts with a lowercase n
            text = text[3:] # if it does then it slices it and starts the text at the third index
        await message.channel.send(text)
    await bot.process_commands(message)
"""

"""
@bot.command(name='chat')
async def ai(ctx,question):
    print(question.content)
    openai.api_key_path = '/home/endeavour/Github/Dennis-the-discord-bot/openai.env'
    api_key = os.getenv('key')
    openai.api_key =api_key
    #api key
    question = yes
    start_sequence = "\nAI:"
    restart_sequence = "\nHuman: "
    #start and end sequences
    response = (openai.Completion.create(
        engine="text-davinci-001",
        prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\nHuman: Hello, what do you like to do?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: What do you like to do?\nAI: I enjoy spending time with friends and family, going on walks, reading, and listening to music.\nHuman: what is your age\nAI: I am 26 years old.\nHuman: do you like anime?\nAI: I do enjoy anime.\nHuman: what anime do you enjoy?\nAI: I enjoy Attack on Titan, Naruto, and Fullmetal Alchemist.\nHuman: what scenes did you like in naruto?\nAI: I enjoyed the fight scenes and the character development.\nHuman: what fight scenes did you like in particular?\nAI: I liked the fight scenes between Naruto and Sasuke the best.\nHuman: "+question+ "\nAi:",
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    ))
    # api call
    text = str(response.choices)
    # the .choices only gives the choices from the response, we make this a string.
    text = text.split("\n")[4]
    # split this along \n and use an index of 4 to only get the output text
    text = (text[12:-1])
    # The text gets sliced to remove any uneeded text in the front (eg, AI:)
    text = text.replace(r'\n', '. ').replace(r'\r', '')
    # This is to replace all \n's with a period and a space.
    n_t = text.split(".")
    # This is to split the string into a list
    if n_t[0] == "n": #checks if the list starts with a lowercase n
        text = text[3:] # if it does then it slices it and starts the text at the third index
    await ctx.send(text)
"""
@bot.event
async def on_message(msg):
    print(msg.content)
    if '!chat' in msg.content:
        print('working over here!')
        openai.api_key_path = '/home/endeavour/Github/Dennis-the-discord-bot/openai.env'
        api_key = os.getenv('key')
        openai.api_key =api_key
        #api key
        question = msg.content
        start_sequence = "\nAI:"
        restart_sequence = "\nHuman: "
        #start and end sequences
        response = (openai.Completion.create(
            engine="text-davinci-001",
            prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\nHuman: Hello, what do you like to do?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: What do you like to do?\nAI: I enjoy spending time with friends and family, going on walks, reading, and listening to music.\nHuman: what is your age\nAI: I am 26 years old.\nHuman: do you like anime?\nAI: I do enjoy anime.\nHuman: what anime do you enjoy?\nAI: I enjoy Attack on Titan, Naruto, and Fullmetal Alchemist.\nHuman: what scenes did you like in naruto?\nAI: I enjoyed the fight scenes and the character development.\nHuman: what fight scenes did you like in particular?\nAI: I liked the fight scenes between Naruto and Sasuke the best.\nHuman: "+question+ "\nAi:",
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        ))
        # api call
        text = str(response.choices)
        # the .choices only gives the choices from the response, we make this a string.
        text = text.split("\n")[4]
        # split this along \n and use an index of 4 to only get the output text
        text = (text[12:-1])
        # The text gets sliced to remove any uneeded text in the front (eg, AI:)
        text = text.replace(r'\n', '. ').replace(r'\r', '')
        # This is to replace all \n's with a period and a space.
        n_t = text.split(".")
        # This is to split the string into a list
        if n_t[0] == "n": #checks if the list starts with a lowercase n
            text = text[3:] # if it does then it slices it and starts the text at the third index
        await msg.channel.send(text)

bot.run(TOKEN)
# runs the bot with the token