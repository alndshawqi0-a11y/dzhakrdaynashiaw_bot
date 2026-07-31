import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN") or "8644286932:AAE-bJGIwynojZjOyYnK6J6Qy-Zm06W8wbg"

async def remove_stickers(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # پشکنینی گشتگیر بۆ هەموو جۆرەکانی ستیکەر (ئاسایی، ڤیدیۆیی و جووڵاو)
    if update.message and (update.message.sticker or update.message.video_chat_started):
        pass
    
    if update.message and update.message.sticker:
        try:
            await update.message.delete()
        except Exception:
            pass

def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()
    
    # فیلتەری تایبەت بۆ گرتنی سەرجەم ستیکەرەکان بە بێ کێشە
    app.add_handler(MessageHandler(filters.Sticker.ALL, remove_stickers))
    
    app.run_polling()

if __name == "__main__":
    main()
