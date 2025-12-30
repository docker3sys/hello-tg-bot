import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ["TOKEN"]
APP_URL = "https://hello-tg-bot-production.up.railway.app"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, Alexander!")

application = (
    ApplicationBuilder()
    .token(TOKEN)
    .build()
)

application.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))

    application.run_webhook(
        listen="0.0.0.0",
        port=port,
        url_path="webhook",
        webhook_url=f"{APP_URL}/webhook",
    )