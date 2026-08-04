import telebot
from telebot.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)

# ==========================================
# 🛠️ تنظیمات اصلی ربات (نهایی و کامل)
# ==========================================
TOKEN = "8877477958:AAFmHWautnT39uFMeN67wfSl6REdV1j3kg8"
CHANNEL_USERNAME = "@math_rajae"  # آیدی کانال شما
ADMIN_ID = 6622616311  # آیدی عددی شما (تنظیم شد)

bot = telebot.TeleBot(TOKEN)


# ==========================================
# 📚 بانک اطلاعات پیشرفته (برای مدیریت آسان دروس و فایل‌ها)
# ==========================================

CHARTS_DATA = {
    "chart_1402": {
        "title": "چارت درسی ورودی ۱۴۰۲ آموزش ریاضی",
        "file_id": "AgACAgQAAxkBAAOGanH6bG4kG20QflJyM9TrerI4iW0AAqUNaxsi_JFTvNIgzU3eSLwBAAMCAAN3AAM9BA",
    },
    "chart_1403": {
        "title": "چارت درسی ورودی ۱۴۰۳ آموزش ریاضی",
        "file_id": "AgACAgQAAxkBAAM4anHhlDbTt7tudmTIHWuecys2urkAAm4NaxvbzdhSP08pJBBJKmsBAAMCAAN5AAM9BA",
    },
    "chart_1404": {
        "title": "چارت درسی ورودی ۱۴۰۴ آموزش ریاضی",
        "file_id": "AgACAgQAAxkBAAOEanH513C1MmWK2ibWsZHwrhX8YasAAqQNaxsi_JFTA6t73gu1p-sBAAMCAAN3AAM9BA",
    },
}

VIDEOS_DATA = {
    "vid_math1": {
        "title": "ریاضی عمومی ۱",
        "items": [
            {"name": "جلسه اول: تابع و حد", "link": "https://t.me/c/xxxx/1"},
            {
                "name": "جلسه دوم: مشتق و کاربردها",
                "link": "https://t.me/c/xxxx/2",
            },
        ],
    },
    "vid_math2": {
        "title": "ریاضی عمومی ۲",
        "items": [
            {
                "name": "جلسه اول: بردارها و هندسه تحلیلی",
                "link": "https://t.me/c/xxxx/3",
            }
        ],
    },
    "vid_eq": {
        "title": "معادلات دیفرانسیل",
        "items": [
            {
                "name": "جلسه اول: معادلات مرتبه اول",
                "link": "https://t.me/c/xxxx/4",
            }
        ],
    },
    "vid_eng": {
        "title": "ریاضیات مهندسی",
        "items": [
            {"name": "جلسه اول: آنالیز مختلط", "link": "https://t.me/c/xxxx/5"}
        ],
    },
}

BOOKS_DATA = {
    "book_intro": {
        "title": "ریاضی مقدماتی",
        "files": [{"name": "جزوه ریاضی مقدماتی", "file_id": "FILE_ID_INTRO"}],
    },
    "book_math1": {
        "title": "ریاضی عمومی ۱",
        "files": [
            {"name": "📖 کتاب مرجع", "file_id": "FILE_ID_PDF_1"},
            {"name": "📝 جزوه دست‌نویس", "file_id": "FILE_ID_PDF_2"},
        ],
    },
    "book_math2": {
        "title": "ریاضی عمومی ۲",
        "files": [{"name": "📖 کتاب مرجع ریاضی ۲", "file_id": "FILE_ID_PDF_3"}],
    },
    "book_eq": {
        "title": "معادلات دیفرانسیل",
        "files": [{"name": "جزوه معادلات", "file_id": "FILE_ID_PDF_4"}],
    },
    "book_proof": {
        "title": "مقدمه‌ای بر اثبات",
        "files": [{"name": "جزوه مبانی اثبات", "file_id": "FILE_ID_PDF_5"}],
    },
    "book_number": {
        "title": "نظریه اعداد",
        "files": [{"name": "جزوه نظریه اعداد", "file_id": "FILE_ID_PDF_6"}],
    },
    "book_geometry": {
        "title": "مبانی هندسه",
        "files": [{"name": "جزوه هندسه", "file_id": "FILE_ID_PDF_7"}],
    },
    "book_discrete": {
        "title": "ریاضیات گسسته",
        "files": [{"name": "جزوه گسسته", "file_id": "FILE_ID_PDF_8"}],
    },
    "book_linear": {
        "title": "جبر خطی",
        "files": [{"name": "جزوه جبر خطی", "file_id": "FILE_ID_PDF_9"}],
    },
    "book_stats": {
        "title": "آمار و احتمال",
        "files": [{"name": "جزوه آمار و احتمال", "file_id": "FILE_ID_PDF_10"}],
    },
}


# ==========================================
# 🔘 توابع ساخت کیبوردها و منوها
# ==========================================


def get_join_channel_menu():
  markup = InlineKeyboardMarkup()
  channel_url = f"https://t.me/{CHANNEL_USERNAME.replace('@', '')}"
  markup.add(InlineKeyboardButton("📢 ورود به کانال رسمی انجمن", url=channel_url))
  markup.add(
      InlineKeyboardButton(
          "🔄 بررسی دوباره عضویتم", callback_data="check_sub_again"
      )
  )
  return markup


def get_main_reply_keyboard():
  # ساخت کیبورد شستی (پایین صفحه) با ظاهر مرتب و دو ستونه
  keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
  btn1 = KeyboardButton("📚 چارت‌های درسی")
  btn2 = KeyboardButton("🎬 ویدیوهای آموزشی")
  btn3 = KeyboardButton("📄 جزوات و منابع")
  btn4 = KeyboardButton("🎙️ نشریات و پادکست")
  btn5 = KeyboardButton("🔗 لینک‌های مفید")
  btn6 = KeyboardButton("📞 پشتیبانی و ارسال فایل")

  keyboard.add(btn1, btn2)
  keyboard.add(btn3, btn4)
  keyboard.add(btn5, btn6)
  return keyboard


def get_chart_menu():
  markup = InlineKeyboardMarkup()
  markup.row_width = 1
  for key, val in CHARTS_DATA.items():
    markup.add(InlineKeyboardButton(f"🎓 {val['title']}", callback_data=key))
  markup.add(
      InlineKeyboardButton("🔙 بازگشت به منوی اصلی", callback_data="back_to_main")
  )
  return markup


def get_videos_menu():
  markup = InlineKeyboardMarkup()
  markup.row_width = 2
  for key, val in VIDEOS_DATA.items():
    markup.add(InlineKeyboardButton(f"📐 {val['title']}", callback_data=key))
  markup.add(
      InlineKeyboardButton("🔙 بازگشت به منوی اصلی", callback_data="back_to_main")
  )
  return markup


def get_handouts_menu():
  markup = InlineKeyboardMarkup()
  markup.row_width = 2
  for key, val in BOOKS_DATA.items():
    markup.add(InlineKeyboardButton(f"🔹 {val['title']}", callback_data=key))
  markup.add(
      InlineKeyboardButton("🔙 بازگشت به منوی اصلی", callback_data="back_to_main")
  )
  return markup


def get_back_menu():
  markup = InlineKeyboardMarkup()
  markup.add(
      InlineKeyboardButton("🔙 بازگشت به منوی اصلی", callback_data="back_to_main")
  )
  return markup


# ==========================================
# 🔒 سیستم بررسی عضویت
# ==========================================
def check_subscription(user_id):
  try:
    member = bot.get_chat_member(CHANNEL_USERNAME, user_id)
    if member.status in ["member", "administrator", "creator"]:
      return True
    return False
  except Exception as e:
    print(f"Error checking subscription: {e}")
    return True


# ==========================================
# 🚀 هندلر دستور /start
# ==========================================
@bot.message_handler(commands=["start"])
def send_welcome(message):
  user_id = message.from_user.id
  user_name = message.from_user.first_name

  if not check_subscription(user_id):
    warning_text = (
        f"سلام {user_name} جان! 👋🧮\n\n"
        "❌ برای اینکه بتونی از امکانات خفن ربات استفاده کنی، لطفاً اول تو کانال"
        " زیر عضو شو و بعد روی دکمه‌ی بررسی دوباره بزن:"
    )
    bot.send_message(
        message.chat.id, warning_text, reply_markup=get_join_channel_menu()
    )
    return

  welcome_text = (
      f"✨ سلام {user_name} عزیز؛ به ربات انجمن علمی ریاضی خوش اومدی! 🚀🎓\n\n"
      "از منوی جذابی که پایین صفحه برات گذاشتم، می‌تونی خیلی راحت به تمام"
      " امکانات دسترسی داشته باشی. خسته نباشی قهرمان! 💪✨"
  )
  bot.send_message(
      message.chat.id, welcome_text, reply_markup=get_main_reply_keyboard()
  )


# ==========================================
# 💬 مدیریت کلیک‌های شیشه‌ای (داخل پیام‌ها)
# ==========================================
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
  user_id = call.from_user.id

  if call.data != "check_sub_again" and not check_subscription(user_id):
    bot.answer_callback_query(
        call.id, "❌ اول باید تو کانال عضو بشی رفیق!", show_alert=True
    )
    return

  if call.data == "check_sub_again":
    if check_subscription(user_id):
      bot.answer_callback_query(call.id, "✅ عضویتت تأیید شد!")
      bot.edit_message_text(
          chat_id=call.message.chat.id,
          message_id=call.message.message_id,
          text=(
              "🎉 دمت گرم که عضو شدی! حالا از منوی پایین صفحه می‌تونی راحت کارتو"
              " پیش ببری 👇"
          ),
      )
      # ارسال منوی کیبورد شستی به کاربر بعد از تایید
      bot.send_message(
          call.message.chat.id,
          "منوی اصلی ربات:",
          reply_markup=get_main_reply_keyboard(),
      )
    else:
      bot.answer_callback_query(
          call.id, "❌ هنوزه تو کانال عضو نشدی که!", show_alert=True
      )
    return

  elif call.data == "menu_chart":
    bot.answer_callback_query(call.id)
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="📚 **بخش چارت‌های درسی**\n\nورودی خودت رو انتخاب کن:",
        parse_mode="Markdown",
        reply_markup=get_chart_menu(),
    )

  elif call.data == "menu_videos":
    bot.answer_callback_query(call.id)
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="🎬 **بخش ویدیوهای آموزشی**\n\nدرس مد نظرت رو انتخاب کن:",
        parse_mode="Markdown",
        reply_markup=get_videos_menu(),
    )

  elif call.data == "menu_handouts":
    bot.answer_callback_query(call.id)
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="📄 **بانک جزوات و منابع ریاضی**\n\nکدوم درس رو نیاز داری؟",
        parse_mode="Markdown",
        reply_markup=get_handouts_menu(),
    )

  elif call.data == "back_to_main":
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(
        call.message.chat.id,
        "🏠 برگشتیم به منوی اصلی:",
        reply_markup=get_main_reply_keyboard(),
    )

  elif call.data in CHARTS_DATA:
    bot.answer_callback_query(call.id)
    item = CHARTS_DATA[call.data]
    bot.send_photo(
        call.message.chat.id, item["file_id"], caption=f"📄 {item['title']}"
    )

  elif call.data in VIDEOS_DATA:
    bot.answer_callback_query(call.id)
    course = VIDEOS_DATA[call.data]
    text = f"🎥 **ویدیوهای آموزشی درس {course['title']}:**\n\n"
    for idx, vid in enumerate(course["items"], 1):
      text += f"{idx}. [{vid['name']}]({vid['link']})\n"
    bot.send_message(
        call.message.chat.id,
        text,
        parse_mode="Markdown",
        disable_web_page_preview=True,
    )

  elif call.data in BOOKS_DATA:
    bot.answer_callback_query(call.id)
    course = BOOKS_DATA[call.data]
    bot.send_message(
        call.message.chat.id,
        f"📁 منابع و جزوات مربوط به درس **{course['title']}**:",
    )
    for file_info in course["files"]:
      if file_info["file_id"].startswith("FILE_ID_"):
        bot.send_message(
            call.message.chat.id,
            f"🔸 {file_info['name']} (فایل هنوز بارگذاری نشده است)",
        )
      else:
        bot.send_document(
            call.message.chat.id,
            file_info["file_id"],
            caption=file_info["name"],
        )


# ==========================================
# 📱 مدیریت کلیک روی دکمه‌های کیبورد پایین صفحه (Reply Keyboard)
# ==========================================
@bot.message_handler(
    func=lambda message: message.text
    in [
        "📚 چارت‌های درسی",
        "🎬 ویدیوهای آموزشی",
        "📄 جزوات و منابع",
        "🎙️ نشریات و پادکست",
        "🔗 لینک‌های مفید",
        "📞 پشتیبانی و ارسال فایل",
    ]
)
def handle_reply_keyboard_buttons(message):
  user_id = message.from_user.id
  if not check_subscription(user_id):
    bot.send_message(
        message.chat.id,
        "❌ رفیق اول باید تو کانال عضو بشی!",
        reply_markup=get_join_channel_menu(),
    )
    return

  text = message.text

  if text == "📚 چارت‌های درسی":
    bot.send_message(
        message.chat.id,
        "📚 **بخش چارت‌های درسی**\n\nورودی خودت رو انتخاب کن:",
        parse_mode="Markdown",
        reply_markup=get_chart_menu(),
    )

  elif text == "🎬 ویدیوهای آموزشی":
    bot.send_message(
        message.chat.id,
        "🎬 **بخش ویدیوهای آموزشی**\n\nدرس مد نظرت رو انتخاب کن:",
        parse_mode="Markdown",
        reply_markup=get_videos_menu(),
    )

  elif text == "📄 جزوات و منابع":
    bot.send_message(
        message.chat.id,
        "📄 **بانک جزوات و منابع ریاضی**\n\nکدوم درس رو نیاز داری؟",
        parse_mode="Markdown",
        reply_markup=get_handouts_menu(),
    )

  elif text == "🎙️ نشریات و پادکست":
    pod_text = (
        "🎙 **نشریات و پادکست‌های انجمن علمی ریاضی**\n\nمحتواهای صوتی و نشریات"
        " جذاب ما به زودی اینجا آپدیت میشن! 🎧✨"
    )
    bot.send_message(
        message.chat.id, pod_text, parse_mode="Markdown", reply_markup=None
    )

  elif text == "🔗 لینک‌های مفید":
    links_text = (
        "🔗 **لینک‌های مهم و کاربردی:**\n\n🔹 [سامانه"
        " گلستان](https://golestan.sru.ac.ir)\n🔹 [کانال تلگرامی"
        " انجمن](https://t.me/math_rajae)\n🔹 سایت دانشکده ریاضی"
    )
    bot.send_message(
        message.chat.id,
        links_text,
        parse_mode="Markdown",
        disable_web_page_preview=True,
    )

  elif text == "📞 پشتیبانی و ارسال فایل":
    sup_text = (
        "📞 **ارتباط با پشتیبانی و ارسال فایل**\n\nهر گونه پیشنهاد، انتقاد یا"
        " فایلی داری بفرست تا به دست ادمین برسه: 👇"
    )
    sent_msg = bot.send_message(message.chat.id, sup_text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, receive_user_file_or_message)


# ==========================================
# 📥 دریافت فایل و پیام کاربر (و استخراج file_id برای ادمین)
# ==========================================
@bot.message_handler(
    content_types=["photo", "document", "video", "audio", "voice"]
)
def get_file_id_for_admin(message):
  if message.from_user.id == ADMIN_ID:
    if message.photo:
      file_id = message.photo[-1].file_id
      file_type = "عکس (Photo)"
    elif message.document:
      file_id = message.document.file_id
      file_type = "سند/فایل (Document)"
    elif message.video:
      file_id = message.video.file_id
      file_type = "ویدیو (Video)"
    elif message.voice:
      file_id = message.voice.file_id
      file_type = "وویس (Voice)"
    else:
      return

    response_text = (
        f"✅ فایل‌آیدیِ این {file_type}:\n\n`{file_id}`\n\n(برای کپی کردن کافیست"
        " روی متن بالا ضربه بزنید)"
    )
    bot.reply_to(message, response_text, parse_mode="Markdown")
  else:
    receive_user_file_or_message(message)


def receive_user_file_or_message(message):
  if message.text == "/start":
    send_welcome(message)
    return

  user_id = message.from_user.id
  user_name = message.from_user.first_name
  header_text = f"📩 پیام یا فایل جدید از طرف: [{user_name}](tg://user?id={user_id})\nشناسه کاربر: `{user_id}`"

  try:
    bot.send_message(ADMIN_ID, header_text, parse_mode="Markdown")
    bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)
    bot.reply_to(
        message, "✅ پیام یا فایل شما با موفقیت به دست ادمین رسید. مرسی! 🌹"
    )
  except Exception as e:
    bot.reply_to(message, "❌ خطا در ارسال پیام به ادمین.")
    print(f"Error: {e}")


# اجرای اصلی ربات
if __name__ == "__main__":
  print("Bot is running and waiting for messages...")
  bot.infinity_polling()
