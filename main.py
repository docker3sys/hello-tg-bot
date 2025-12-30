import os
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio

TOKEN = os.environ.get("TOKEN")  # В Replit/локально создай переменную окружения TOKEN
app = Flask(__name__)

# ===== Telegram Bot =====
application = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, Alexander!")

application.add_handler(CommandHandler("start", start))

asyncio.run(application.initialize())  # ⚠ обязательно!

# ===== Webhook =====
# @app.route("/webhook", methods=["POST"])
# def webhook():
#     update = Update.de_json(request.get_json(force=True), application.bot)
#     asyncio.run(application.process_update(update))
#     return "ok"

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "POST":
        update = Update.de_json(request.get_json(force=True), application.bot)
        asyncio.run(application.process_update(update))
    return "WEBHOOK OK"

# ===== Проверка сервера =====
@app.route("/", methods=["GET"])
def index():
    return "Server is running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Replit/локально
    app.run(host="0.0.0.0", port=port)
