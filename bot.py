from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler, ContextTypes

# Replace with your bot token
BOT_TOKEN = "7730000467:AAHFsthJo-2kxXIUi91fVuYR4yCpRuBz-2E"

# Buttons
def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Auto Ads Showing", callback_data='show_ads')],
        [InlineKeyboardButton("Stop Ads Showing", callback_data='stop_ads')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Choose an option:", reply_markup=reply_markup)

# Callback for button clicks
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'show_ads':
        await query.edit_message_text(text="Ads are now showing. Visit the [ad page](http://127.0.0.1:5000/)!", parse_mode="Markdown")
    elif query.data == 'stop_ads':
        await query.edit_message_text(text="Ads have been stopped.")

# Main function
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
