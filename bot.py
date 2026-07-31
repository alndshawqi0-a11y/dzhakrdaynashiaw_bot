import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN") or "8644286932:AAE-bJGIwynojZjOyYnK6J6Qy-Zm06W8wbg"

async def delete_stickers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.sticker:
        try:
            await update.message.delete()
        except Exception as e:
            pass

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    # filters.Sticker گشتییە و هەموو جۆرە ستیکەرێکی وێنەیی، جووڵاو و ڤیدیۆیی دەگرێتەوە
    app.add_handler(MessageHandler(filters.Sticker.ALL, delete_stickers))
    app.run_polling()

if name == "main":
    main()
