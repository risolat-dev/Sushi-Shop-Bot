import asyncio
import datetime
from telegram.ext import ApplicationBuilder, CommandHandler
from config import BOT_TOKEN
from handlers import start
from handlers import help_command
from handlers import about
from remind import get_remind_handler
from database import create_table, get_due_reminders, delete_reminder


async def check_reminders(app):
    while True:
        now = datetime.datetime.now().isoformat()
        reminders = get_due_reminders(now)

        for reminder_id, chat_id, text in reminders:
            await app.bot.send_message(
                chat_id=chat_id,
                text=f"⏰ Eslatma:\n{text}"
            )
            delete_reminder(reminder_id)

        await asyncio.sleep(30)


async def on_startup(app):
    asyncio.create_task(check_reminders(app))


def main():
    create_table()

    app = ApplicationBuilder().token(BOT_TOKEN).post_init(on_startup).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(get_remind_handler())

    print("✅ Reminder Bot ishga tushdi")
    app.run_polling()


if __name__ == "__main__":
    main()
