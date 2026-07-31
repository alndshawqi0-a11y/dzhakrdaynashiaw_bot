import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN") or "8644286932:AAE-bJGIwynojZjOyYnK6J6Qy-Zm06W8wbg"

async def delete_all_stickers(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # پشکنین بۆ ئەوەی ئایا نامەکە ستیکەرە (بە هەموو جۆرەکانیەوە: ئاسایی، جووڵاو، ڤیدیۆیی)
    if update.message and update.message.sticker:
        try:
            await update.message.delete()
        except Exception:
            pass

def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()
    
    # بەکارهێنانی filters.ATTACHMENT یان filters.ALL بۆ ئەوەی هیچ ستیکەرێک فەرامۆش نەکات
    app.add_handler(MessageHandler(filters.Sticker.ALL | filters.ALL, delete_all_stickers))
    
    app.run_polling()

if __name__ == "__main__":
    main()
