import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN", "7704679350:AAHjVtndORSoGMuiNk1YogeP3N6olyF2EU0")
ADMIN_CHAT_ID = int(os.environ.get("ADMIN_CHAT_ID", "7370542279"))

def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("📶 Mpt", callback_data="mpt"), InlineKeyboardButton("📶 Ooredoo", callback_data="ooredoo")],
        [InlineKeyboardButton("📶 Atom", callback_data="atom"), InlineKeyboardButton("📶 Mytel", callback_data="mytel")],
        [InlineKeyboardButton("💳 ငွေလွဲ နံပါတ်များ", callback_data="money_transfer"), InlineKeyboardButton("ℹ️ အကူအညီ", callback_data="help")],
        [InlineKeyboardButton("🤖 Bot ရေးသားသူ", callback_data="author")]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"မဂ်လာပါ {update.effective_user.first_name}!\nWin Lwin Tun data min ရောင်းဝယ်ရေးမှ ကြိုဆိုပါသည်။",
        reply_markup=main_menu_keyboard()
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data in ["mpt","ooredoo","atom","mytel"]:
        prefix = query.data.capitalize()
        keyboard = [
            [InlineKeyboardButton("💾 Data", callback_data=f"{query.data}_data"), InlineKeyboardButton("📱 Min", callback_data=f"{query.data}_min")],
            [InlineKeyboardButton("🛠 Other", callback_data=f"{query.data}_other")],
            [InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")]
        ]
        await query.edit_message_text(f"{prefix} Options:", reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif query.data == "money_transfer":
        keyboard = [
            [InlineKeyboardButton("💸 Wave", callback_data="wave")],
            [InlineKeyboardButton("💸 Kpay", callback_data="kpay")],
            [InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")]
        ]
        await query.edit_message_text("💳 ငွေလွဲ နံပါတ်များ:", reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif query.data == "wave":
        await query.edit_message_text("💸 Wave\n09677782244\nMaythuzarhtun", reply_markup=main_menu_keyboard())
    elif query.data == "kpay":
        await query.edit_message_text("💸 Kpay\n09677782244\nWin Lwin Tun", reply_markup=main_menu_keyboard())
    
    elif query.data == "help":
        keyboard = [
            [InlineKeyboardButton("⚠️ အရေးကြီးဆက်သွယ်ရန်", callback_data="urgent")],
            [InlineKeyboardButton("🔗 Admin acc link", callback_data="admin_link")],
            [InlineKeyboardButton("✍️ အကြုံပြချက်", callback_data="experience")],
            [InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")]
        ]
        await query.edit_message_text("ℹ️ အကူအညီ:", reply_markup=InlineKeyboardMarkup(keyboard))
    elif query.data == "urgent":
        await query.edit_message_text("⚠️ အရေးကြီးဆက်သွယ်ရန်\n09677782244\n09947782244", reply_markup=main_menu_keyboard())
    elif query.data == "admin_link":
        await query.edit_message_text("🔗 Admin acc link\n@Winlwintun123happyBoy", reply_markup=main_menu_keyboard())
    elif query.data == "experience":
        await query.edit_message_text("✍️ အကြုံပြချက်ပေးပါ...", reply_markup=main_menu_keyboard())
    
    elif query.data == "author":
        await query.edit_message_text("🤖 Bot ရေးသားသူ\n@Winlwintun123happyBoy", reply_markup=main_menu_keyboard())
    
    elif query.data == "main_menu":
        await query.edit_message_text(
            f"မဂ်လာပါ {query.from_user.first_name}!\nWin Lwin Tun data min ရောင်းဝယ်ရေးမှ ကြိုဆိုပါသည်။",
            reply_markup=main_menu_keyboard()
        )async def forward_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text:
        text_to_send = f"📨 Bot မှလာသောစာ\nFrom: {update.effective_user.first_name} (@{update.effective_user.username})\n\n{update.message.text}"
        await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=text_to_send)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_text))
    
    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()