from pyrogram import Client
from pytgcalls import PyTgCalls
from bot.config import API_ID, API_HASH, BOT_TOKEN, SESSION

bot = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
user = Client("user", api_id=API_ID, api_hash=API_HASH, session_string=SESSION)

call = PyTgCalls(user)