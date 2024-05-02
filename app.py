import os
from flask import Flask

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name} and {os.environ.get("GREET")}')


app = ApplicationBuilder().token("7088882913:AAHazPIPjVaZTmapVcwrztJP2kZAb3XwFWQ").build()
app1 = Flask(__name__)

app.add_handler(CommandHandler("hello", hello))

@app1.route("/")
def home():
    res = "Hello, World!"
    return res

if __name__ == "__main__":
    app.run_polling()
    app1.run(host='0.0.0.0', port=80)
    
