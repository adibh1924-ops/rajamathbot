import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

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
        "file_id": "YOUR_FILE_ID_1402",
    },
    "chart_1403": {
        "title": "چارت درسی ورودی ۱۴۰۳ آموزش ریاضی",
        "file_id": "YOUR_FILE_ID_1403",
    },
    "chart_1404": {
        "title": "چارت درسی ورودی ۱۴۰۴ آموزش ریاضی",
        "file_id": "YOUR_FILE_ID_1404",
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
# 🔘 توابع ساخت منوها (ویرایش شده با دکمه لینک کانال)
# ==========================================


def get_join_channel_menu():
  markup = InlineKeyboardMarkup()
  channel_url = f"https://t.me/{CHANNEL_USERNAME.replace('@', '')}"
  markup.add(InlineKeyboardButton("📢 ورود به کانال رسمی", url=channel_url))
  markup.add(
      InlineKeyboardButton(
          "🔄 بررسی دوباره عضویت", callback_data="check_sub_again"
      )
  )
  return markup


def get_main_menu():
  markup = InlineKeyboardMarkup()
  markup.row_width = 2
  markup.add(
      InlineKeyboardButton("📚 چارت درسی", callback_data="menu_chart"),
      InlineKeyboardButton("🎬 ویدیوهای آموزشی", callback_data="menu_videos"),
      InlineKeyboardButton(
          "📄 جزوات و منابع ریاضی", callback_data="menu_handouts"
      ),
      InlineKeyboardButton("🎙 منشورات و پادکست", callback_data="menu_podcasts"),
      InlineKeyboardButton("🔗 لینک‌های مفید", callback_data="menu_links"),
      InlineKeyboardButton(
          "📞 پشتیبانی و ارسال فایل", callback_data="menu_support"
      ),
  )
  return markup


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
        f"سلام {user_name} عزیز! 🌹\n\n"
        "❌ برای استفاده از امکانات ربات، لطفاً ابتدا در کانال ما عضو شوید و سپس"
        " روی دکمه «بررسی دوباره عضویت» کلیک کنید:"
    )
    bot.send_message(
        message.chat.id, warning_text, reply_markup=get_join_channel_menu()
    )
    return

  welcome_text = (
      f"✨ سلام {user_name} عزیز به ربات انجمن علمی ریاضی خوش آمدید! 🌸\n\n"
      "لطفاً از منوی رنگی زیر بخش مورد نظر خود را انتخاب کنید:"
  )
  bot.send_message(message.chat.id, welcome_text, reply_markup=get_main_menu())


# ==========================================
# 🎯 مدیریت کلیک‌ها
# ==========================================
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
  user_id = call.from_user.id

  if call.data != "check_sub_again" and not check_subscription(user_id):
    bot.answer_callback_query(
        call.id, "❌ ابتدا باید در کانال عضو شوید!", show_alert=True
    )
    return

  if call.data == "check_sub_again":
    if check_subscription(user_id):
      bot.answer_callback_query(call.id, "✅ عضویت شما تایید شد!")
      bot.edit_message_text(
          chat_id=call.message.chat.id,
          message_id=call.message.message_id,
          text="✨ خوش آمدید! لطفاً از منوی زیر استفاده کنید:",
          reply_markup=get_main_menu(),
      )
    else:
      bot.answer_callback_query(
          call.id, "❌ شما هنوز در کانال عضو نشده‌اید!", show_alert=True
      )
    return

  elif call.data == "menu_chart":
    bot.answer_callback_query(call.id)
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="📚 **بخش چارت درسی**\n\nلطفاً ورودی خود را انتخاب کنید:",
        parse_mode="Markdown",
        reply_markup=get_chart_menu(),
    )

  elif call.data == "menu_videos":
    bot.answer_callback_query(call.id)
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="🎬 **بخش ویدیوهای آموزشی**\n\nدرس مورد نظر را انتخاب کنید:",
        parse_mode="Markdown",
        reply_markup=get_videos_menu(),
    )

  elif call.data == "menu_handouts":
    bot.answer_callback_query(call.id)
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="📄 **بانک جزوات و منابع ریاضی**\n\nدرس مورد نظر خود را انتخاب"
        " کنید:",
        parse_mode="Markdown",
        reply_markup=get_handouts_menu(),
    )

  elif call.data == "menu_podcasts":
    bot.answer_callback_query(call.id)
    text = (
        "🎙 **نشریات و پادکست‌های انجمن علمی"
        " ریاضی**\n\nلیست شماره‌های نشریه و پادکست‌های صوتی در این بخش قرار"
        " دارد."
    )
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=text,
        parse_mode="Markdown",
        reply_markup=get_back_menu(),
    )

  elif call.data == "menu_links":
    bot.answer_callback_query(call.id)
    text = (
        "🔗 **لینک‌های مفید و کاربردی:**\n\n🔹 سامانه گلستان\n🔹 کانال تلگرامی"
        " انجمن\n🔹 سایت دانشکده"
    )
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=text,
        parse_mode="Markdown",
        reply_markup=get_back_menu(),
    )

  elif call.data == "menu_support":
    bot.answer_callback_query(call.id)
    text = (
        "📞 **ارتباط با پشتیبانی و ارسال فایل**\n\nپیام یا فایل خود را ارسال"
        " کنید تا به دست ادمین برسد:"
    )
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=text,
        parse_mode="Markdown",
        reply_markup=get_back_menu(),
    )
    bot.register_next_step_handler(call.message, receive_user_file_or_message)

  elif call.data == "back_to_main":
    bot.answer_callback_query(call.id)
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="✨ منوی اصلی ربات:",
        reply_markup=get_main_menu(),
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
            f"🔸 {file_info['name']} (فایل هنوز تنظیم نشده است)",
        )
      else:
        bot.send_document(
            call.message.chat.id,
            file_info["file_id"],
            caption=file_info["name"],
        )


# ==========================================
# 📥 دریافت فایل و پیام کاربر (و استخراج file_id برای ادمین)
# ==========================================
@bot.message_handler(
    content_types=["photo", "document", "video", "audio", "voice"]
)
def get_file_id_for_admin(message):
  # اگر فرستنده خودِ شما (ادمین) هستید، file_id فایل را بگیرید
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
    # اگر کاربر عادی بود، فرآیند بخش پشتیبانی و ارسال فایل طی شود
    receive_user_file_or_message(message)


def receive_user_file_or_message(message):
  if message.text == "/start":
    send_welcome(message)
    return

  user_id = message.from_user.id
  user_name = message.from_user.first_name
  header_text = f"📩 دریافت فایل یا پیام جدید از طرف: [{user_name}](tg://user?id={user_id})\nشناسه کاربر: `{user_id}`"

  try:
    bot.send_message(ADMIN_ID, header_text, parse_mode="Markdown")
    bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)
    bot.reply_to(
        message, "✅ پیام و فایل شما با موفقیت به دست ادمین رسید. سپاس! 🌹"
    )
  except Exception as e:
    bot.reply_to(message, "❌ خطا در ارسال فایل یا پیام.")
    print(f"Error: {e}")


# اجرای اصلی ربات
if __name__ == "__main__":
  print("Bot is running and waiting for messages...")
  bot.infinity_polling()
