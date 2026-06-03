from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

import random

TOKEN = "8839652394:AAFIJzNzhNrd4Fs1hq-7KAK5vEcwf89_rMM"

teams = {
    "argentina": 90,
    "france": 89,
    "brazil": 91,
    "germany": 85,
    "iran": 76,
    "england": 88
}

forms = [
    "✅✅✅➖✅",
    "✅❌✅✅➖",
    "✅✅❌➖✅",
    "❌✅✅✅➖"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏆 Football AI Bot Ready"
    )

async def analyze(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:

        text = update.message.text.lower()

        home, away = text.split(" vs ")

        if home not in teams or away not in teams:
            await update.message.reply_text(
                "❌ Team not found"
            )
            return

        home_power = teams[home]
        away_power = teams[away]

        total = home_power + away_power

        home_win = round((home_power / total) * 100)
        away_win = round((away_power / total) * 100)

        draw = random.randint(18, 30)

        xg_home = round(random.uniform(1.4, 2.8), 1)
        xg_away = round(random.uniform(0.7, 2.0), 1)

        corners = random.randint(8, 13)
        shots = random.randint(7, 15)

        analysis = f"""
🏆 Match Analysis

⚽ {home.title()} vs {away.title()}

━━━━━━━━━━━━━━

📈 Win Probability

{home.title()}: {home_win}%
Draw: {draw}%
{away.title()}: {away_win}%

━━━━━━━━━━━━━━

🔥 xG

{home.title()}: {xg_home}
{away.title()}: {xg_away}

━━━━━━━━━━━━━━

🚩 Total Corners: {corners}

🎯 Shots On Target: {shots}

━━━━━━━━━━━━━━

📊 Recent Form

{home.title()}: {random.choice(forms)}
{away.title()}: {random.choice(forms)}

━━━━━━━━━━━━━━

💎 Betting Tips

✔ Over 2.5 Goals
✔ Both Teams To Score
✔ High Corner Match
"""

        await update.message.reply_text(analysis)

    except:
        await update.message.reply_text(
            "Use:\nArgentina vs France"
        )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, analyze))

print("BOT RUNNING ⚽")

app.run_polling()
