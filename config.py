# ══════════════════════════════════════════════
# MRKT Bot Configuration
# ══════════════════════════════════════════════

# ── Telegram Bot ──
BOT_TOKEN = "" # Получите у @BotFather
BOT_USERNAME = ""  # без @

# ── Admins ──
ADMIN_IDS = [] # Список ID администраторов, которые могут использовать команды бота
INLINE_ALLOWED_IDS = [
]   # Список ID пользователей, которым разрешено использовать инлайн-режим бота (оставьте пустым для разрешения всем)

# ── MRKT API ──
MRKT_API_URL = "https://api.tgmrkt.io/api/v1"

# ── Telegram API (для получения init_data через Telethon/Pyrogram) ──
API_ID = 2040
API_HASH = "b18441a1ff607e10a989891a5462e627"

# ── Withdraw Wallet ──
WITHDRAW_WALLET = "" # Адрес кошелька для вывода средств (оставьте пустым для отключения функции вывода)

# ── Logging ──
LOG_CHAT_ID = "" # ID чата для отправки логов (оставьте пустым для отключения)

# ── Broadcast Sessions ──
BROADCAST_SESSIONS_DIR = "mrkt/sessions"

# ── WebApp URL ──
WEBAPP_URL = "" # URL вашего веб-приложения (например, https://yourdomain.com), используемый для генерации ссылок в боте. Оставьте пустым, если не используете веб-приложение.

# ── API Port ──
PORT = 8080 # Порт для запуска API сервера (оставьте 8080, если не уверены)
