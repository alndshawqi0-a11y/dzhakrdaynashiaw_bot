import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN") or "8644286932:AAE-bJGIwynojZjOyYnK6J6Qy-Zm06W8wbg"

async def delete_everything(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        # پشکنین بۆ ئەوەی ئایا ستیکەرە، یان فایلی جووڵاوە (GIF/Animation)، یان ڤیدیۆیە
        if update.message.sticker or update.message.animation or update.message.video or update.message.document:
            try:
                await update.message.delete()
            except Exception as e:
                print(f"Error: {e}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    # filters.ALL گشتییە و هەموو جۆرە نامە و فایلك دەگرێت
    app.add_handler(MessageHandler(filters.ALL, delete_everything))
    app.run_polling()

if __name__ == "__main__":
    main()
