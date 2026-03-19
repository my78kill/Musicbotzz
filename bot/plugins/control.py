from pyrogram import filters
from bot.core.call import bot, call
from bot.core.queue import pop

@bot.on_message(filters.command("skip"))
async def skip(_, message):
    chat_id = message.chat.id
    next_song = pop(chat_id)

    if next_song:
        url, title = next_song
        await call.change_stream(chat_id, url)
        await message.reply(f"⏭ Playing: {title}")
    else:
        await call.leave_group_call(chat_id)
        await message.reply("Queue khatam")

@bot.on_message(filters.command("stop"))
async def stop(_, message):
    await call.leave_group_call(message.chat.id)
    await message.reply("⏹ Stopped")