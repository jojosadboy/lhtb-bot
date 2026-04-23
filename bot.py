from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import os
TOKEN = os.getenv("BOT_TOKEN")

# 🎳 START MENU
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎳 *Welcome to LHTB Official Bot!*\n\n"
        "Here are the available commands:\n\n"
        "/course - 📚 Course information\n"
        "/schedule - 📅 Class schedule\n"
        "/register - 📝 Register for class\n"
        "/tournament - 🏆 Tournament info\n"
        "/latest - 📢 Latest updates\n"
        "/contact - 📞 Contact us\n"
        "/help - ❓ Help\n\n"
        "🔥 Learn • Practice • Compete • Grow\n"
        "Let’s strike together!",
        parse_mode="Markdown"
    )

# 📚 COURSE
async def course(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎳 *LHTB Course Information*\n\n"
        "Beginner-friendly program to learn bowling fundamentals.\n\n"
        "📚 You will learn:\n"
        "• Grip, stance, balance\n"
        "• Techniques & movement\n"
        "• Rules and gameplay\n"
        "• Targeting and scoring\n"
        "• Practice drills\n\n"
        "⏱️ Duration: 4 Weeks\n"
        "👥 Open for beginners\n"
        "📍 Location: Bowling Center",
        parse_mode="Markdown"
    )

# 📅 SCHEDULE
async def schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📅 *Class Schedule*\n\n"
        "Weekday Class:\n"
        "• Monday & Wednesday\n"
        "• 6:00 PM – 8:00 PM\n\n"
        "Weekend Class:\n"
        "• Saturday & Sunday\n"
        "• 2:00 PM – 4:00 PM\n\n"
        "⚠️ Please choose only ONE class.",
        parse_mode="Markdown"
    )

# 📝 REGISTER
async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📝 *Register for LHTB*\n\n"
        "Click the link below to register:\n"
        "👉 https://forms.gle/mVoL8uFqiJy6R3ZUA \n\n"
        "⚠️ Limited slots available. Register early!",
        parse_mode="Markdown"
    )

# 🏆 TOURNAMENT
async def tournament(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏆 *Tournament Info*\n\n"
        "The LHTB Tournament is coming soon!\n"
        "Stay tuned for updates and announcements.\n\n"
        "🔥 Get ready to compete!",
        parse_mode="Markdown"
    )

# 📢 LATEST
async def latest(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📢 *Latest Update*\n\n"
        "Registration for May class is now OPEN!\n\n"
        "👉 Secure your spot now before it’s full.",
        parse_mode="Markdown"
    )

# 📞 CONTACT
async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 *Contact Us*\n\n"
        "Telegram: @teamclassicrollers\n"
        "Instagram: https://www.instagram.com/teamclassicrollers/\n"
        "Facebook: https://web.facebook.com/teamclassicrollers\n\n"
        "We’re here to help!",
        parse_mode="Markdown"
    )

# ❓ HELP
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "❓ *Help*\n\n"
        "Use /start to see all commands.\n"
        "If you need support, contact us via /contact.",
        parse_mode="Markdown"
    )

# 🚀 MAIN
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("course", course))
    app.add_handler(CommandHandler("schedule", schedule))
    app.add_handler(CommandHandler("register", register))
    app.add_handler(CommandHandler("tournament", tournament))
    app.add_handler(CommandHandler("latest", latest))
    app.add_handler(CommandHandler("contact", contact))
    app.add_handler(CommandHandler("help", help_command))

    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
