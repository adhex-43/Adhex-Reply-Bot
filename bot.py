import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")
OWNER_ID = 123456789  # ← bu yerga O'Z Telegram ID ingizni yozing

AUTO_REPLY_TEXT = (
    "Salom! 👋\n\n"
    "Adhex hozir band, keyinroq aloqaga chiqadi. 🕐\n"
    "Xabaringiz qabul qilindi, tez orada javob beriladi!"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(AUTO_REPLY_TEXT)

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = update.message.text

    # Yozgan odamga avtomatik javob
    await update.message.reply_text(AUTO_REPLY_TEXT)

    # Sizga xabar yuborish
    await context.bot.send_message(
        chat_id=OWNER_ID,
        text=f"📩 Yangi xabar!\n\n👤 Kim: {user.full_name}\n🆔 Username: @{user.username}\n💬 Xabar: {text}"
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))
    print("Bot ishga tushdi! ✅")
    app.run_polling()

if __name__ == "__main__":
    main()
