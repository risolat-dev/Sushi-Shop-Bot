from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from utils import translate, load_menu, calculate_total
from database import add_order

menu_items = load_menu()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🇺🇿 O'zbekcha", callback_data="lang_uz")],
        [InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru")],
        [InlineKeyboardButton("🇬🇧 English", callback_data="lang_en")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Tilni tanlang / Choose language / Выберите язык:", reply_markup=reply_markup)

async def set_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = query.data.split("_")[1]
    context.user_data["lang"] = lang
    await query.edit_message_text(translate(lang, "welcome"))

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("lang", "uz")
    keyboard = [[InlineKeyboardButton(f"{item['name']} - {item['price']} UZS", callback_data=item['name'])] for item in menu_items]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(translate(lang, "menu_prompt"), reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    selected_item = next((item for item in menu_items if item['name'] == query.data), None)
    if "cart" not in context.user_data:
        context.user_data["cart"] = []
    context.user_data["cart"].append(selected_item)
    lang = context.user_data.get("lang", "uz")
    await query.edit_message_text(f"{selected_item['name']} qo'shildi / added.\nType /cart to see your cart.")

async def view_cart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("lang", "uz")
    cart = context.user_data.get("cart", [])
    if not cart:
        await update.message.reply_text(translate(lang, "cart_empty"))
        return
    total = calculate_total(cart)
    await update.message.reply_text(translate(lang, "cart_total", total=total))

async def checkout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("lang", "uz")
    cart = context.user_data.get("cart", [])
    if not cart:
        await update.message.reply_text(translate(lang, "cart_empty"))
        return
    total = calculate_total(cart)
    add_order(update.message.from_user.id, str(cart), total)
    context.user_data["cart"] = []
    await update.message.reply_text(translate(lang, "order_success", total=total))
