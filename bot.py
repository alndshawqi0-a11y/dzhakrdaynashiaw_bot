import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN") or "8644286932:AAE-bJGIwynojZjOyYnK6J6Qy-Zm06W8wbg"

async def delete_unwanted_content(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        # 1. سڕینەوەی هەموو جۆرە ستیکەرێک، ئەنیمەیشن (GIF) و ڤیدیۆ
        is_sticker_or_media = (
            update.message.sticker or 
            update.message.animation or 
            update.message.video or 
            update.message.document
        )
        
        # 2. سڕینەوەی ئەو نامانەی کە کەسێکی تێدا تاگ کراوە (Mention)
        is_mention = False
        if update.message.text:
            if update.message.parse_entities(["mention", "text_mention"]):
                is_mention = True

        # ئەگەر هەر یەکێک لەوانە بوو، ڕاستەوخۆ دەیسڕێتەوە
        if is_sticker_or_media or is_mention:
            try:
                await update.message.delete()
            except Exception as e:
                print(f"Error: {e}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    
    # filters.ALL بۆ ئەوەی هەموو جۆرە نامە و فایلك بپشکنێت
    app.add_handler(MessageHandler(filters.ALL, delete_unwanted_content))
    
    app.run_polling()

if __name__ == "__main__":
    main()
