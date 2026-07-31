from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = "8644286932:AAE-bJGIwynojZjOYynK6J6Qy-Zm06W8Wbg"

async def delete_stickers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.sticker:
        try:
            await update.message.delete()
            print("ستیکەرێک سڕایەوە!")
        except Exception as e:
            print(f"هەڵە لە سڕینەوەی ستیکەردا: {e}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.Sticker.ALL, delete_stickers))
    print("بوتەکە کارا بوو و ئێستا چاودێری ستیکەرەکان دەکات...")
    app.run_polling()

if __name__ == "__main__":
    main()