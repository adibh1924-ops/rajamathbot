import telebot
from telebot.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    WebAppInfo,
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
    "chart_bachelor": {
        "title": "فایل برنامه درسی رشته کارشناسی آموزش ریاضی",
        "file_id": "BQACAgQAAxkBAAIBDWpyCr87cp8z5QHP_hGzmlQ5XTHzAAIbEwACH7LBUSWnbHWURFFgPQQ",
    },
}

# بخش جزوات با تعداد فایل‌های مشخص شده برای هر درس
BOOKS_DATA = {
    "book_intro": {
        "title": "ریاضی مقدماتی",
        "files": [
            {"name": "جزوه ریاضی مقدماتی - فایل ۱", "file_id": "FILE_ID_INTRO_1"},
            {"name": "جزوه ریاضی مقدماتی - فایل ۲", "file_id": "FILE_ID_INTRO_2"},
        ],
    },
    "book_math1": {
        "title": "ریاضی عمومی ۱",
        "files": [
            {"name": "📝 جزوه ریاضی عمومی ۱ - بخش اول", "file_id": "FILE_ID_PDF_2_1"},
            {"name": "📝 جزوه ریاضی عمومی ۱ - بخش دوم", "file_id": "FILE_ID_PDF_2_2"},
            {"name": "📝 جزوه ریاضی عمومی ۱ - بخش سوم", "file_id": "FILE_ID_PDF_2_3"},
        ],
    },
    "book_math2": {
        "title": "ریاضی عمومی ۲",
        "files": [{"name": "📝 جزوه ریاضی عمومی ۲", "file_id": "FILE_ID_PDF_3"}],
    },
    "book_eq": {
        "title": "معادلات دیفرانسیل",
        "files": [{"name": "📝 جزوه معادلات دیفرانسیل", "file_id": "FILE_ID_PDF_4_1"}],
    },
    "book_probability": {
        "title": "مبانی احتمال",
        "files": [{"name": "جزوه مبانی احتمال", "file_id": "FILE_ID_PDF_PROB"}],
    },
    "book_statistics": {
        "title": "مبانی آمار",
        "files": [
            {"name": "جزوه مبانی آمار - فایل ۱", "file_id": "FILE_ID_STAT_1"},
            {"name": "جزوه مبانی آمار - فایل ۲", "file_id": "FILE_ID_STAT_2"},
        ],
    },
    "book_linear": {
        "title": "جبر خطی",
        "files": [{"name": "جزوه جبر خطی", "file_id": "FILE_ID_PDF_9"}],
    },
    "book_discrete": {
        "title": "ریاضیات گسسته",
        "files": [{"name": "جزوه ریاضیات گسسته", "file_id": "FILE_ID_PDF_8"}],
    },
    "book_geometry": {
        "title": "مبانی هندسه",
        "files": [{"name": "جزوه مبانی هندسه", "file_id": "FILE_ID_PDF_7"}],
    },
    "book_proof": {
        "title": "مقدمه‌ای بر اثبات",
        "files": [
            {"name": "جزوه مقدمه‌ای بر اثبات - فایل ۱", "file_id": "FILE_ID_PDF_5_1"},
            {"name": "جزوه مقدمه‌ای بر اثبات - فایل ۲", "file_id": "FILE_ID_PDF_5_2"},
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
    "book_numerical": {
        "title": "محاسبات عددی",
        "files": [{"name": "جزوه محاسبات عددی", "file_id": "FILE_ID_NUMERICAL"}],
    },
    "book_analysis1": {
        "title": "آنالیز ریاضی",
        "files": [{"name": "جزوه آنالیز ریاضی", "file_id": "FILE_ID_ANALYSIS_1"}],
    },
}

# منابع و رفرنس‌ها - دروس تخصصی ریاضی (با رعایت ترتیب مبانی آمار و مبانی احتمال پشت سر هم و تغییر نام آنالیز ریاضی ۱ به آنالیز ریاضی)
REFERENCES_SPECIALIZED = {
    "ref_statistics_basis": {
        "title": "مبانی آمار",
        "files": [
            {"name": "📖 کتاب مرجع مبانی آمار - فایل ۱", "file_id": "FILE_ID_REF_STAT_1"},
            {"name": "📖 کتاب مرجع مبانی آمار - فایل ۲", "file_id": "FILE_ID_REF_STAT_2"},
        ],
    },
    "ref_probability_basis": {
        "title": "مبانی احتمال",
        "files": [
            {"name": "📖 کتاب مرجع مبانی احتمال - فایل ۱", "file_id": "FILE_ID_REF_PROB_1"},
            {"name": "📖 کتاب مرجع مبانی احتمال - فایل ۲", "file_id": "FILE_ID_REF_PROB_2"},
        ],
    },
    "ref_analysis1": {
        "title": "آنالیز ریاضی",
        "files": [
            {"name": "📖 کتاب مرجع آنالیز ریاضی - فایل ۱", "file_id": "FILE_ID_REF_ANALY_1"},
            {"name": "📖 کتاب مرجع آنالیز ریاضی - فایل ۲", "file_id": "FILE_ID_REF_ANALY_2"},
            {"name": "📖 کتاب مرجع آنالیز ریاضی - فایل ۳", "file_id": "FILE_ID_REF_ANALY_3"},
            {"name": "📖 کتاب مرجع آنالیز ریاضی - فایل ۴", "file_id": "FILE_ID_REF_ANALY_4"},
            {"name": "📖 کتاب مرجع آنالیز ریاضی - فایل ۵", "file_id": "FILE_ID_REF_ANALY_5"},
            {"name": "📖 کتاب مرجع آنالیز ریاضی - فایل ۶", "file_id": "FILE_ID_REF_ANALY_6"},
        ],
    },
    "ref_math1": {
        "title": "ریاضی عمومی ۱",
        "files": [
            {"name": "📖 کتاب مرجع ریاضی عمومی ۱ - فایل ۱", "file_id": "FILE_ID_REF_M1_1"},
            {"name": "📖 کتاب مرجع ریاضی عمومی ۱ - فایل ۲", "file_id": "FILE_ID_REF_M1_2"},
            {"name": "📖 کتاب مرجع ریاضی عمومی ۱ - فایل ۳", "file_id": "FILE_ID_REF_M1_3"},
            {"name": "📖 کتاب مرجع ریاضی عمومی ۱ - فایل ۴", "file_id": "FILE_ID_REF_M1_4"},
            {"name": "📖 کتاب مرجع ریاضی عمومی ۱ - فایل ۵", "file_id": "FILE_ID_REF_M1_5"},
            {"name": "📖 کتاب مرجع ریاضی عمومی ۱ - فایل ۶", "file_id": "FILE_ID_REF_M1_6"},
        ],
    },
    "ref_math2": {
        "title": "ریاضی عمومی ۲",
        "files": [
            {"name": "📖 کتاب مرجع ریاضی عمومی ۲ - فایل ۱", "file_id": "FILE_ID_REF_M2_1"},
            {"name": "📖 کتاب مرجع ریاضی عمومی ۲ - فایل ۲", "file_id": "FILE_ID_REF_M2_2"},
        ],
    },
    "ref_eq": {
        "title": "معادلات دیفرانسیل",
        "files": [{"name": "📖 کتاب مرجع معادلات دیفرانسیل", "file_id": "FILE_ID_REF_EQ"}],
    },
    "ref_numerical": {
        "title": "محاسبات عددی",
        "files": [{"name": "📖 کتاب مرجع محاسبات عددی", "file_id": "FILE_ID_REF_NUMERICAL"}],
    },
    "ref_linear_opt": {
        "title": "بهینه‌سازی",
        "files": [{"name": "📖 کتاب مرجع بهینه‌سازی", "file_id": "FILE_ID_REF_OPT"}],
    },
    "ref_specialized_lang": {
        "title": "زبان تخصصی",
        "files": [{"name": "📖 کتاب مرجع زبان تخصصی", "file_id": "FILE_ID_REF_LANG"}],
    },
    "ref_physics1": {
        "title": "فیزیک پایه ۱",
        "files": [
            {"name": "📖 کتاب مرجع فیزیک پایه ۱ - فایل ۱", "file_id": "FILE_ID_REF_PHY1_1"},
            {"name": "📖 کتاب مرجع فیزیک پایه ۱ - فایل ۲", "file_id": "FILE_ID_REF_PHY1_2"},
        ],
    },
    "ref_physics2": {
        "title": "فیزیک پایه ۲",
        "files": [
            {"name": "📖 کتاب مرجع فیزیک پایه ۲ - فایل ۱", "file_id": "FILE_ID_REF_PHY2_1"},
            {"name": "📖 کتاب مرجع فیزیک پایه ۲ - فایل ۲", "file_id": "FILE_ID_REF_PHY2_2"},
        ],
    },
    "ref_linear": {
        "title": "جبرخطی",
        "files": [
            {"name": "📖 کتاب مرجع جبرخطی - فایل ۱", "file_id": "FILE_ID_REF_LIN_1"},
            {"name": "📖 کتاب مرجع جبرخطی - فایل ۲", "file_id": "FILE_ID_REF_LIN_2"},
        ],
    },
    "ref_algebraic_structures": {
        "title": "ساختارهای جبری",
        "files": [
            {"name": "📖 کتاب مرجع ساختارهای جبری - فایل ۱", "file_id": "FILE_ID_REF_ALG_1"},
            {"name": "📖 کتاب مرجع ساختارهای جبری - فایل ۲", "file_id": "FILE_ID_REF_ALG_2"},
        ],
    },
    "ref_proof": {
        "title": "مقدمه‌ای بر اثبات",
        "files": [
            {"name": "📖 کتاب مرجع مقدمه‌ای بر اثبات - فایل ۱", "file_id": "FILE_ID_REF_PROOF_1"},
            {"name": "📖 کتاب مرجع مقدمه‌ای بر اثبات - فایل ۲", "file_id": "FILE_ID_REF_PROOF_2"},
            {"name": "📖 کتاب مرجع مقدمه‌ای بر اثبات - فایل ۳", "file_id": "FILE_ID_REF_PROOF_3"},
            {"name": "📖 کتاب مرجع مقدمه‌ای بر اثبات - فایل ۴", "file_id": "FILE_ID_REF_PROOF_4"},
        ],
    },
    "ref_discrete": {
        "title": "ریاضیات گسسته",
        "files": [
            {"name": "📖 کتاب مرجع ریاضیات گسسته - فایل ۱", "file_id": "FILE_ID_REF_DISC_1"},
            {"name": "📖 کتاب مرجع ریاضیات گسسته - فایل ۲", "file_id": "FILE_ID_REF_DISC_2"},
            {"name": "📖 کتاب مرجع ریاضیات گسسته - فایل ۳", "file_id": "FILE_ID_REF_DISC_3"},
            {"name": "📖 کتاب مرجع ریاضیات گسسته - فایل ۴", "file_id": "FILE_ID_REF_DISC_4"},
            {"name": "📖 کتاب مرجع ریاضیات گسسته - فایل ۵", "file_id": "FILE_ID_REF_DISC_5"},
            {"name": "📖 کتاب مرجع ریاضیات گسسته - فایل ۶", "file_id": "FILE_ID_REF_DISC_6"},
        ],
    },
    "ref_geometry": {
        "title": "مبانی هندسه",
        "files": [
            {"name": "📖 کتاب مرجع مبانی هندسه - فایل ۱", "file_id": "FILE_ID_REF_GEO_1"},
            {"name": "📖 کتاب مرجع مبانی هندسه - فایل ۲", "file_id": "FILE_ID_REF_GEO_2"},
            {"name": "📖 کتاب مرجع مبانی هندسه - فایل ۳", "file_id": "FILE_ID_REF_GEO_3"},
        ],
    },
    "ref_number": {
        "title": "نظریه اعداد",
        "files": [{"name": "📖 کتاب مرجع نظریه اعداد", "file_id": "FILE_ID_REF_NUM"}],
    },
    "ref_math_art": {
        "title": "ریاضی و هنر",
        "files": [{"name": "📖 کتاب مرجع ریاضی و هنر", "file_id": "FILE_ID_REF_ART"}],
    },
}

# منابع و رفرنس‌ها - دروس عمومی
REFERENCES_GENERAL = {
    "gen_english": {
        "title": "زبان انگلیسی",
        "files": [
            {"name": "📖 منبع زبان انگلیسی - فایل ۱", "file_id": "FILE_ID_GEN_ENG_1"},
            {"name": "📖 منبع زبان انگلیسی - فایل ۲", "file_id": "FILE_ID_GEN_ENG_2"},
        ],
    },
    "gen_health": {
        "title": "سلامت و بهداشت",
        "files": [
            {"name": "📖 منبع سلامت و بهداشت - فایل ۱", "file_id": "FILE_ID_GEN_HEALTH_1"},
            {"name": "📖 منبع سلامت و بهداشت - فایل ۲", "file_id": "FILE_ID_GEN_HEALTH_2"},
        ],
    },
    "gen_history_civilization": {
        "title": "تاریخ و تمدن",
        "files": [],
    },
    "gen_islamic_thought": {
        "title": "اندیشه اسلامی",
        "files": [],
    },
    "gen_life_tradition": {
        "title": "آیین زندگی",
        "files": [],
    },
    "gen_islamic_revolution": {
        "title": "انقلاب اسلامی",
        "files": [],
    },
    "gen_family_knowledge": {
        "title": "دانش خانواده",
        "files": [],
    },
    "gen_analytical_history": {
        "title": "تاریخ تحلیلی",
        "files": [],
    },
    "gen_quran_interpretation": {
        "title": "تفسیر قرآن",
        "files": [],
    },
    "gen_persian": {
        "title": "زبان فارسی",
        "files": [],
    },
}

# منابع و رفرنس‌ها - دروس تربیتی
REFERENCES_EDUCATIONAL = {
    "edu_educational_biography": {
        "title": "سیره تربیتی",
        "files": [{"name": "📖 منبع سیره تربیتی", "file_id": "FILE_ID_EDU_BIO"}],
    },
    "edu_educational_philosophy": {
        "title": "فلسفه تربیتی",
        "files": [{"name": "📖 منبع فلسفه تربیتی", "file_id": "FILE_ID_EDU_PHIL"}],
    },
    "edu_docs_laws": {
        "title": "اسناد و قوانین آ.پ",
        "files": [{"name": "📖 منبع اسناد و قوانین آ.پ", "file_id": "FILE_ID_EDU_DOCS"}],
    },
    "edu_religious_training": {
        "title": "تربیت دینی",
        "files": [{"name": "📖 منبع تربیت دینی", "file_id": "FILE_ID_EDU_REL"}],
    },
    "edu_teacher_ethics": {
        "title": "اخلاق معلمی",
        "files": [{"name": "📖 منبع اخلاق معلمی", "file_id": "FILE_ID_EDU_ETHICS"}],
    },
    "edu_islamic_training_challenges": {
        "title": "چالش‌های تربیت اسلامی",
        "files": [{"name": "📖 منبع چالش‌های تربیت اسلامی", "file_id": "FILE_ID_EDU_CHALL"}],
    },
    "edu_educational_psychology": {
        "title": "روانشناسی",
        "files": [{"name": "📖 منبع روانشناسی", "file_id": "FILE_ID_EDU_PSY"}],
    },
    "edu_counseling_principles": {
        "title": "اصول مشاوره",
        "files": [{"name": "📖 منبع اصول مشاوره", "file_id": "FILE_ID_EDU_COUNSEL"}],
    },
    "edu_sociology": {
        "title": "جامعه شناسی",
        "files": [{"name": "📖 منبع جامعه شناسی", "file_id": "FILE_ID_EDU_SOC"}],
    },
    "edu_islamic_schools_exp": {
        "title": "آشنایی با تجارب مدارس اسلامی",
        "files": [],
    },
    "edu_sacred_defense": {
        "title": "دفاع مقدس",
        "files": [],
    },
}

# کتب درسی ریاضی متوسطه (متوسطه اول و دوم با زیرمجموعه‌ها - هرکدام دو فایل)
HIGH_SCHOOL_MATH = {
    "middle_school": {
        "title": "متوسطه اول",
        "sub_items": {
            "grade_7": {
                "title": "هفتم",
                "files": [
                    {"name": "📚 کتاب ریاضی هفتم - بخش اول", "file_id": "FILE_ID_MATH_7_1"},
                    {"name": "📚 کتاب ریاضی هفتم - بخش دوم", "file_id": "FILE_ID_MATH_7_2"},
                ],
            },
            "grade_8": {
                "title": "هشتم",
                "files": [
                    {"name": "📚 کتاب ریاضی هشتم - بخش اول", "file_id": "FILE_ID_MATH_8_1"},
                    {"name": "📚 کتاب ریاضی هشتم - بخش دوم", "file_id": "FILE_ID_MATH_8_2"},
                ],
            },
            "grade_9": {
                "title": "نهم",
                "files": [
                    {"name": "📚 کتاب ریاضی نهم - بخش اول", "file_id": "FILE_ID_MATH_9_1"},
                    {"name": "📚 کتاب ریاضی نهم - بخش دوم", "file_id": "FILE_ID_MATH_9_2"},
                ],
            },
        },
    },
    "high_school": {
        "title": "متوسطه دوم",
        "sub_items": {
            "10_math_exp": {
                "title": "دهم ریاضی و تجربی",
                "files": [
                    {"name": "📚 کتاب ریاضی ۱ دهم ریاضی و تجربی - فایل ۱", "file_id": "FILE_ID_MATH_10_ME_1"},
                    {"name": "📚 کتاب ریاضی ۱ دهم ریاضی و تجربی - فایل ۲", "file_id": "FILE_ID_MATH_10_ME_2"},
                ],
            },
            "10_humanities": {
                "title": "دهم انسانی",
                "files": [
                    {"name": "📚 کتاب ریاضی و آمار ۱ دهم انسانی - فایل ۱", "file_id": "FILE_ID_MATH_10_HUM_1"},
                    {"name": "📚 کتاب ریاضی و آمار ۱ دهم انسانی - فایل ۲", "file_id": "FILE_ID_MATH_10_HUM_2"},
                ],
            },
            "11_math": {
                "title": "یازدهم ریاضی",
                "files": [
                    {"name": "📚 کتاب‌های ریاضی یازدهم ریاضی - فایل ۱", "file_id": "FILE_ID_MATH_11_M_1"},
                    {"name": "📚 کتاب‌های ریاضی یازدهم ریاضی - فایل ۲", "file_id": "FILE_ID_MATH_11_M_2"},
                ],
            },
            "11_exp": {
                "title": "یازدهم تجربی",
                "files": [
                    {"name": "📚 کتاب ریاضی یازدهم تجربی - فایل ۱", "file_id": "FILE_ID_MATH_11_E_1"},
                    {"name": "📚 کتاب ریاضی یازدهم تجربی - فایل ۲", "file_id": "FILE_ID_MATH_11_E_2"},
                ],
            },
            "11_humanities": {
                "title": "یازدهم انسانی",
                "files": [
                    {"name": "📚 کتاب ریاضی و آمار ۲ یازدهم انسانی - فایل ۱", "file_id": "FILE_ID_MATH_11_HUM_1"},
                    {"name": "📚 کتاب ریاضی و آمار ۲ یازدهم انسانی - فایل ۲", "file_id": "FILE_ID_MATH_11_HUM_2"},
                ],
            },
            "12_math": {
                "title": "دوازدهم ریاضی",
                "files": [
                    {"name": "📚 کتاب‌های ریاضی دوازدهم ریاضی - فایل ۱", "file_id": "FILE_ID_MATH_12_M_1"},
                    {"name": "📚 کتاب‌های ریاضی دوازدهم ریاضی - فایل ۲", "file_id": "FILE_ID_MATH_12_M_2"},
                ],
            },
            "12_exp": {
                "title": "دوازدهم تجربی",
                "files": [
                    {"name": "📚 کتاب ریاضی دوازدهم تجربی - فایل ۱", "file_id": "FILE_ID_MATH_12_E_1"},
                    {"name": "📚 کتاب ریاضی دوازدهم تجربی - فایل ۲", "file_id": "FILE_ID_MATH_12_E_2"},
                ],
            },
            "12_humanities": {
                "title": "دوازدهم انسانی",
                "files": [
                    {"name": "📚 کتاب ریاضی و آمار ۳ دوازدهم انسانی - فایل ۱", "file_id": "FILE_ID_MATH_12_HUM_1"},
                    {"name": "📚 کتاب ریاضی و آمار ۳ دوازدهم انسانی - فایل ۲", "file_id": "FILE_ID_MATH_12_HUM_2"},
                ],
            },
        },
    },
}

# بخش ویدیوهای آموزشی جدید با زیربخش‌های دقیق و تعداد ویدیوهای درخواستی
VIDEOS_DATA = {
    "vid_math1": {
        "title": "ریاضی عمومی ۱",
        "sub": {
            "v_m1_complex": {
                "title": "اعداد مختلط",
                "count": 6,
                "videos": [
                    {"caption": "🎥 ویدیوی شماره ۱ اعداد مختلط ریاضی عمومی ۱", "file_id": "FILE_ID_VID_M1_C1"},
                    {"caption": "🎥 ویدیوی شماره ۲ اعداد مختلط ریاضی عمومی ۱", "file_id": "FILE_ID_VID_M1_C2"},
                    {"caption": "🎥 ویدیوی شماره ۳ اعداد مختلط ریاضی عمومی ۱", "file_id": "FILE_ID_VID_M1_C3"},
                    {"caption": "🎥 ویدیوی شماره ۴ اعداد مختلط ریاضی عمومی ۱", "file_id": "FILE_ID_VID_M1_C4"},
                    {"caption": "🎥 ویدیوی شماره ۵ اعداد مختلط ریاضی عمومی ۱", "file_id": "FILE_ID_VID_M1_C5"},
                    {"caption": "🎥 ویدیوی شماره ۶ اعداد مختلط ریاضی عمومی ۱", "file_id": "FILE_ID_VID_M1_C6"},
                ],
            },
            "v_m1_integral": {
                "title": "انتگرال",
                "count": 7,
                "videos": [
                    {"caption": "🎥 ویدیوی شماره ۱ انتگرال ریاضی عمومی ۱", "file_id": "FILE_ID_VID_M1_I1"},
                    {"caption": "🎥 ویدیوی شماره ۲ انتگرال ریاضی عمومی ۱", "file_id": "FILE_ID_VID_M1_I2"},
                    {"caption": "🎥 ویدیوی شماره ۳ انتگرال ریاضی عمومی ۱", "file_id": "FILE_ID_VID_M1_I3"},
                    {"caption": "🎥 ویدیوی شماره ۴ انتگرال ریاضی عمومی ۱", "file_id": "FILE_ID_VID_M1_I4"},
                    {"caption": "🎥 ویدیوی شماره ۵ انتگرال ریاضی عمومی ۱", "file_id": "FILE_ID_VID_M1_I5"},
                    {"caption": "🎥 ویدیوی شماره ۶ انتگرال ریاضی عمومی ۱", "file_id": "FILE_ID_VID_M1_I6"},
                    {"caption": "🎥 ویدیوی شماره ۷ انتگرال ریاضی عمومی ۱", "file_id": "FILE_ID_VID_M1_I7"},
                ],
            },
            "v_m1_app_integral": {
                "title": "کاربرد انتگرال",
                "count": 4,
                "videos": [
                    {"caption": "🎥 ویدیوی شماره ۱ کاربرد انتگرال ریاضی عمومی ۱", "file_id": "FILE_ID_VID_M1_AI1"},
                    {"caption": "🎥 ویدیوی شماره ۲ کاربرد انتگرال ریاضی عمومی ۱", "file_id": "FILE_ID_VID_M1_AI2"},
                    {"caption": "🎥 ویدیوی شماره ۳ کاربرد انتگرال ریاضی عمومی ۱", "file_id": "FILE_ID_VID_M1_AI3"},
                    {"caption": "🎥 ویدیوی شماره ۴ کاربرد انتگرال ریاضی عمومی ۱", "file_id": "FILE_ID_VID_M1_AI4"},
                ],
            },
        },
    },
    "vid_math2": {
        "title": "ریاضی عمومی ۲",
        "sub": {
            "v_m2_lagrange": {
                "title": "ضرایب لاگرانژ",
                "count": 2,
                "videos": [
                    {"caption": "🎥 ویدیوی شماره ۱ ضرایب لاگرانژ ریاضی عمومی ۲", "file_id": "FILE_ID_VID_M2_L1"},
                    {"caption": "🎥 ویدیوی شماره ۲ ضرایب لاگرانژ ریاضی عمومی ۲", "file_id": "FILE_ID_VID_M2_L2"},
                ],
            },
            "v_m2_double_int": {
                "title": "انتگرال دوگانه",
                "count": 3,
                "videos": [
                    {"caption": "🎥 ویدیوی شماره ۱ انتگرال دوگانه ریاضی عمومی ۲", "file_id": "FILE_ID_VID_M2_DI1"},
                    {"caption": "🎥 ویدیوی شماره ۲ انتگرال دوگانه ریاضی عمومی ۲", "file_id": "FILE_ID_VID_M2_DI2"},
                    {"caption": "🎥 ویدیوی شماره ۳ انتگرال دوگانه ریاضی عمومی ۲", "file_id": "FILE_ID_VID_M2_DI3"},
                ],
            },
            "v_m2_triple_int": {
                "title": "انتگرال سه‌گانه",
                "count": 4,
                "videos": [
                    {"caption": "🎥 ویدیوی شماره ۱ انتگرال سه‌گانه ریاضی عمومی ۲", "file_id": "FILE_ID_VID_M2_TI1"},
                    {"caption": "🎥 ویدیوی شماره ۲ انتگرال سه‌گانه ریاضی عمومی ۲", "file_id": "FILE_ID_VID_M2_TI2"},
                    {"caption": "🎥 ویدیوی شماره ۳ انتگرال سه‌گانه ریاضی عمومی ۲", "file_id": "FILE_ID_VID_M2_TI3"},
                    {"caption": "🎥 ویدیوی شماره ۴ انتگرال سه‌گانه ریاضی عمومی ۲", "file_id": "FILE_ID_VID_M2_TI4"},
                ],
            },
            "v_m2_summary": {
                "title": "جمع‌بندی",
                "count": 2,
                "videos": [
                    {"caption": "🎥 ویدیوی شماره ۱ جمع‌بندی ریاضی عمومی ۲", "file_id": "FILE_ID_VID_M2_S1"},
                    {"caption": "🎥 ویدیوی شماره ۲ جمع‌بندی ریاضی عمومی ۲", "file_id": "FILE_ID_VID_M2_S2"},
                ],
            },
        },
    },
    "vid_eq": {
        "title": "معادلات دیفرانسیل",
        "sub": {
            "v_eq_derivative": {
                "title": "مشتق‌گیری",
                "count": 2,
                "videos": [
                    {"caption": "🎥 ویدیوی شماره ۱ مشتق‌گیری معادلات دیفرانسیل", "file_id": "FILE_ID_VID_EQ_D1"},
                    {"caption": "🎥 ویدیوی شماره ۲ مشتق‌گیری معادلات دیفرانسیل", "file_id": "FILE_ID_VID_EQ_D2"},
                ],
            },
            "v_eq_first_order": {
                "title": "معادلات دیفرانسیل مرتبه اول",
                "count": 5,
                "videos": [
                    {"caption": "🎥 ویدیوی شماره ۱ معادلات دیفرانسیل مرتبه اول", "file_id": "FILE_ID_VID_EQ_FO1"},
                    {"caption": "🎥 ویدیوی شماره ۲ معادلات دیفرانسیل مرتبه اول", "file_id": "FILE_ID_VID_EQ_FO2"},
                    {"caption": "🎥 ویدیوی شماره ۳ معادلات دیفرانسیل مرتبه اول", "file_id": "FILE_ID_VID_EQ_FO3"},
                    {"caption": "🎥 ویدیوی شماره ۴ معادلات دیفرانسیل مرتبه اول", "file_id": "FILE_ID_VID_EQ_FO4"},
                    {"caption": "🎥 ویدیوی شماره ۵ معادلات دیفرانسیل مرتبه اول", "file_id": "FILE_ID_VID_EQ_FO5"},
                ],
            },
            "v_eq_methods": {
                "title": "روش های حل معادلات دیفرانسیل",
                "count": 3,
                "videos": [
                    {"caption": "🎥 ویدیوی شماره ۱ روش های حل معادلات دیفرانسیل", "file_id": "FILE_ID_VID_EQ_M1"},
                    {"caption": "🎥 ویدیوی شماره ۲ روش های حل معادلات دیفرانسیل", "file_id": "FILE_ID_VID_EQ_M2"},
                    {"caption": "🎥 ویدیوی شماره ۳ روش های حل معادلات دیفرانسیل", "file_id": "FILE_ID_VID_EQ_M3"},
                ],
            },
        },
    },
    "vid_engineering_math": {
        "title": "ریاضیات مهندسی",
        "sub": {
            "v_eng_general": {
                "title": "آموزش‌های ریاضیات مهندسی",
                "count": 1,
                "videos": [
                    {"caption": "🎥 ویدیوهای آموزشی ریاضیات مهندسی", "file_id": "FILE_ID_VID_ENG_GEN"}
                ],
            }
        },
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
    # استفاده از ایموجی‌های رنگی و جذاب برای 8 کلید اصلی طبق درخواست رنگ‌بندی زیبا
    btn1 = KeyboardButton("🔗 لینک‌های مفید 🔵")
    btn2 = KeyboardButton("🎙️ نشریات و پادکست 🟣")
    btn3 = KeyboardButton("🎬 ویدیوهای آموزشی 🔴")
    btn4 = KeyboardButton("📚 چارت‌های درسی 🟢")
    btn5 = KeyboardButton("📄 جزوات 🟡")
    btn6 = KeyboardButton("📖 منابع و رفرنس 🟠")
    btn7 = KeyboardButton("📞 پشتیبانی 🟤")
    btn8 = KeyboardButton("☎️ راه‌های ارتباطی ⚫")

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


# منوی اصلی منابع و رفرنس شامل ۴ گزینه
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
            "📚 کتب درسی ریاضی متوسطه", callback_data="ref_high_school_math"
        ),
        InlineKeyboardButton(
            "🔙 بازگشت به منوی اصلی", callback_data="back_to_main"
        ),
    )
    return markup


# دروس تخصصی ریاضی
def get_references_specialized_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    for key, val in REFERENCES_SPECIALIZED.items():
        markup.add(InlineKeyboardButton(f"🔹 {val['title']}", callback_data=key))
    markup.add(InlineKeyboardButton("🔙 بازگشت", callback_data="menu_references"))
    return markup


# دروس عمومی
def get_references_general_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    for key, val in REFERENCES_GENERAL.items():
        markup.add(InlineKeyboardButton(f"🔹 {val['title']}", callback_data=key))
    markup.add(InlineKeyboardButton("🔙 بازگشت", callback_data="menu_references"))
    return markup


# دروس تربیتی
def get_references_educational_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    for key, val in REFERENCES_EDUCATIONAL.items():
        markup.add(InlineKeyboardButton(f"🔹 {val['title']}", callback_data=key))
    markup.add(InlineKeyboardButton("🔙 بازگشت", callback_data="menu_references"))
    return markup


# منوی کتب درسی ریاضی متوسطه (متوسطه اول و متوسطه دوم)
def get_high_school_math_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    for key, val in HIGH_SCHOOL_MATH.items():
        markup.add(InlineKeyboardButton(f"📚 {val['title']}", callback_data=f"hs_{key}"))
    markup.add(InlineKeyboardButton("🔙 بازگشت", callback_data="menu_references"))
    return markup


# زیرمجموعه متوسطه اول (هفتم، هشتم، نهم)
def get_middle_school_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    for key, val in HIGH_SCHOOL_MATH["middle_school"]["sub_items"].items():
        markup.add(InlineKeyboardButton(f"🔹 {val['title']}", callback_data=f"hs_sub_{key}"))
    markup.add(InlineKeyboardButton("🔙 بازگشت", callback_data="ref_high_school_math"))
    return markup


# زیرمجموعه متوسطه دوم
def get_high_school_sub_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    for key, val in HIGH_SCHOOL_MATH["high_school"]["sub_items"].items():
        markup.add(InlineKeyboardButton(f"🔹 {val['title']}", callback_data=f"hs_sub_{key}"))
    markup.add(InlineKeyboardButton("🔙 بازگشت", callback_data="ref_high_school_math"))
    return markup


# منوی ویدیوهای آموزشی
def get_videos_main_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    for key, val in VIDEOS_DATA.items():
        markup.add(InlineKeyboardButton(f"🎬 {val['title']}", callback_data=f"vid_main_{key}"))
    markup.add(
        InlineKeyboardButton("🔙 بازگشت به منوی اصلی", callback_data="back_to_main")
    )
    return markup


# زیرمجموعه‌های ویدیوها برای هر درس
def get_videos_sub_menu(main_key):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    course = VIDEOS_DATA[main_key]
    for sub_key, sub_val in course["sub"].items():
        markup.add(InlineKeyboardButton(f"🔹 {sub_val['title']}", callback_data=f"vid_sub_{sub_key}"))
    markup.add(InlineKeyboardButton("🔙 بازگشت", callback_data="menu_videos"))
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
            url="https://instagram.com/your_instagram_id",
        ),
        InlineKeyboardButton(
            "🟢 کانال بله انجمن علمی ریاضی", url="https://ble.ir/your_bale_id"
        ),
        InlineKeyboardButton(
            " ایتا انجمن علمی ریاضی", url="https://eitaa.com/your_eitaa_id"
        ),
        InlineKeyboardButton(
            " روبیکا انجمن علمی ریاضی",
            url="https://rubika.ir/your_rubika_id",
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
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="📚 **دروس عمومی**\n\nدرس مورد نظر رو انتخاب کن:",
            parse_mode="Markdown",
            reply_markup=get_references_general_menu(),
        )

    elif call.data == "ref_educational":
        bot.answer_callback_query(call.id)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="🎓 **دروس تربیتی**\n\nحوزه مورد نظر رو انتخاب کن:",
            parse_mode="Markdown",
            reply_markup=get_references_educational_menu(),
        )

    elif call.data == "ref_high_school_math":
        bot.answer_callback_query(call.id)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="📚 **کتب درسی ریاضی متوسطه**\n\nمقطع مورد نظر رو انتخاب کن:",
            parse_mode="Markdown",
            reply_markup=get_high_school_math_menu(),
        )

    elif call.data == "hs_middle_school":
        bot.answer_callback_query(call.id)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="📚 **متوسطه اول**\n\nپایه تحصیلی رو انتخاب کن:",
            parse_mode="Markdown",
            reply_markup=get_middle_school_menu(),
        )

    elif call.data == "hs_high_school":
        bot.answer_callback_query(call.id)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="📚 **متوسطه دوم**\n\nرشته و پایه تحصیلی رو انتخاب کن:",
            parse_mode="Markdown",
            reply_markup=get_high_school_sub_menu(),
        )

    elif call.data.startswith("hs_sub_"):
        bot.answer_callback_query(call.id)
        key = call.data.replace("hs_sub_", "")
        found_item = None
        if key in HIGH_SCHOOL_MATH["middle_school"]["sub_items"]:
            found_item = HIGH_SCHOOL_MATH["middle_school"]["sub_items"][key]
        elif key in HIGH_SCHOOL_MATH["high_school"]["sub_items"]:
            found_item = HIGH_SCHOOL_MATH["high_school"]["sub_items"][key]

        if found_item:
            bot.send_message(
                call.message.chat.id,
                f"📚 کتاب مربوط به **{found_item['title']}**:",
                parse_mode="Markdown",
            )
            for f_info in found_item["files"]:
                if f_info["file_id"].startswith("FILE_ID_"):
                    bot.send_message(
                        call.message.chat.id,
                        f"🔸 {f_info['name']} (فایل هنوز بارگذاری نشده است)",
                    )
                else:
                    bot.send_document(
                        call.message.chat.id,
                        f_info["file_id"],
                        caption=f"📚 {f_info['name']}",
                    )

    elif call.data == "menu_videos":
        bot.answer_callback_query(call.id)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="🎬 **بخش ویدیوهای آموزشی**\n\nدرس مورد نظر رو انتخاب کن:",
            parse_mode="Markdown",
            reply_markup=get_videos_main_menu(),
        )

    elif call.data.startswith("vid_main_"):
        bot.answer_callback_query(call.id)
        main_key = call.data.replace("vid_main_", "")
        course_title = VIDEOS_DATA[main_key]["title"]
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f"🎬 **{course_title}**\n\nمبحث مورد نظر رو انتخاب کن:",
            parse_mode="Markdown",
            reply_markup=get_videos_sub_menu(main_key),
        )

    elif call.data.startswith("vid_sub_"):
        bot.answer_callback_query(call.id)
        sub_key = call.data.replace("vid_sub_", "")
        target_sub = None
        for m_key, m_val in VIDEOS_DATA.items():
            if sub_key in m_val["sub"]:
                target_sub = m_val["sub"][sub_key]
                break

        if target_sub:
            bot.send_message(
                call.message.chat.id,
                f"🎥 مبحث: **{target_sub['title']}**\n(تعداد ویدیوها: {target_sub['count']})",
                parse_mode="Markdown",
            )
            for vid in target_sub["videos"]:
                if vid["file_id"].startswith("FILE_ID_"):
                    bot.send_message(
                        call.message.chat.id,
                        f"{vid['caption']}\n(ویدیوی این بخش هنوز بارگذاری نشده است)",
                    )
                else:
                    bot.send_video(
                        call.message.chat.id,
                        vid["file_id"],
                        caption=vid["caption"],
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
        # بررسی پیام‌های پیش‌فرض برای گزینه‌هایی که پیامی به زودی دارند
        if course["title"] in ["معادلات دیفرانسیل", "محاسبات عددی", "بهینه‌سازی", "زبان تخصصی"]:
            bot.send_message(call.message.chat.id, "این امکان به زودی فراهم می‌شود.")
            return

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
        # بررسی قوانین تعداد فایل‌ها برای دروس تخصصی
        title = course['title']
        if title in ["معادلات دیفرانسیل", "محاسبات عددی", "بهینه‌سازی", "زبان تخصصی"]:
            bot.send_message(call.message.chat.id, "این امکان به زودی فراهم می‌شود.")
            return

        bot.send_message(
            call.message.chat.id,
            f"📖 رفرنس و منبع مربوط به **{title}**:",
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

    elif call.data in REFERENCES_GENERAL:
        bot.answer_callback_query(call.id)
        course = REFERENCES_GENERAL[call.data]
        title = course['title']
        if title in ["تاریخ و تمدن", "اندیشه اسلامی", "آیین زندگی", "انقلاب اسلامی", "دانش خانواده", "تاریخ تحلیلی", "تفسیر قرآن", "زبان فارسی"]:
            bot.send_message(call.message.chat.id, "این امکان به زودی فراهم می‌شود.")
            return

        bot.send_message(
            call.message.chat.id,
            f"📖 منبع عمومی مربوط به **{title}**:",
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

    elif call.data in REFERENCES_EDUCATIONAL:
        bot.answer_callback_query(call.id)
        course = REFERENCES_EDUCATIONAL[call.data]
        title = course['title']
        if title in ["آشنایی با تجارب مدارس اسلامی", "دفاع مقدس"]:
            bot.send_message(call.message.chat.id, "این امکان به زودی فراهم می‌شود.")
            return

        bot.send_message(
            call.message.chat.id,
            f"📖 منبع تربیتی مربوط به **{title}**:",
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
        "🔗 لینک‌های مفید 🔵",
        "🎙️ نشریات و پادکست 🟣",
        "🎬 ویدیوهای آموزشی 🔴",
        "📚 چارت‌های درسی 🟢",
        "📄 جزوات 🟡",
        "📖 منابع و رفرنس 🟠",
        "📞 پشتیبانی 🟤",
        "☎️ راه‌های ارتباطی ⚫",
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

    if "چارت‌های درسی" in text:
        bot.send_message(
            message.chat.id,
            "📚 **بخش چارت‌های درسی و برنامه‌ها**\n\nگزینه مورد نظر خودت رو انتخاب کن:",
            parse_mode="Markdown",
            reply_markup=get_chart_menu(),
        )

    elif "ویدیوهای آموزشی" in text:
        bot.send_message(
            message.chat.id,
            "🎬 **بخش ویدیوهای آموزشی**\n\nدرس مورد نظر رو انتخاب کن:",
            parse_mode="Markdown",
            reply_markup=get_videos_main_menu(),
        )

    elif "جزوات" in text:
        bot.send_message(
            message.chat.id,
            "📄 **بانک جزوات ریاضی**\n\nکدوم درس رو نیاز داری؟",
            parse_mode="Markdown",
            reply_markup=get_handouts_menu(),
        )

    elif "منابع و رفرنس" in text:
        bot.send_message(
            message.chat.id,
            "📖 **بخش منابع و رفرنس‌ها**\n\nدسته‌بندی مورد نظر رو انتخاب کن:",
            parse_mode="Markdown",
            reply_markup=get_references_main_menu(),
        )

    elif "نشریات و پادکست" in text:
        bot.send_message(
            message.chat.id,
            "🎙 **نشریات و پادکست‌های انجمن علمی ریاضی**\n\nبخش مورد نظر رو انتخاب کن:",
            parse_mode="Markdown",
            reply_markup=get_podcasts_magazines_menu(),
        )

    elif "لینک‌های مفید" in text:
        bot.send_message(
            message.chat.id,
            "🔗 **لینک‌های مهم و کاربردی دانشگاه:**\n\nبخش مورد نظر رو انتخاب کن:",
            parse_mode="Markdown",
            reply_markup=get_useful_links_main_menu(),
        )

    elif "پشتیبانی" in text:
        sup_text = (
            "📞 **ارتباط با پشتیبانی و ارسال فایل**\n\nهر گونه پیشنهاد، انتقاد یا"
            " فایلی داری بفرست تا به دست ادمین برسه: 👇"
        )
        sent_msg = bot.send_message(message.chat.id, sup_text, parse_mode="Markdown")
        bot.register_next_step_handler(sent_msg, receive_user_file_or_message)

    elif "راه‌های ارتباطی" in text:
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
