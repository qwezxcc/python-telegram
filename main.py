from config import BOT_TOKEN
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


#
async def start(update: Update,
                context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "hello! i am the game bot\n"
    )

#main

app = ApplicationBuilder().token(BOT_TOKEN).build()

#
app.add_handler(CommandHandler('start', start))

print("bot started! ctrl+c to stop")
app.run_polling()