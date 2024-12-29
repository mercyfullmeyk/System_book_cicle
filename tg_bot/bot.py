import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler, CallbackContext, CallbackQueryHandler
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hello, {update.message.from_user.username}")
    books, desc = parser()
    kb = []
    co = len(books)
    for i in range(0, co):
        kb.append(InlineKeyboardButton(books[i], callback_data=f'{books[i]}{i}'))
                                   
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            kb
        ]
    )

    await update.message.reply_text(
        text="Выберите книгу",
        reply_markup=keyboard
    )

def parser():
    URL = 'http://127.0.0.1:8000/api/books/'

    json_data = requests.get(URL).json()

    names = []
    desc = []

    for i in json_data:
        names.append(i['name'])
        desc.append(i['description'])

    return names, desc

book, desc = parser()

async def button(update: Update, context: CallbackContext):
    query = update.callback_query
    print(query)
    query.answer() 
    await query.edit_message_text(text=f"{query.data[:-1]}, {desc[int(query.data[-1:])]}")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


if __name__ == '__main__':
    application = ApplicationBuilder().token('7978240927:AAEwblBmrlukGR38XV15d3_ExsUgRYKmAYU').build()

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)    
    start_handler = CommandHandler('start', start)

    application.add_handler(start_handler)
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(echo_handler)
    
    application.run_polling()
