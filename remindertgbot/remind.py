import datetime
from telegram import Update
from telegram.ext import (
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    ContextTypes,
    filters
)
from database import add_reminder

TIME, TEXT = range(2)

async def remind_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⏰ Vaqtni kiriting:\nYYYY-MM-DD HH:MM\nMisol uchun: 2026-01-09 09:53\n\n/cancel — bekor qilish"
    )
    return TIME

async def get_time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        time = datetime.datetime.strptime(update.message.text, "%Y-%m-%d %H:%M")
        context.user_data["time"] = time
        await update.message.reply_text("✍️ Eslatma matnini yozing:")
        return TEXT
    except ValueError:
        await update.message.reply_text("❌ Noto‘g‘ri format. Qayta urinib ko‘ring.")
        return TIME

async def get_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    add_reminder(
        update.effective_chat.id,
        update.message.text,
        context.user_data["time"].isoformat()
    )
    await update.message.reply_text("✅ Eslatma saqlandi!")
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ Bekor qilindi.")
    return ConversationHandler.END

def get_remind_handler():
    return ConversationHandler(
        entry_points=[CommandHandler("remind", remind_start)],
        states={
            TIME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_time)],
            TEXT: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_text)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
