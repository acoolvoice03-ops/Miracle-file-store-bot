import os
from flask import Flask, send_from_directory
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")
UPLOAD_FOLDER = "downloads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app = Flask(__name__)

@app.route('/files/<filename>')
def serve_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

# Telegram Handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me a file, and I'll give you a download link!")

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await update.message.document.get_file()
    filename = update.message.document.file_name
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    await file.download_to_drive(filepath)

    app_url = os.environ.get("APP_URL", "https://your-app.up.railway.app")
    file_link = f"{app_url}/files/{filename}"
    await update.message.reply_text(f"File uploaded! Shareable link:
{file_link}")

def telegram_bot():
    app_bot = ApplicationBuilder().token(BOT_TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    app_bot.add_handler(MessageHandler(filters.Document.ALL, handle_file))
    app_bot.run_polling()

if __name__ == "__main__":
    from threading import Thread
    Thread(target=telegram_bot).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
(update: Update, context: ContextTypes.DEFAULT_TYPE):
    doc = update.message.document
    file_size_mb = doc.file_size / (1024 * 1024)

    if file_size_mb > MAX_FILE_SIZE_MB:
        await update.message.reply_text("❌ File too large. Max 20MB allowed.")
        return

    file = await doc.get_file()
    filename = doc.file_name
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    await file.download_to_drive(filepath)

    filetype = mimetypes.guess_type(filename)[0] or "Unknown"
    app_url = os.environ.get("APP_URL", "https://your-app.up.railway.app")
    file_link = f"{app_url}/files/{filename}"

    await update.message.reply_text(
        f"✅ File received!
"
        f"📄 Name: {filename}
"
        f"💾 Size: {file_size_mb:.2f} MB
"
        f"🗂 Type: {filetype}
"
        f"🔗 Link: {file_link}"
    )

def telegram_bot():
    app_bot = ApplicationBuilder().token(BOT_TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    app_bot.add_handler(MessageHandler(filters.Document.ALL, handle_file))
    app_bot.run_polling()

if __name__ == "__main__":
    from threading import Thread
    Thread(target=telegram_bot).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
