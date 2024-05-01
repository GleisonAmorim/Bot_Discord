import discord
import openai
from dotenv import load_dotenv
from discord.ext import commands
import os

load_dotenv()
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

openai.api_key = OPENAI_API_KEY

async def buscar_historico_canal(canal, limit=5):
    messages_list = []
    async for message in canal.history(limit=limit, oldest_first=True):
        messages_list.append(
            {
                "role": "user" if message.author.id != bot.user.id else "system",
                "content": message.content
            }
        )
    return messages_list

async def ask_gpt(mensagens):
    prompt = "\n".join([m["content"] for m in mensagens])
    response = await openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        temperature=0.9,
        top_p=1.0,
        frequency_penalty=0,
        presence_penalty=0,
        stop="\n"
    )
    return response.choices[0].text.strip()

@bot.event
async def on_ready():
    print(f"O bot {bot.user.name} ficou ligado!")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    async with message.channel.typing():
        mensagens = await buscar_historico_canal(message.channel)
        resposta = await ask_gpt(mensagens)

        await message.reply(resposta)

    await bot.process_commands(message)

if DISCORD_BOT_TOKEN is None:
    print("Erro: Token do Discord não foi encontrado.")
    exit()

if OPENAI_API_KEY is None:
    print("Erro: Chave da API do OpenAI não foi encontrada.")
    exit()

bot.run(DISCORD_BOT_TOKEN)
