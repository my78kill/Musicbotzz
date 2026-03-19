from bot.core.call import bot, user, call
from web.server import start

start()

bot.start()
user.start()
call.start()

print("Bot Started!")

bot.idle()