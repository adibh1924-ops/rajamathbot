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
ADMIN_ID = 6622616311  # آیدی عددی شما

bot = telebot.TeleBot(TOKEN)


# ==========================================
# 📚 بانک اطلاعات پیشرفته (برای مدیریت آسان دروس و فایل‌ها)
# ==========================================

CHARTS_DATA = {
    "chart_1402": {
        "title": "چارت درسی ورودی ۱۴۰۲ آموزش ریاضی",
        "file_id": "BQACAgQAAxkBAAIBd2pyGRlOvSXFK05P9oSy0y-bDuSqAAJlHAACIvyRU-zB1RvtSi1APQQ",
    },
    "chart_1403": {
        "title": "چارت درسی ورودی ۱۴۰۳ آموزش ریاضی",
        "file_id": "BQACAgQAAxkBAAIBf2pyGZoPejTCupCIwBYro2u2adbJAAJmHAACIvyRUzmxKA40ApeMPQQ",
    },
    "chart_1404": {
        "title": "چارت درسی ورودی ۱۴۰۴ آموزش ریاضی",
        "file_id": "BQACAgQAAxkBAAIBgWpyGavIchw4P9ylXpSOKMmz6t3aAAJnHAACIvyRUw4CKNWJkWB8PQQ",
    },
    "chart_bachelor": {
        "title": "فایل برنامه درسی رشته کارشناسی آموزش ریاضی",
        "file_id": "BQACAgQAAxkBAAIBDWpyCr87cp8z5QHP_hGzmlQ5XTHzAAIbEwACH7LBUSWnbHWURFFgPQQ",
    },
}

# بخش جزوات با تعداد فایل‌های مشخص شده برای هر درس
BOOKS_DATA = {
    "book_intro": {
        "title": "ریاضی مقدماتی",
        "files": [{"name": "جزوه ریاضی مقدماتی", "file_id": "FILE_ID_INTRO"}],
    },
    "book_math1": {
        "title": "ریاضی عمومی ۱",
        "files": [
            {"name": "📝 جزوه ریاضی عمومی ۱ - فایل اول", "file_id": "FILE_ID_PDF_2_1"},
            {"name": "📝 جزوه ریاضی عمومی ۱ - فایل دوم", "file_id": "FILE_ID_PDF_2_2"},
        ],
    },
    "book_math2": {
        "title": "ریاضی عمومی ۲",
        "files": [{"name": "📝 جزوه ریاضی عمومی ۲", "file_id": "FILE_ID_PDF_3"}],
    },
    "book_eq": {
        "title": "معادلات دیفرانسیل",
        "files": [
            {"name": "📝 جزوه معادلات دیفرانسیل - فایل اول", "file_id": "FILE_ID_PDF_4_1"},
            {"name": "📝 جزوه معادلات دیفرانسیل - فایل دوم", "file_id": "FILE_ID_PDF_4_2"},
        ],
    },
    "book_number": {
        "title": "نظریه اعداد",
        "files": [
            {"name": "📄 نظریه اعداد - فایل ۱", "file_id": "FILE_ID_NUM_1"},
            {"name": "📄 نظریه اعداد - فایل ۲", "file_id": "FILE_ID_NUM_2"},
            {"name": "📄 نظریه اعداد - فایل ۳", "file_id": "FILE_ID_NUM_3"},
            {"name": "📄 نظریه اعداد - فایل ۴", "file_id": "FILE_ID_NUM_4"},
            {"name": "📄 نظریه اعداد - فایل ۵", "file_id": "FILE_ID_NUM_5"},
        ],
    },
    "book_geometry": {
        "title": "مبانی هندسه",
        "files": [{"name": "جزوه مبانی هندسه", "file_id": "FILE_ID_PDF_7"}],
    },
    "book_proof": {
        "title": "مقدمه‌ای بر اثبات",
        "files": [{"name": "جزوه مقدمه‌ای بر اثبات", "file_id": "FILE_ID_PDF_5"}],
    },
    "book_discrete": {
        "title": "ریاضیات گسسته",
        "files": [{"name": "جزوه ریاضیات گسسته", "file_id": "FILE_ID_PDF_8"}],
    },
    "book_linear": {
        "title": "جبر خطی",
        "files": [{"name": "جزوه جبر خطی", "file_id": "FILE_ID_PDF_9"}],
    },
    "book_probability": {
        "title": "مبانی احتمال",
        "files": [{"name": "جزوه مبانی احتمال", "file_id": "FILE_ID_PDF_PROB"}],
    },
}

# منابع و رفرنس‌ها (۱۱ گزینه دروس تخصصی ریاضی)
REFERENCES_SPECIALIZED = {
    "ref_math1": {
        "title": "ریاضی عمومی ۱",
        "files": [{"name": "📖 کتاب مرجع ریاضی عمومی ۱", "file_id": "FILE_ID_REF_M1"}],
    },
    "ref_math2": {
        "title": "ریاضی عمومی ۲",
        "files": [{"name": "📖 کتاب مرجع ریاضی عمومی ۲", "file_id": "FILE_ID_REF_M2"}],
    },
    "ref_eq": {
        "title": "معادلات دیفرانسیل",
        "files": [{"name": "📖 کتاب مرجع معادلات دیفرانسیل", "file_id": "FILE_ID_REF_EQ"}],
    },
    "ref_linear": {
        "title": "جبرخطی",
        "files": [{"name": "📖 کتاب مرجع جبرخطی", "file_id": "FILE_ID_REF_LIN"}],
    },
    "ref_discrete": {
        "title": "ریاضیات گسسته",
        "files": [{"name": "📖 کتاب مرجع ریاضیات گسسته", "file_id": "FILE_ID_REF_DISC"}],
    },
    "ref_proof": {
        "title": "مقدمه‌ای بر اثبات",
        "files": [{"name": "📖 کتاب مرجع مقدمه‌ای بر اثبات", "file_id": "FILE_ID_REF_PROOF"}],
    },
    "ref_number": {
        "title": "نظریه اعداد",
        "files": [{"name": "📖 کتاب مرجع نظریه اعداد", "file_id": "FILE_ID_REF_NUM"}],
    },
    "ref_geometry": {
        "title": "مبانی هندسه",
        "files": [{"name": "📖 کتاب مرجع مبانی هندسه", "file_id": "FILE_ID_REF_GEO"}],
    },
    "ref_stats": {
        "title": "آمار و احتمال",
        "files": [{"name": "📖 کتاب مرجع آمار و احتمال", "file_id": "FILE_ID_REF_STATS"}],
    },
    "ref_algebraic_structures": {
        "title": "ساختارهای جبری",
        "files": [{"name": "📖 کتاب مرجع ساختارهای جبری", "file_id": "FILE_ID_REF_ALG"}],
    },
    "ref_analysis1": {
        "title": "آنالیز ریاضی ۱",
        "files": [{"name": "📖 کتاب مرجع آنالیز ریاضی ۱", "file_id": "FILE_ID_REF_ANALY"}],
    },
}

PODCASTS_DATA = [
    {
        "name": "معرفی رشته آموزش ریاضی در سه پارت",
        "is_multi": True,
        "file_ids": [
            "CQACAgQAAxkBAAOcanIBZ8V-yCiLTbL43tLh6yf9-H8AAuMNAAJBTWBTb8nkuvkc2pQ9BA",
            "CQACAgQAAxkBAAOsanIC0lZPIyeCPlV3zVMpfExVsPcAAuUNAAJBTWBTW-em0w7X2t49BA",
            "CQACAgQAAxkBAAOuanIC2YDTGFy3yHDdQUisFsW-HHgAAuYNAAJBTWBTbr7A423Aa1U9BA",
        ],
    },
    {
        "name": "معرفی پادکست دلتا",
        "file_id": "CQACAgQAAxkBAAOwanIDUX0W50F4PhITgqEWiHeUxNcAAnAQAAJE8iBSBZDjAAEwnUq9PQQ",
    },
    {
        "name": "منطق فازی و دنباله فیبوناچی",
        "file_id": "CQACAgQAAxkBAAOyanIDWw5hhleYOGCyRgn0bPXt6_sAAhwVAAJPYvBTT5VGPspyduY9BA",
    },
    {
        "name": "مصاحبه با دکتر میثم سلیمانی ملکان",
        "file_id": "CQACAgQAAxkBAAO0anIDZr1mKPtRx5uwn6Ir4WIZ6LkAAmkQAAJ9EulQOMRaVORMgYY9BA",
    },
    {
        "name": "عدد پی",
        "file_id": "CQACAgQAAxkBAAO2anIDccXn5v0SNUKBY9rvi_OJPTIAAioRAALMV5hTwc1Ly4KqeHA9BA",
    },
    {
        "name": "روز جهانی زن در ریاضی",
        "file_id": "CQACAgQAAxkBAAO4anIDed29-OL4NOT6tySiWknx_2QAAu0iAALDkAABUnlYjRaXuFQhPQQ",
    },
    {
        "name": "شب یلدا",
        "file_id": "CQACAgQAAxkBAAO6anIDgDVqv_YXm-tho1l_HBTqw7AAAssYAAI85jBTgLyb77iEqJs9BA",
    },
    {
        "name": "پادکست ویژه مرحوم دکتر ریحانی",
        "file_id": "CQACAgQAAxkBAAO8anIDiFZOvW74qsOjNzF937WOcJYAAkcZAAIvCxlQakaLbTYOT-c9BA",
    },
    {
        "name": "منطق یا دیوانگی",
        "file_id": "CQACAgQAAxkBAAO-anIDkefMJt9RNPZe3Qi5__0h5_gAAnMYAALEmjBSJbhgBTY2Ow49BA",
    },
    {
        "name": "معرفی پادکست زندگی پشت فرمول‌ها",
        "file_id": "CQACAgQAAxkBAAPAanIDmVvudOofVB6bnThY4-I8a6MAAnoeAAK_8jBQMbcPenTe5Bs9BA",
    },
    {
        "name": "روت موفانگ",
        "file_id": "CQACAgQAAxkBAAPCanIDocImPF0MqMXztrXrG_Em5GMAArYcAALb8lhQb-yAm68cefQ9BA",
    },
    {
        "name": "نقاشی با اعداد",
        "file_id": "CQACAgQAAxkBAAPEanIDqYcaQVSRsNo6KpK7Vo3VIroAAsUeAAIHJ3hT7FUpHh_165o9BA",
    },
    {
        "name": "اخگر خاکستر طوس",
        "file_id": "CQACAgQAAxkBAAPGanIDsSlINGuEfU27xhsTlp-imcMAAg4dAAIHJ4BTqJ0_8iaYc3g9BA",
    },
]

MAGAZINES_DATA = [
    {
        "name": "نشریه شماره یک دلتا",
        "file_id": "BQACAgQAAxkBAAPIanIDvNuK1jcRojnKj8q7x9SG2GwAAmoQAAL3KqhRLRsl6eU1P1Q9BA",
    },
    {
        "name": "نشریه شماره دوم دلتا",
        "file_id": "BQACAgQAAxkBAAPKanIDxOPchCxmSn7Yh1P-Px6a6UkAAoMRAAJqAAHwUyFDtwsrsKUsPQQ",
    },
    {
        "name": "نشریه دلتا پریم",
        "file_id": "BQACAgQAAxkBAAPSanID70cIYZ48z6C7mHy_X6Etc-8AApYRAAIhBsBQPhQi3wABhNJUPQQ",
    },
    {
        "name": "نشریه شماره سوم دلتا",
        "file_id": "BQACAgQAAxkBAAPManIDzO2yNLqCJLKja5mz2ghfRQQAAmoQAAOy2VNjzJOpbqllUz0E",
    },
    {
        "name": "نشریه شماره چهارم دلتا",
        "file_id": "BQACAgQAAxkBAAPOanID1I7ENHQJezOJTXmVbuiEUh8AAmAZAALPQTBSZji860MXRXI9BA",
    },
    {
        "name": "نشریه شماره پنجم دلتا",
        "file_id": "BQACAgQAAxkBAAPQanID3xflfMGnO9vr-l04S8DXEkkAApodAAIHJ3hT8MWNP6Bg3ps9BA",
    },
]


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
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = KeyboardButton("🔗 لینک‌های مفید")
    btn2 = KeyboardButton("🎙️ نشریات و پادکست")
    btn3 = KeyboardButton("🎬 ویدیوهای آموزشی")
    btn4 = KeyboardButton("📚 چارت‌های درسی")
    btn5 = KeyboardButton("📄 جزوات")
    btn6 = KeyboardButton("📖 منابع و رفرنس")
    btn7 = KeyboardButton("📞 پشتیبانی و ارسال فایل")
    btn8 = KeyboardButton("☎️ راه‌های ارتباطی")

    keyboard.add(btn1, btn2)
    keyboard.add(btn3, btn4)
    keyboard.add(btn5, btn6)
    keyboard.add(btn7, btn8)
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


def get_handouts_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    for key, val in BOOKS_DATA.items():
        markup.add(InlineKeyboardButton(f"🔹 {val['title']}", callback_data=key))
    markup.add(
        InlineKeyboardButton("🔙 بازگشت به منوی اصلی", callback_data="back_to_main")
    )
    return markup


# منوی منابع و رفرنس شامل ۳ گزینه درخواستی
def get_references_main_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton(
            "📐 دروس تخصصی ریاضی", callback_data="ref_specialized"
        ),
        InlineKeyboardButton("📚 دروس عمومی", callback_data="ref_general"),
        InlineKeyboardButton(
            "🎓 دروس تربیتی", callback_data="ref_educational"
        ),
        InlineKeyboardButton(
            "🔙 بازگشت به منوی اصلی", callback_data="back_to_main"
        ),
    )
    return markup


# ۱۱ گزینه دروس تخصصی ریاضی به ترتیب خواسته شده
def get_references_specialized_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    for key, val in REFERENCES_SPECIALIZED.items():
        markup.add(InlineKeyboardButton(f"🔹 {val['title']}", callback_data=key))
    markup.add(InlineKeyboardButton("🔙 بازگشت", callback_data="menu_references"))
    return markup


def get_podcasts_magazines_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("🎧 پادکست‌ها", callback_data="sub_podcasts"),
        InlineKeyboardButton("📚 نشریات", callback_data="sub_magazines"),
        InlineKeyboardButton(
            "🔙 بازگشت به منوی اصلی", callback_data="back_to_main"
        ),
    )
    return markup


def get_podcasts_list_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    for idx, pod in enumerate(PODCASTS_DATA):
        markup.add(
            InlineKeyboardButton(
                f"🎙️ {pod['name']}", callback_data=f"podcast_{idx}"
            )
        )
    markup.add(InlineKeyboardButton("🔙 بازگشت", callback_data="menu_podcasts"))
    return markup


def get_magazines_list_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    for idx, mag in enumerate(MAGAZINES_DATA):
        markup.add(
            InlineKeyboardButton(
                f"📄 {mag['name']}", callback_data=f"magazine_{idx}"
            )
        )
    markup.add(InlineKeyboardButton("🔙 بازگشت", callback_data="menu_podcasts"))
    return markup


def get_useful_links_main_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton(
            "🏛️ سایت‌های دانشگاه تربیت دبیر شهید رجائی",
            callback_data="links_sru_sites",
        ),
        InlineKeyboardButton(
            "📢 کانال‌های دانشگاه", callback_data="links_uni_channels"
        ),
        InlineKeyboardButton(
            "👥 کانال‌های دانشجویی", callback_data="links_student_channels"
        ),
        InlineKeyboardButton(
            "🔙 بازگشت به منوی اصلی", callback_data="back_to_main"
        ),
    )
    return markup


def get_useful_links_sru_sites_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton(
            "سایت دانشگاه تربیت دبیر شهید رجائی",
            url="https://www.sru.ac.ir",
        ),
        InlineKeyboardButton(
            "سایت گلستان رجائی",
            url="https://portal.sru.ac.ir/forms/authenticateuser/main.htm",
        ),
        InlineKeyboardButton(
            "سامانه ال‌ام‌اس رجائی", url="https://lms.sru.ac.ir"
        ),
        InlineKeyboardButton(
            "سامانه نگارستان رجائی", url="https://negarestan.sru.ac.ir"
        ),
        InlineKeyboardButton("سماد رجائی", url="https://food.sru.ac.ir/index.rose"),
        InlineKeyboardButton(
            "سامانه کتابخانه رجائی", url="https://lib.sru.ac.ir/dl/usersearch/"
        ),
        InlineKeyboardButton(
            "سایت کارورزی دانشگاه رجائی", url="https://karvarzi.sru.ac.ir"
        ),
        InlineKeyboardButton(
            "سامانه رویدادهای پژوهشی دانشگاه رجائی",
            url="https://events.sru.ac.ir/users/login.php",
        ),
        InlineKeyboardButton("سامانه تکدا", url="https://tarsim.sru.ac.ir"),
        InlineKeyboardButton("🔙 بازگشت", callback_data="menu_useful_links"),
    )
    return markup


def get_useful_links_uni_channels_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton(
            "کانال رسمی دانشگاه", url="https://t.me/SRU_Official"
        ),
        InlineKeyboardButton(
            "کانال معاونت فرهنگی", url="https://t.me/SRU_Cultural"
        ),
        InlineKeyboardButton(
            "کانال معاونت پژوهش و فناوری", url="https://t.me/SRU_Research"
        ),
        InlineKeyboardButton(
            "کانال مرکز آموزش‌های مجازی", url="https://t.me/SRU_Virtual"
        ),
        InlineKeyboardButton(
            "کانال امور دانشجویی", url="https://t.me/SRU_StudentAffairs"
        ),
        InlineKeyboardButton(
            "کانال دانشکده علوم پایه", url="https://t.me/SRU_ScienceFaculty"
        ),
        InlineKeyboardButton(
            "کانال نهاد رهبری", url="https://t.me/SRU_LeaderOffice"
        ),
        InlineKeyboardButton("🔙 بازگشت", callback_data="menu_useful_links"),
    )
    return markup


def get_useful_links_student_channels_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton(
            "کانال انجمن علمی ریاضی", url="https://t.me/math_rajae"
        ),
        InlineKeyboardButton(
            "کانال رسانه دانشجویی", url="https://t.me/SRU_Media"
        ),
        InlineKeyboardButton(
            "کانال انجمن‌های علمی دانشگاه", url="https://t.me/SRU_ScientificAssoc"
        ),
        InlineKeyboardButton(
            "کانال شورای صنفی دانشگاه", url="https://t.me/SRU_Senfi"
        ),
        InlineKeyboardButton(
            "کانال کانون‌های فرهنگی هنری دانشگاه",
            url="https://t.me/SRU_CulturalArt",
        ),
        InlineKeyboardButton(
            "کانال بسیج دانشگاه", url="https://t.me/SRU_Basij"
        ),
        InlineKeyboardButton(
            "کانال جامعه اسلامی دانشگاه", url="https://t.me/SRU_Jamee"
        ),
        InlineKeyboardButton(
            "کانال انجمن اسلامی مستقل", url="https://t.me/SRU_Mostaghel"
        ),
        InlineKeyboardButton(
            "هیئت محبان اهل بیت", url="https://t.me/SRU_Moheban"
        ),
        InlineKeyboardButton("🔙 بازگشت", callback_data="menu_useful_links"),
    )
    return markup


# منوی راه‌های ارتباطی شامل ۵ گزینه درخواستی با دکمه‌های شیشه‌ای URL
def get_communication_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton(
            "💬 کانال تلگرام انجمن علمی ریاضی",
            url="https://t.me/math_rajae",
        ),
        InlineKeyboardButton(
            "📸 پیج اینستاگرام انجمن علمی ریاضی",
            url="https://www.instagram.com/math.sru?igsh=MXZycndhemhkMXgzYg==",
        ),
        InlineKeyboardButton(
            "🟢 کانال بله انجمن علمی ریاضی", url="https://ble.ir/join/J3i3XsLakw"
        ),
        InlineKeyboardButton(
            " ایتا انجمن علمی ریاضی", url="https://eitaa.com/math_rajae"
        ),
        InlineKeyboardButton(
            " روبیکا انجمن علمی ریاضی",
            url="https://rubika.ir/Math_rajae",
        ),
        InlineKeyboardButton(
            "🔙 بازگشت به منوی اصلی", callback_data="back_to_main"
        ),
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

    elif call.data == "menu_useful_links":
        bot.answer_callback_query(call.id)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="🔗 **لینک‌های مفید دانشگاه و انجمن**\n\nبخش مورد نظر رو انتخاب کن:",
            parse_mode="Markdown",
            reply_markup=get_useful_links_main_menu(),
        )

    elif call.data == "links_sru_sites":
        bot.answer_callback_query(call.id)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="🏛️ **سایت‌های دانشگاه تربیت دبیر شهید رجائی**\n\nسامانه مورد نظر رو انتخاب کن:",
            parse_mode="Markdown",
            reply_markup=get_useful_links_sru_sites_menu(),
        )

    elif call.data == "links_uni_channels":
        bot.answer_callback_query(call.id)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="📢 **کانال‌های رسمی دانشگاه**\n\nکانال مورد نظر رو انتخاب کن:",
            parse_mode="Markdown",
            reply_markup=get_useful_links_uni_channels_menu(),
        )

    elif call.data == "links_student_channels":
        bot.answer_callback_query(call.id)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="👥 **کانال‌های دانشجویی**\n\nکانال مورد نظر رو انتخاب کن:",
            parse_mode="Markdown",
            reply_markup=get_useful_links_student_channels_menu(),
        )

    elif call.data == "menu_podcasts":
        bot.answer_callback_query(call.id)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="🎙 **نشریات و پادکست‌های انجمن علمی ریاضی**\n\nبخش مورد نظر رو انتخاب کن:",
            parse_mode="Markdown",
            reply_markup=get_podcasts_magazines_menu(),
        )

    elif call.data == "menu_references":
        bot.answer_callback_query(call.id)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="📖 **منابع و رفرنس‌های درسی**\n\nدسته‌بندی مورد نظر رو انتخاب کن:",
            parse_mode="Markdown",
            reply_markup=get_references_main_menu(),
        )

    elif call.data == "ref_specialized":
        bot.answer_callback_query(call.id)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="📐 **دروس تخصصی ریاضی**\n\nدرس مورد نظر رو انتخاب کن:",
            parse_mode="Markdown",
            reply_markup=get_references_specialized_menu(),
        )

    elif call.data == "ref_general":
        bot.answer_callback_query(call.id)
        bot.send_message(
            call.message.chat.id, "به زودی این امکان فراهم می شود."
        )

    elif call.data == "ref_educational":
        bot.answer_callback_query(call.id)
        bot.send_message(
            call.message.chat.id, "به زودی این امکان فراهم می شود."
        )

    elif call.data == "sub_podcasts":
        bot.answer_callback_query(call.id)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="🎧 **پادکست‌های تخصصی ریاضی**\n\nیکی از پادکست‌ها رو انتخاب کن:",
            parse_mode="Markdown",
            reply_markup=get_podcasts_list_menu(),
        )

    elif call.data == "sub_magazines":
        bot.answer_callback_query(call.id)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="📚 **نشریات علمی دلتا**\n\nشماره مورد نظر رو انتخاب کن:",
            parse_mode="Markdown",
            reply_markup=get_magazines_list_menu(),
        )

    elif call.data.startswith("podcast_"):
        bot.answer_callback_query(call.id)
        idx = int(call.data.split("_")[1])
        pod = PODCASTS_DATA[idx]

        if pod.get("is_multi"):
            for f_id in pod["file_ids"]:
                if f_id.startswith("FILE_ID_"):
                    bot.send_message(
                        call.message.chat.id,
                        f"🎧 **{pod['name']}**\n(فایل صوتی هنوز بارگذاری نشده است)",
                    )
                else:
                    bot.send_audio(
                        call.message.chat.id, f_id, caption=f"🎧 {pod['name']}"
                    )
        else:
            if pod["file_id"].startswith("FILE_ID_"):
                bot.send_message(
                    call.message.chat.id,
                    f"🎧 **{pod['name']}**\n(فایل صوتی هنوز بارگذاری نشده است)",
                )
            else:
                bot.send_audio(
                    call.message.chat.id,
                    pod["file_id"],
                    caption=f"🎧 {pod['name']}",
                )

    elif call.data.startswith("magazine_"):
        bot.answer_callback_query(call.id)
        idx = int(call.data.split("_")[1])
        mag = MAGAZINES_DATA[idx]
        if mag["file_id"].startswith("FILE_ID_"):
            bot.send_message(
                call.message.chat.id,
                f"📄 **{mag['name']}**\n(فایل نشریه هنوز بارگذاری نشده است)",
            )
        else:
            bot.send_document(
                call.message.chat.id, mag["file_id"], caption=f"📄 {mag['name']}"
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
        if item["file_id"].startswith("FILE_ID_"):
            bot.send_message(
                call.message.chat.id,
                f"🔸 {item['title']}\n(فایل این بخش هنوز بارگذاری نشده است)",
            )
        else:
            bot.send_document(
                call.message.chat.id, item["file_id"], caption=f"📄 {item['title']}"
            )

    elif call.data in BOOKS_DATA:
        bot.answer_callback_query(call.id)
        course = BOOKS_DATA[call.data]
        bot.send_message(
            call.message.chat.id,
            f"📁 جزوات مربوط به درس **{course['title']}**:",
            parse_mode="Markdown",
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
                    caption=f"📁 {file_info['name']}",
                )

    elif call.data in REFERENCES_SPECIALIZED:
        bot.answer_callback_query(call.id)
        course = REFERENCES_SPECIALIZED[call.data]
        bot.send_message(
            call.message.chat.id,
            f"📖 رفرنس و منبع مربوط به **{course['title']}**:",
            parse_mode="Markdown",
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
                    caption=f"📖 {file_info['name']}",
                )


# ==========================================
# 📱 مدیریت کلیک روی دکمه‌های کیبورد پایین صفحه (Reply Keyboard)
# ==========================================
@bot.message_handler(
    func=lambda message: message.text
    in [
        "🔗 لینک‌های مفید",
        "🎙️ نشریات و پادکست",
        "🎬 ویدیوهای آموزشی",
        "📚 چارت‌های درسی",
        "📄 جزوات",
        "📖 منابع و رفرنس",
        "📞 پشتیبانی و ارسال فایل",
        "☎️ راه‌های ارتباطی",
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
            "📚 **بخش چارت‌های درسی و برنامه‌ها**\n\nگزینه مورد نظر خودت رو انتخاب کن:",
            parse_mode="Markdown",
            reply_markup=get_chart_menu(),
        )

    elif text == "🎬 ویدیوهای آموزشی":
        bot.send_message(
            message.chat.id, "این امکان به زودی فراهم می‌شود."
        )

    elif text == "📄 جزوات":
        bot.send_message(
            message.chat.id,
            "📄 **بانک جزوات ریاضی**\n\nکدوم درس رو نیاز داری؟",
            parse_mode="Markdown",
            reply_markup=get_handouts_menu(),
        )

    elif text == "📖 منابع و رفرنس":
        bot.send_message(
            message.chat.id,
            "📖 **بخش منابع و رفرنس‌ها**\n\nدسته‌بندی مورد نظر رو انتخاب کن:",
            parse_mode="Markdown",
            reply_markup=get_references_main_menu(),
        )

    elif text == "🎙️ نشریات و پادکست":
        bot.send_message(
            message.chat.id,
            "🎙 **نشریات و پادکست‌های انجمن علمی ریاضی**\n\nبخش مورد نظر رو انتخاب کن:",
            parse_mode="Markdown",
            reply_markup=get_podcasts_magazines_menu(),
        )

    elif text == "🔗 لینک‌های مفید":
        bot.send_message(
            message.chat.id,
            "🔗 **لینک‌های مهم و کاربردی دانشگاه:**\n\nبخش مورد نظر رو انتخاب کن:",
            parse_mode="Markdown",
            reply_markup=get_useful_links_main_menu(),
        )

    elif text == "📞 پشتیبانی و ارسال فایل":
        sup_text = (
            "📞 **ارتباط با پشتیبانی و ارسال فایل**\n\nهر گونه پیشنهاد، انتقاد یا"
            " فایلی داری بفرست تا به دست ادمین برسه: 👇"
        )
        sent_msg = bot.send_message(message.chat.id, sup_text, parse_mode="Markdown")
        bot.register_next_step_handler(sent_msg, receive_user_file_or_message)

    elif text == "☎️ راه‌های ارتباطی":
        comm_text = (
            "☎️ **راه‌های ارتباطی با انجمن علمی ریاضی:**\n\n"
            "لطفاً یکی از راه‌های ارتباطی زیر را انتخاب کنید:"
        )
        bot.send_message(
            message.chat.id,
            comm_text,
            parse_mode="Markdown",
            reply_markup=get_communication_menu(),
        )


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
        elif message.audio:
            file_id = message.audio.file_id
            file_type = "فایل صوتی / پادکست (Audio)"
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
