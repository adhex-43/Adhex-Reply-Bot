from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# O'z tokeningizni shu yerga yozing
BOT_TOKEN = "BU_YERGA_TOKENINGIZNI_YOZING"

# Avtomatik javon matni
AUTO_REPLY_TEXT = (
    "Salom! 👋\n\n"
    "Adhex hozir band, keyinroq aloqaga chiqadi. 🕐\n"
    "Xabaringiz qabul qilindi, tez orada javob beriladi!"
)

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Har qanday xabarga avtomatik javob beradi"""
    await update.message.reply_text(AUTO_REPLY_TEXT)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # Barcha matnli xabarlarga javob beradi
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))
    
    print("Bot ishga tushdi! ✅")
    app.run_polling()

if __name__ == "__main__":
    main()
