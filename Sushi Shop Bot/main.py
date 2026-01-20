from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from handlers import start, set_language, menu, button, view_cart, checkout
from database import init_db
from config import TOKEN

init_db()

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("menu", menu))
app.add_handler(CommandHandler("cart", view_cart))
app.add_handler(CommandHandler("checkout", checkout))

app.add_handler(CallbackQueryHandler(set_language, pattern="^lang_"))
app.add_handler(CallbackQueryHandler(button, pattern="^(Salmon Roll|Tuna Roll|California Roll|Chicken Roll)$"))

print("Bot is running...")
app.run_polling()
