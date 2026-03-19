from pyrogram import filters
from pytgcalls.types.input_stream import AudioPiped
from bot.core.call import bot, call
from bot.core.queue import add, get
from bot.utils.ytdl import search

@bot.on_message(filters.command("play"))
async def play(_, message):
    if len(message.command) < 2:
        return await message.reply("Song name de")

    query = " ".join(message.command[1:])
    url, title = search(query)

    chat_id = message.chat.id
    queue = get(chat_id)

    if not queue:
        await call.join_group_call(chat_id, AudioPiped(url))
        await message.reply(f"▶️ Playing: {title}")
    else:
        add(chat_id, (url, title))
        await message.reply(f"➕ Added to queue: {title}")