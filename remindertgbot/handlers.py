from telegram import ReplyKeyboardMarkup
from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["/remind"], ["/help"]]
    await update.message.reply_text(
        "👋 Salom!\nMen Reminder Botman ⏰",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Botni ishga tushirish\n"
        "/remind - Yangi eslatma qo‘yish\n"
        "/cancel - Jarayonni bekor qilish\n"
        "/about - Bot haqida"
    )
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Reminder Bot\n\n"
        "Python va SQLite yordamida yozilgan.\n"
        "Eslatmalarni belgilangan vaqtda yuboradi."
    )