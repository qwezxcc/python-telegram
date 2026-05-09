from config import BOT_TOKEN
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import database

#
async def start(update: Update,
                context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user = database.get_user(user_id)

    if user:
        await update.message.reply_text(
            f" hello {user_name}! \n"
            "you are already registered. \n"
        )
    else:
        user_name = update.effective_user.first_name
        database.add_user(user_id, user_name)

        await update.message.reply_text(
            f"hi, {user_name}! you succesfully added. \n"
        )
def main():
    print('hi')
    database.init_db()

    print('bot start')
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    
    print("bot started! ctrl+c to stop")
    app.run_polling()

if __name__ == "__main__":
    main()