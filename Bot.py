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
        "title": "چارت درسی ورودی مهر 1402 آموزش ریاضی",
        "file_id": "BQACAgQAAxkBAAIBd2pyGRlOvSXFK05P9oSy0y-bDuSqAAJlHAACIvyRU-zB1RvtSi1APQQ",
    },
    "chart_1403": {
        "title": "چارت درسی ورودی مهر 1403 آموزش ریاضی",
        "file_id": "BQACAgQAAxkBAAIBf2pyGZoPejTCupCIwBYro2u2adbJAAJmHAACIvyRUzmxKA40ApeMPQQ",
    },
    "chart_1404": {
        "title": "چارت درسی ورودی بهمن 1404 آموزش ریاضی",
        "file_id": "BQACAgQAAxkBAAIBgWpyGavIchw4P9ylXpSOKMmz6t3aAAJnHAACIvyRUw4CKNWJkWB8PQQ",
    },
    "chart_bachelor": {
        "title": "فایل برنامه درسی رشته کارشناسی آموزش ریاضی",
        "file_id": "BQACAgQAAxkBAAIBDWpyCr87cp8z5QHP_hGzmlQ5XTHzAAIbEwACH7LBUSWnbHWURFFgPQQ",
    },
    "chart_calendar": {
        "title": "تقویم آموزشی سال 1405-1406",
        "file_id": "FILE_ID_EDUCATION_CALENDAR",
    },
}

# بخش جزوات با تعداد فایل‌های مشخص شده برای هر درس
BOOKS_DATA = {
    "book_intro": {
        "title": "ریاضی مقدماتی",
        "files": [
            {"name": "جزوه ریاضی مقدماتی -فایل 1 ", "file_id": "BQACAgQAAxkBAAIBqWpyIN_vSe4B9EN0JPmBJNQ206soAAIpHgACByd4UzfZyqXy7gABbj0E"},
            {"name": "جزوه ریاضی مقدماتی - فایل 2", "file_id": "BQACAgQAAxkBAAIBrWpyITquRZi7fCuVEr-gyri55Q0VAAL9HQACByd4U7LaJvJY6HDIPQQ"},
        ],
    },
    "book_math1": {
        "title": "ریاضی عمومی ۱",
        "files": [
            {"name": "📝  ریاضی عمومی ۱ - جزوه اول", "file_id": "BQACAgQAAxkBAAIBq2pyIOiPIzy-Z_99wScmKftEvPMBAAIWHgACByd4Uwt6o3ibHtClPQQ"},
            {"name": "📝  ریاضی عمومی ۱ - جزوه دوم", "file_id": "BQACAgQAAxkBAAIBsWpyIUz51c3prfmHgq4GLjkjgRvRAAI1HgACByd4UxnvhreD2NcpPQQ"},
            {"name": "📝  ریاضی عمومی ۱ - ادامه جزوه دوم", "file_id": "BQACAgQAAxkBAAIBs2pyIVGMDbk5hUm1kwdyvJSDsFgrAAI2HgACByd4Uzjx_wxA9FBOPQQ"},
        ],
    },
    "book_math2": {
        "title": "ریاضی عمومی ۲",
        "files": [{"name": "📝 جزوه ریاضی عمومی ۲", "file_id": "BQACAgQAAxkBAAIBtWpyIVroF9caJzufTnTfmGLR7P4NAAMeAAIHJ3hTZM6kagevN149BA"}],
    },
    "book_eq": {
        "title": "معادلات دیفرانسیل",
        "files": [{"name": "📝 جزوه معادلات دیفرانسیل", "file_id": "BQACAgQAAxkBAAIBt2pyIWMFQK8gs2Et7S7k3P-AXzWsAAIvHgACByd4U7BnrjKIVXWTPQQ"}],
    },
    "book_probability": {
        "title": "مبانی احتمال",
        "files": [{"name": "جزوه مبانی احتمال", "file_id": "BQACAgQAAxkBAAIBz2pyIdzaLK6QouNIZ6Au_gxpZzEvAAIwHgACByd4U_QUjA9F8KGePQQ"}],
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
        "files": [{"name": "جزوه جبر خطی", "file_id": "BQACAgQAAxkBAAIBzWpyIdOjejA6L3mVYhS6XvdKacJ8AAIIHgACByd4U91rb40dnivlPQQ"}],
    },
    "book_discrete": {
        "title": "ریاضیات گسسته",
        "files": [{"name": "جزوه ریاضیات گسسته", "file_id": "BQACAgQAAxkBAAIBy2pyIcgWfbJelm-PRKU7pylrmw-ZAAICHgACByd4U6Q0xRZUDt_zPQQ"}],
    },
    "book_geometry": {
        "title": "مبانی هندسه",
        "files": [{"name": "جزوه مبانی هندسه", "file_id": "BQACAgQAAxkBAAIBxWpyIa6PbwoMypHan2yY0r9FP1TrAAL2HQACByd4U8877A99o_jFPQQ"}],
    },
    "book_proof": {
        "title": "مقدمه‌ای بر اثبات",
        "files": [
            {"name": "جزوه مقدمه‌ای بر اثبات - فایل ۱", "file_id": "BQACAgQAAxkBAAIBx2pyIbjNRX2jpA39CVAKzVl6CZzOAAIsHgACByd4U_acq0vbw666PQQ"},
            {"name": "جزوه مقدمه‌ای بر اثبات - فایل ۲", "file_id": "BQACAgQAAxkBAAIByWpyIb0-7E_Ir726Y17BnU-V5kw5AAI7HgACByd4U-zISaD3nIUXPQQ"},
        ],
    },
    "book_number": {
        "title": "نظریه اعداد",
        "files": [
            {"name": "📄 جزوه اول نظریه اعداد - بخش ۱", "file_id": "BQACAgQAAxkBAAIBu2pyIXV2RtcCqCmkMwfYuvruAcUkAAIyHgACByd4U2XKykzn1hLuPQQ"},
            {"name": "📄 جزوه اول نظریه اعداد - بخش ۲", "file_id": "BQACAgQAAxkBAAIBvWpyIXuDPQfKOv_NFjhETvU465yLAAIzHgACByd4U7D6xmcgo_USPQQ"},
            {"name": "📄 جزوه اول نظریه اعداد - بخش ۳", "file_id": "BQACAgQAAxkBAAIBv2pyIYOJNk-cEX-Y6UXPykakfzyvAAIHHgACByd4U3LK5f1Y_BWzPQQ"},
            {"name": "📄 جزوه دوم نظریه اعداد - بخش 1", "file_id": "BQACAgQAAxkBAAIBwWpyIY_KsSvPPVkW7D-IM0AnL3s6AAIXHgACByd4U-vSMOZrw2YEPQQ"},
            {"name": "📄 جزوه دوم نظریه اعداد - بخش 2", "file_id": "BQACAgQAAxkBAAIBw2pyIZ_LmrAln5FmnMJxXTa6LjKZAAIxHgACByd4U3nQ3hlucQtmPQQ"},
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

# منابع و رفرنس‌ها - دروس تخصصی ریاضی
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
            {"name": "📖 کتاب مرجع مبانی احتمال - شلدون راس ", "file_id": "BQACAgQAAxkBAAIEE2pzHTLBzQXwyud5S8WZ5Wnq02zoAAI3GQACdsrwUrizUoGQ8VAXPQQ"},
            {"name": "📖 کتاب مرجع مبانی احتمال - حل مسائل ", "file_id": "BQACAgQAAxkBAAIEFWpzHTeY7l_lhGMCubPQdsXc6dC0AAI4GQACdsrwUoowH_Skwe6KPQQ"},
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
            {"name": "📖 کتاب مرجع ریاضی عمومی ۱ - آدامز ", "file_id": "BQACAgQAAxkBAAIEA2pzHL07vfatStBYitIDdN-pEaaFAAJbEQACnptgUvMvmiHc64O3PQQ"},
            {"name": "📖 کتاب مرجع ریاضی عمومی ۱ - حل مسائل آدامز ", "file_id": "BQACAgQAAxkBAAIEBWpzHMWkwIEESRrj-p7uxdySNyPiAAKVHgACF3KZU9XsZQW6FjpmPQQ"},
            {"name": "📖 کتاب مرجع ریاضی عمومی ۱ - توماس ", "file_id": "BQACAgQAAxkBAAIEB2pzHMvcehVjvIfNVa76CbJNJkrAAAJAAAO8XXhTXkt56QcU5NY9BA"},
            {"name": "📖 کتاب مرجع ریاضی عمومی ۱ - حل مسائل توماس ", "file_id": "BQACAgQAAxkBAAIECWpzHM8p78BORxVZWE85AnYb1_TqAAIKAAOJ1X8HEe1KXrDOltI9BA"},
            {"name": "📖 کتاب مرجع ریاضی عمومی ۱ - انتشارات قلم ", "file_id": "BQACAgQAAxkBAAIEC2pzHNWHTX6rrh6wRXfkyKzmz1R5AALJEwACK0QQUqbq_vfdZzBUPQQ"},
            {"name": "📖 کتاب مرجع ریاضی عمومی ۱ - فرامرزی ", "file_id": "BQACAgQAAxkBAAIEDWpzHOAcbI6Kl7zPKV02t55OINU3AAKWHgACF3KZUzBOAcchHlAvPQQ"},
        ],
    },
    "ref_math2": {
        "title": "ریاضی عمومی ۲",
        "files": [
            {"name": "📖 کتاب مرجع ریاضی عمومی ۲ - استوارت ویرایش 6 ", "file_id": "BQACAgQAAxkBAAIED2pzHRwN48rm2vd4YXe70kQ_qhbFAAIiGwACYyXIUg49N7oqJT60PQQ"},
            {"name": "📖 کتاب مرجع ریاضی عمومی ۲ - حل مسائل ", "file_id": "BQACAgQAAxkBAAIEEWpzHR8hjfcV7XbvIUEZiXjema_7AAIqGwACYyXIUtbtV4Qdrx53PQQ"},
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
            {"name": "📖 کتاب مرجع جبرخطی -  شولتز", "file_id": "BQACAgQAAxkBAAIEF2pzHT79K2Ox6C0SzLv0yZk-vgrlAAK-FQACFurJU1H_4MAxBAjhPQQ"},
            {"name": "📖 کتاب مرجع جبرخطی - هافمن ", "file_id": "BQACAgQAAxkBAAIEGWpzHUL7iOERh5Bq7YIP4p-NeYDRAAJiFQADyrBS4stqvxrxM3w9BA"},
        ],
    },
    "ref_algebraic_structures": {
        "title": "ساختارهای جبری",
        "files": [
            {"name": "📖 کتاب مرجع ساختارهای جبری ", "file_id": "BQACAgQAAxkBAAIEH2pzHVEWSnV6aW_5U8YMCOjhh5Y5AALsHwACuQGIUMPtkQzE_9egPQQ"},
            {"name": "📖 کتاب مرجع ساختارهای جبری - حل مسائل ", "file_id": "BQACAgQAAxkBAAIEIWpzHVQo4bhD-x-CBfltHBw61xmdAAJIHwACuQGQUHLVwRg89dxqPQQ"},
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
        "files": [{"name": "📖 کتاب مرجع نظریه اعداد", "file_id": "BQACAgQAAxkBAAIEG2pzHUadAAFvxFGzll-fK2YQ6ZY6vwAC1BoAAkF_iVGkrwVX2UYa8j0E"}],
    },
    "ref_math_art": {
        "title": "ریاضی و هنر",
        "files": [{"name": "📖 کتاب مرجع ریاضی و هنر", "file_id": "BQACAgQAAxkBAAIEHWpzHU080lTB8gV7wfq_PNdk-GISAAICFwAC0LvZUakZNz1cjUxuPQQ"}],
    },
}

# منابع و رفرنس‌ها - دروس عمومی (ترتیب جدید)
REFERENCES_GENERAL = {
    "gen_life_tradition": {
        "title": "آیین زندگی",
        "files": [{"name": "📖 آیین زندگی | احمدحسین شریفی", "file_id": "BQACAgQAAxkBAAIJ7mp3DWuo4ee7USVhr0zKda-bOZ6fAALCCAACv2C4Umh4E7EGL-HsPQQ"}],
    },
    "gen_islamic_thought": {
        "title": "اندیشه اسلامی",
        "files": [
            {"name": "📖 اندیشه اسلامی 1 آیت الله سبحانی", "file_id": "BQACAgQAAxkBAAIJ6mp3DVPwygMzVLcScXfeSs8_EcOoAALfAQACs-yAU4nhXqHVNOyhPQQ"},
            {"name": "📖 ندیشه اسلامی 2 آیت الله سبحانی", "file_id": "BQACAgQAAxkBAAIJ7Gp3DVqCsIO1uhcXRmlwS1LAy6MVAAK7AAPIdVoHIBhCT4vc-9E9BA"},
        ],
    },
    "gen_persian": {
        "title": "زبان فارسی",
        "files": [{"name": "📖 زبان فارسی | یدالله بهمنی - رسول چهرقانی", "file_id": "BQACAgQAAxkBAAIJ_Gp3Dnqdy9BxVUMrWO3GwZq7ffIMAALEBwAC30XxUiIPK_42OhNSPQQ"}],
    },
    "gen_english": {
        "title": "زبان انگلیسی",
        "files": [
            {"name": "📖  زبان انگلیسی - فایل خام", "file_id": "BQACAgQAAxkBAAIDO2py_Hu9oCpeFWk6FrlJOv8pmALNAAKIGwAC3yZIUnzyjk7voUMQPQQ"},
            {"name": "📖  زبان انگلیسی - فایل حل شده", "file_id": "AIDPWpy_IN9M_eZtT9rKTm8pbNabp9PAAMbAAJNriFSLJmTKJr3zCU9BA"},
        ],
    },
    "gen_family_knowledge": {
        "title": "دانش خانواده و جمعیت",
        "files": [{"name": "📖 دانش خانواده و جمعیت | زهرا آیت‌اللهی", "file_id": "BQACAgQAAxkBAAIJ8Gp3DXApyI55HPeP99UhZvRjjTq0AALcCQACFXzxUlJAmPDf-t1EPQQ"}],
    },
    "gen_islamic_revolution": {
        "title": "انقلاب اسلامی",
        "files": [{"name": "📖 انقلاب اسلامی | ویراست دوم - محمدرحیم عیوضی - محمدجواد هراتی", "file_id": "BQACAgQAAxkBAAIJ-Gp3Dmz5d0Gq4T4BAdsiJ_uDBjhxAAKuHwACxhS5U-T7pCDXVvkuPQQ"}],
    },
    "gen_health": {
        "title": "سلامت و بهداشت",
        "files": [
            {"name": "📖 کتاب سلامت و بهداشت جمعی از نویسندگان", "file_id": "BQACAgQAAxkBAAIKImp3D54Kek1unithtt4CnMSixFq-AALiGwACohVBUpmFeAIpwkZjPQQ"},
            {"name": "📖 جزوه دکتر باقری", "file_id": "BQACAgQAAxkBAAIKJGp3D6YTTpvw1pXXcKu-MunRoBMzAAI6HQACphI4UgcY-oxEF_ZsPQQ"},
            {"name": "📖 جزوه دکتر فائزه فاضلی", "file_id": "AIDQWpy_ItETnBDxUpa3Td0K6_WKBkhAAKCHAACZFWwUtBC815X0cfiPQQ"},
            {"name": "📖 خلاصه جزوه دکتر فاضلی", "file_id": "BQACAgQAAxkBAAIDP2py_IiRRYACe5moHIO7Os15zsCAAAK0GgACI5aoUvZcrgWGu3FpPQQ"},
        ],
    },
    "gen_analytical_history": {
        "title": "تاریخ تحلیلی صدراسلام",
        "files": [{"name": "📖 منبع تاریخ تحلیلی صدراسلام", "file_id": "BQACAgQAAxkBAAIJ-mp3DnQCQMk11oDoEyom6NMsBTjUAAKXAAMYAAEPBUg4L20ERLUaPQQ"}],
    },
    "gen_quran_interpretation": {
        "title": "تفسیر موضوعی قرآن",
        "files": [
            {"name": "📖 کتاب تقسیر موضوعی قرآن کریم اثر جمعی از نویسندگان", "file_id": "BQACAgQAAxkBAAIJ8mp3DlG0GO6sMFUzuyvLwN8-ZtWMAAKqHwACxhS5U-IywexTQNw2PQQ"},
            {"name": "📖 جزوه تفسیر موضوعی قرآن", "file_id": "BQACAgQAAxkBAAIJ9Gp3DlWBdKddfvd5NgsLmak_xJHiAAKrHwACxhS5Uw_VOj_Jp_mmPQQ"},
        ],
    },
    "gen_history_civilization": {
        "title": "تاریخ فرهنگ و تمدن",
        "files": [{"name": "📖 کتاب تاریخ فرهنگ و تمدن اثر فاطمه جان‌احمدی", "file_id": "BQACAgQAAxkBAAIJ9mp3DlzxU92e3GKU3Pd1sa7pgFELAAL2CAACIbBoUXlYVW6fd8OPPQQ"}],
    },
}

# منابع و رفرنس‌ها - دروس تربیتی (ترتیب و تعداد فایل‌های جدید)
REFERENCES_EDUCATIONAL = {
    "edu_educational_biography": {
        "title": "سیره تربیتی پیامبر و اهل بیت",
        "files": [{"name": "📖 کتاب سیره تربیتی پیاکبر اثر داوودی و حسینی‌زاده", "file_id": "BQACAgQAAxkBAAIJ_mp3Dox7LfxkOlHEKvgIPSBflK2mAAKfCQACLZ_oUeHEnejO5dV2PQQ"}],
    },
    "edu_educational_psychology": {
        "title": "روانشناسی تربیتی",
        "files": [{"name": "📖 روانشناسی پرورشی نوین دکتر سیف", "file_id": "BQACAgQAAxkBAAIKAAFqdw6kHU6x5-iQs_DfZ2ayzgZC4QACTg8AAoIWoFFqtsURavL5QT0E"}],
    },
    "edu_tech_application": {
        "title": "کاربست فناوری در یادگیری",
        "files": [],  # پیام اختصاصی بررسی می‌شود
    },
    "edu_educational_philosophy": {
        "title": "فلسفه تربیتی اسلام",
        "files": [
            {"name": "📖 منبع فلسفه تربیتی اسلام - فایل ۱", "file_id": "BQACAgQAAxkBAAIKAmp3Dr_Zfmx6mdJt1TTF9C4QBoQvAAJTHwACV2WpUdpYGk4EozkAAT0E"},
            {"name": "📖 منبع فلسفه تربیتی اسلام - فایل ۲", "file_id": "BQACAgQAAxkBAAIKBGp3DsXT_kxPB_9OyzLO-HdCd6nYAAK_EgAC_kbZUJtOXBD5wG4aPQQ"},
        ],
    },
    "edu_learning_theories": {
        "title": "نظریه‌های یادگیری و آموزش",
        "files": [
            {"name": "📖 فایل پاورپوینت بخش اول", "file_id": "BQACAgQAAxkBAAIKCGp3DukynTl0PHtpd6ABhja4m_guAAKsFwACIiPBUBTL8jvKkfexPQQ"},
            {"name": "📖 فایل پاورپوینت بخش دوم", "file_id": "BQACAgQAAxkBAAIKCmp3Du17F23tPGLgRutNQ3MIxR7jAAKtFwACIiPBUMvw8nM61AhbPQQ"},
            {"name": "📖 کتاب مقدمه‌ای بر نظریه یادگیری دکتر سیف", "file_id": "BQACAgQAAxkBAAIKDGp3DvI1zUPSBbPthoN5wCc0GvEYAAIhCwACULVRUfqRFQ30xMVkPQQ"},
            {"name": "📖 جزوه آقای محمدامین فتحی‌پور", "file_id": "BQACAgQAAxkBAAIKDmp3DvbVU61-EFQkoWHoLA96_28YAAJVFAAC6gapU_YZYrX3075BPQQ"},
        ],
    },
    "edu_docs_laws": {
        "title": "اسناد و قوانین سازمان آموزش و پرورش",
        "files": [{"name": "📖 کتاب سازمان و قوانین آموزش و پرورش ایران اثر احمد صافی", "file_id": "BQACAgQAAxkBAAIKEGp3DwynoYeDalCm981SBpsyjjZtAAK-CwAChbD4UpjoJ-EpXYNZPQQ"}],
    },
    "edu_school_management": {
        "title": "مدیریت آموزشگاهی",
        "files": [{"name": "📖 کتاب مدیریت کلاس اثر دکتر سیف و دکتر سرمدی", "file_id": "BQACAgQAAxkBAAIKFmp3D1brTk_7S6YmeQQfdhGKXzkaAAI2EQAC318xUJyPDxhB3vBJPQQ"}],
    },
    "edu_religious_training": {
        "title": " تربیت دینی کودک و نوجوان در اسلام",
        "files": [
            {"name": "📖 جزوه تربیت دینی دکتر انارکی", "file_id": "BQACAgQAAxkBAAIDOWpy_HYeCeZgSI9hFlSA_lyZ8eOyAAJ0IAACb_gIUnqapd3HnwcjPQQ"},
            {"name": "📖 تربیت دینی در دوره دبستان و دبیرستان اثر محمود نوذری", "file_id": "BQACAgQAAxkBAAIKGGp3D2Kb2mK3jW2ny2YhflEDktCUAAIvEAAC4NupUosbP8okb22_PQQ"},
        ],
    },
    "edu_teacher_ethics": {
        "title": "اخلاق معلمی از دیدگاه اسلام",
        "files": [
            {"name": "📖 جزوه اخلاق معلمی از دیدگاه اسلام دکتر انارکی", "file_id": "BQACAgQAAxkBAAIDNWpy_Gxw7vnrQ2Jj4DMIoQ8JLL7JAAJDHAACI5awUvGXLmnys5PBPQQ"},
            {"name": "📖 کتاب اخلاق حرفه‌ای در تربیت اثر فاطمه وجدانی", "file_id": "BQACAgQAAxkBAAIKGmp3D3P7iW6Xfrx7Wy89xI_z6lQqAALNHQACQa-oUhXjkZMeg4s4PQQ"},
            {"name": "📖 کتاب اخلاق حرفه‌ای در مدرسه اثر جمعی از نویسندگان", "file_id": "BQACAgQAAxkBAAIKHGp3D4Kj4hthoPOrFi9mNqXDeuh8AAI2DAACY_4AAVCBPWFYlyQblD0E"},
        ],
    },
    "edu_islamic_schools_exp": {
        "title": " آشنایی با تجارب مدارس اسلامی معاصر",
        "files": [{"name": "📖 جزوه تجارب مدارس اسلامی دکتر انارکی", "file_id": "BQACAgQAAxkBAAIKEmp3DxHeGhkd3qH-F8edkWoOBT2SAAKZHAACZFWwUizHy1VotW6KPQQ"}],
    },
    "edu_counseling_principles": {
        "title": "اصول و روش‌های راهنمایی و مشاوره",
        "files": [{"name": "📖 کتاب اصول مشاوره اثر دکتر شفیع‌آبادی", "file_id": "BQACAgQAAxkBAAIDM2py_GjHtInvBUbv87afjrCVKfvvAAIFBwACXHXRUMMV5OMkhIgKPQQ"}],
    },
    "edu_islamic_training_challenges": {
        "title": "چالش‌های تربیت اسلامی در دنیای معاصر",
        "files": [{"name": "📖 جزوه چالش های تربیت اسلامی دکتر انارکی", "file_id": "BQACAgQAAxkBAAIDN2py_HHJ9cEB51S3SUauHHr0AZa2AAJdJQAC5U-hUuCIuR2EeyklPQQ"}],
    },
    "edu_sacred_defense": {
        "title": "آشنایی با ارزش‌های تربیتی دفاع مقدس",
        "files": [{"name": "📖 کتاب آشنایی با علوم و معارف دفاع مقدس اثر مرادپیری و شربتی", "file_id": "BQACAgQAAxkBAAIKIGp3D5U_mRM8lx5-P1dyW_t31S0PAAJTEAACgJFIUnbCAXKdOb9BPQQ"}],
    },
    "edu_sociology": {
        "title": "جامعه شناسی آموزش و پرورش",
        "files": [{"name": "📖 کتاب جامعه شناسی آموزش و پرورش اثر محمود شارع‌پور", "file_id": "BQACAgQAAxkBAAIKFGp3D04Oq1NKkm5m-_UmBuUPnggyAAK5EQACBTIgU2Gyhy7zqbSuPQQ"}],
    },
    "edu_quran_recitation": {
        "title": "تجوید و روخوانی قرآن",
        "files": [
            {"name": "📖 جزوه تجوید قرآن استاد شرفی", "file_id": "BQACAgQAAxkBAAIKHmp3D4oljzCMjAor0RrmFppmYcIKAAJ8HAACZFWwUjkRNfdvaDYWPQQ"},
            {"name": "📖 جزوه روخوانی و روانخوانی قرآن استاد شرفی", "file_id": "FILE_ID_EDU_QURAN_REC_2"},
        ],
    },
    "edu_quran_concepts": {
        "title": "مفاهیم قرآنی",
        "files": [{"name": "📖 جزوه استاد زهره اکبری", "file_id": "FILE_ID_EDU_QURAN_CON"}],
    },
}

# کتب درسی ریاضی متوسطه
HIGH_SCHOOL_MATH = {
    "middle_school": {
        "title": "متوسطه اول",
        "sub_items": {
            "grade_7": {
                "title": "هفتم",
                "files": [
                    {"name": "📚 کتاب ریاضی هفتم", "file_id": "BQACAgQAAxkBAAIC6mpy9iWHmTmHsu8FLhypYYgS6T9NAAI5FQACXUUhU-9UPkUygBn4PQQ"},
                    {"name": "📚 راهنمای معلم ریاضی هفتم", "file_id": "BQACAgQAAxkBAAIC7Gpy9jAxhQpcPPWlAhmK_oDNiaShAAJRFQACXUUhU1CyE53WE5GdPQQ"},
                ],
            },
            "grade_8": {
                "title": "هشتم",
                "files": [
                    {"name": "📚 کتاب ریاضی هشتم", "file_id": "BQACAgQAAxkBAAIC8Wpy9kpbJp5R-x5Y7QOq7i_u1BemAAI6FQACXUUhU1RRrvath3-IPQQ"},
                    {"name": "📚 راهنمای معلم ریاضی هشتم", "file_id": "BQACAgQAAxkBAAIC82py9lNJR79JKfZ_AhNl7WlAD7C4AAJSFQACXUUhU3V7xmHsLMpMPQQ"},
                ],
            },
            "grade_9": {
                "title": "نهم",
                "files": [
                    {"name": "📚 کتاب ریاضی نهم", "file_id": "BQACAgQAAxkBAAIC9Wpy9lmcBCALYYshRxCmk5JvI6lDAAI8FQACXUUhU_eQGvFQNY4bPQQ"},
                    {"name": "📚 راهنمای معلم ریاضی نهم", "file_id": "BQACAgQAAxkBAAIC92py9l-W2b7dUUvioB2LqboBpDsDAAJHFQACXUUhUxLBPgRv1eLBPQQ"},
                ],
            },
        },
    },
    "high_school_fields": {
        "title": "متوسطه دوم",
        "streams": {
            "experimental": {
                "title": "رشته علوم تجربی",
                "sub_items": {
                    "10_exp": {
                        "title": "ریاضی دهم تجربی",
                        "files": [
                            {"name": "📚 کتاب ریاضی دهم تجربی ", "file_id": "BQACAgQAAxkBAAIDDWpy9rEsL2BZPrAHD8Pba94abzepAAI9FQACXUUhUwqZgTZsiMcQPQQ"},
                            {"name": "📚 راهنمای معلم ریاضی دهم تجربی  ", "file_id": "BQACAgQAAxkBAAIDD2py9rgOi7TGpN5Fltx4wU38LDJ0AAJIFQACXUUhUwGY2z25SkbOPQQ"},
                        ],
                    },
                    "11_exp": {
                        "title": "ریاضی یازدهم تجربی",
                        "files": [
                            {"name": "📚 کتاب ریاضی یازدهم تجربی ", "file_id": "BQACAgQAAxkBAAIDJWpy-g6iLYComA_nhS5XDv2wTmGGAAJjHgACF3KZU20ZTDAHJoefPQQ"},
                            {"name": "📚 راهنمای معلم ریاضی یازدهم تجربی ", "file_id": "BQACAgQAAxkBAAIDJ2py-hXLhB_MJUQC1ZUj-wVqYpz8AAJeHgACF3KZU9ayn6apL-2WPQQ"},
                        ],
                    },
                    "12_exp": {
                        "title": "ریاضی دوازدهم تجربی",
                        "files": [
                            {"name": "📚 کتاب ریاضی دوازدهم تجربی ", "file_id": "BQACAgQAAxkBAAIDKWpy-h0Bih1bY3-G6jpkluPeXZ3zAAJfHgACF3KZU7x_OsnuqrgQPQQ"},
                            {"name": "📚 راهنمای معلم ریاضی دوازدهم تجربی  ", "file_id": "BQACAgQAAxkBAAIDK2py-iJIzvnv0_s-ZgMLT5QjmanlAAJaHgACF3KZU7PVKWzxCzdVPQQ"},
                        ],
                    },
                },
            },
            "mathematics": {
                "title": "رشته ریاضی و فیزیک",
                "sub_items": {
                    "10_math": {
                        "title": "ریاضی دهم ریاضی",
                        "files": [
                            {"name": "📚 کتاب ریاضی دهم ریاضی", "file_id": "BQACAgQAAxkBAAIDDWpy9rEsL2BZPrAHD8Pba94abzepAAI9FQACXUUhUwqZgTZsiMcQPQQ"},
                            {"name": "📚 راهنمای معلم ریاضی دهم ریاضی", "file_id": "BQACAgQAAxkBAAIDD2py9rgOi7TGpN5Fltx4wU38LDJ0AAJIFQACXUUhUwGY2z25SkbOPQQ"}
                        ],
                    },
                    "10_geometry": {
                        "title": "هندسه دهم",
                        "files": [
                            {"name": "📚 کتاب هندسه دهم", "file_id": "BQACAgQAAxkBAAIC-Wpy9mh8tVVUYz3Dh_GvgtOrNXAxAAJAFQACXUUhU-ZUC0sTs8AiPQQ"},
                            {"name": "📚 راهنمای معلم هندسه دهم", "file_id": "BQACAgQAAxkBAAIC-2py9m9R9HrWGzhMlEN82cd_qxpWAAJLFQACXUUhUwbjdMVz7g6nPQQ"}
                        ],
                    },
                    "11_calculus": {
                        "title": "حسابان یازدهم",
                        "files": [
                            {"name": "📚 کتاب حسابان یازدهم", "file_id": "BQACAgQAAxkBAAIDEWpy9r2OfKfjHg01ScNoAAE2k_UfqAACPhUAAl1FIVO03MhawtPtvT0E"},
                            {"name": "📚 راهنمای معلم حسابان یازدهم", "file_id": "BQACAgQAAxkBAAIDE2py9sUZ3VF7q4fBIdHgR2v3ZFPkAAJJFQACXUUhU5XXnv2rkogTPQQ"}
                        ],
                    },
                    "11_geometry": {
                        "title": "هندسه یازدهم",
                        "files": [
                            {"name": "📚 کتاب هندسه یازدهم", "file_id": "BQACAgQAAxkBAAIC_Wpy9naN2ncjph_IHzAHMrz-ioP5AAJBFQACXUUhU0Bkcw0EZb9iPQQ"},
                            {"name": "📚 راهنمای معلم هندسه یازدهم", "file_id": "BQACAgQAAxkBAAIC_2py9n4jerkmXi5rnb08JHdghy8oAAJMFQACXUUhUyS3LxsoUadYPQQ"}
                        ],
                    },
                    "11_stats": {
                        "title": "آمار و احتمال یازدهم",
                        "files": [
                            {"name": "📚 کتاب آمار و احتمال یازدهم", "file_id": "BQACAgQAAxkBAAIDBWpy9pf8zQht1SSG-BGUwRC6bVdKAAJDFQACXUUhU-JqzLydR_V3PQQ"},
                            {"name": "📚 راهنمای معلم آمار و احتمال یازدهم", "file_id": "BQACAgQAAxkBAAIDB2py9p5iCTQF6oraO3m93CE8Mwz3AAJOFQACXUUhU2Wi3p1Yb8gLPQQ"}
                        ],
                    },
                    "12_calculus": {
                        "title": "حسابان دوازدهم",
                        "files": [
                            {"name": "📚 کتاب حسابان دوازدهم", "file_id": "BQACAgQAAxkBAAIDFWpy9ssITvVGqMooDoPhbK-Lvvi9AAI_FQACXUUhUwZNRtZH1vf8PQQ"},
                            {"name": "📚 راهنمای معلم حسابان دوازدهم", "file_id": "BQACAgQAAxkBAAIDF2py9tJFOfHIcZB5FRaJlu9L_TBBAAJKFQACXUUhUxbp7hAMOgIUPQQ"}
                        ],
                    },
                    "12_geometry": {
                        "title": "هندسه دوازدهم",
                        "files": [
                            {"name": "📚 کتاب هندسه دوازدهم", "file_id": "BQACAgQAAxkBAAIDAWpy9oV5QeLTQJF5kzNb3CbDwXxWAAJCFQACXUUhU_wl5Xo5W4rwPQQ"},
                            {"name": "📚 راهنمای معلم هندسه دوازدهم", "file_id": "BQACAgQAAxkBAAIDA2py9oscWOXqQSDP0GuYGdo2BsRpAAJNFQACXUUhU8j4nRY8zCquPQQ"}
                        ],
                    },
                    "12_discrete": {
                        "title": "ریاضیات گسسته دوازدهم",
                        "files": [
                            {"name": "📚 کتاب ریاضیات گسسته دوازدهم", "file_id": "BQACAgQAAxkBAAIDCWpy9qSsyl2Wy6lxnk3foCLfZeUoAAJEFQACXUUhUxeJFVJOcnEgPQQ"},
                            {"name": "📚 راهنمای معلم ریاضیات گسسته دوازدهم", "file_id": "BQACAgQAAxkBAAIDC2py9qhzGhg-vnXAy4qiJE5d5gtJAAJQFQACXUUhU7SSTSc0fv54PQQ"}
                        ],
                    },
                },
            },
            "humanities": {
                "title": "رشته علوم انسانی",
                "sub_items": {
                    "10_humanities": {
                        "title": "ریاضی و آمار دهم",
                        "files": [
                            {"name": "📚 کتاب ریاضی و آمار دهم انسانی ", "file_id": "BQACAgQAAxkBAAIDGWpy-eByuI69I-BoRyUcX3YSNTbuAAJgHgACF3KZU190B8idcFZEPQQ"},
                            {"name": "📚 راهنمای معلم ریاضی و آمار دهم انسانی ", "file_id": "BQACAgQAAxkBAAIDG2py-eZauhimNP_BtYyU-IV5XwqrAAJbHgACF3KZUzMO8N7Sg5dJPQQ"},
                        ],
                    },
                    "11_humanities": {
                        "title": "ریاضی و آمار یازدهم",
                        "files": [
                            {"name": "📚 کتاب ریاضی و آمار یازدهم انسانی ", "file_id": "BQACAgQAAxkBAAIDHWpy-fCV2ZT_9B6ZYSUKb4jgsUOCAAJiHgACF3KZU8Xp-pbWYj51PQQ"},
                            {"name": "📚 راهنمای معلم ریاضی و آمار یازدهم انسانی ", "file_id": "BQACAgQAAxkBAAIDH2py-fRl6hWoJPmiKvtlhh578ckwAAJdHgACF3KZU6HblJlNEV8vPQQ"},
                        ],
                    },
                    "12_humanities": {
                        "title": "ریاضی و آمار دوازدهم",
                        "files": [
                            {"name": "📚 کتاب ریاضی و آمار دوازدهم انسانی  ", "file_id": "BQACAgQAAxkBAAIDIWpy-fwz8ZLjrKu2n5AEVkDBX9B_AAJhHgACF3KZUyecycfI6MCHPQQ"},
                            {"name": "📚 راهنمای معلم ریاضی و آمار دوازدهم انسانی ", "file_id": "BQACAgQAAxkBAAIDI2py-gUCWTLVBZUPaArqtkOYYVwAA1weAAIXcplTTLBu6eOrjd49BA"},
                        ],
                    },
                },
            },
        },
    },
}

# بخش ویدیوهای آموزشی
VIDEOS_DATA = {
    "vid_math1": {
        "title": "ریاضی عمومی ۱",
        "sub": {
            "v_m1_complex": {
                "title": "اعداد مختلط",
                "count": 6,
                "videos": [
                    {"caption": "🎥 ویدیوی شماره ۱ اعداد مختلط ریاضی عمومی ۱", "file_id": "BAACAgQAAxkBAAIChGpy7KEeAyLov8qD60_-MzRVPZoTAAK9HQACByd4U2JqG7R0PWcMPQQ"},
                    {"caption": "🎥 ویدیوی شماره ۲ اعداد مختلط ریاضی عمومی ۱", "file_id": "BAACAgQAAxkBAAIChmpy7KgmuqSWRYDf2_6QJDQ2LuTnAAK-HQACByd4U8w4zFCSyXmYPQQ"},
                    {"caption": "🎥 ویدیوی شماره ۳ اعداد مختلط ریاضی عمومی ۱", "file_id": "BAACAgQAAxkBAAICiGpy7K2UAdvojMYN_qQLGsOIcGigAALAHQACByd4UyDajW41tIRbPQQ"},
                    {"caption": "🎥 ویدیوی شماره ۴ اعداد مختلط ریاضی عمومی ۱", "file_id": "BAACAgQAAxkBAAICimpy7LcerjZVzivP8mJcKbyMEt2TAALBHQACByd4U0Q8QKKgrso7PQQ"},
                    {"caption": "🎥 ویدیوی شماره ۵ اعداد مختلط ریاضی عمومی ۱", "file_id": "BAACAgQAAxkBAAICjGpy7LyoKrNxBAVNTka4NfjF46gyAALDHQACByd4U-3_ojQqMRfaPQQ"},
                    {"caption": "🎥 ویدیوی شماره ۶ اعداد مختلط ریاضی عمومی ۱", "file_id": "BAACAgQAAxkBAAICjmpy7MHBbxz3FXcSzszYCx14KcgxAALEHQACByd4U6zzAAHAu1QwxT0E"},
                ],
            },
            "v_m1_integral": {
                "title": "انتگرال",
                "count": 5,
                "videos": [
                    {"caption": "🎥انتگرال‌گیری با روش تغییر متغیر (بخش اول)", "file_id": "BAACAgQAAxkBAAICkGpy7Mj8WDXokDlQFcJFDLHAxUBKAAKtHQACByd4U05gJGfkQE0iPQQ"},
                    {"caption": "🎥انتگرال‌گیری با روش تغییر متغیر (بخش دوم)", "file_id": "BAACAgQAAxkBAAICkmpy7MwDGZUu37DcHnONlYlTHpxBAAK0HQACByd4U_-icWkNKYIDPQQ"},
                    {"caption": "🎥انتگرال‌گیری به روش تجزیه کسر‌ها", "file_id": "BAACAgQAAxkBAAIClGpy7NQqPLeaKWa6ssOCkVNaJnSnAAK1HQACByd4U34uu30K9WGYPQQ"},
                    {"caption": "🎥 انتگرال‌گیری با روش جز به جز (بخش اول)", "file_id": "BAACAgQAAxkBAAIClmpy7OC-eh2XXAVD-oHHDIK4llM7AALFHQACByd4U_FQU-BZZTq2PQQ"},
                    {"caption": "🎥 انتگرال‌گیری با روش جز به جز (بخش دوم)", "file_id": "BAACAgQAAxkBAAICmGpy7OWDmp3FG8bLHdnqL-FpHIEdAALHHQACByd4Uz8w42oTI9X0PQQ"},
                ],
            },
            "v_m1_app_integral": {
                "title": "کاربرد انتگرال",
                "count": 4,
                "videos": [
                    {"caption": "🎥 ویدیوی شماره ۱ کاربرد انتگرال ریاضی عمومی ۱", "file_id": "BAACAgQAAxkBAAICmmpy7OxX0wUFoPydrHHdOnvokwO9AALUHQACByd4UwSVue87WOR2PQQ"},
                    {"caption": "🎥 ویدیوی شماره ۲ کاربرد انتگرال ریاضی عمومی ۱", "file_id": "BAACAgQAAxkBAAICnGpy7PFUoG1Wj5EVeDX6RDKKHXGHAALVHQACByd4U4bAlLGd0FcNPQQ"},
                    {"caption": "🎥 ویدیوی شماره ۳ کاربرد انتگرال ریاضی عمومی ۱", "file_id": "BAACAgQAAxkBAAICnmpy7PUVxbJfIo_RnZHoUg-iyuxMAALWHQACByd4U14DxELgXOiBPQQ"},
                    {"caption": "🎥 ویدیوی شماره ۴ کاربرد انتگرال ریاضی عمومی ۱", "file_id": "BAACAgQAAxkBAAICoGpy7Poq4Cqf_g1bY6UZKqg8fMz0AALXHQACByd4U3iH_n7kcJ2VPQQ"},
                ],
            },
            "v_m1_optimization": {
                "title": "بهینه سازی",
                "count": 2,
                "videos": [
                    {"caption": "🎥 ویدیوی شماره ۱ بهینه سازی ریاضی عمومی ۱", "file_id": "BAACAgQAAxkBAAICzWpy7_bcdNIZy9RU00E8jbgE-rerAALYHQACByd4U2_ip1eFrg06PQQ"},
                    {"caption": "🎥 ویدیوی شماره ۲ بهینه سازی ریاضی عمومی ۱", "file_id": "BAACAgQAAxkBAAICz2py7_zyNetryVfnyx9Id23ju6aSAALZHQACByd4U6djVE1xnRBVPQQ"},
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
                    {"caption": "🎥 تعیین اکسترمم‌های مطلق- ضرایب لاگرانژ (بخش اول)", "file_id": "BAACAgQAAxkBAAICompy7eO_tH1xfi3YxK5E7OvDfiMnAALeHQACByd4U-S-lh9r6o5WPQQ"},
                    {"caption": "🎥 تعیین اکسترمم‌های مطلق- ضرایب لاگرانژ (بخش دوم)", "file_id": "BAACAgQAAxkBAAICpGpy7eo_azRDYhrthAZ6YjTrS7h8AALsHQACByd4U_6r62PEkvx6PQQ"},
                ],
            },
            "v_m2_double_int": {
                "title": "انتگرال دوگانه",
                "count": 3,
                "videos": [
                    {"caption": "🎥تغییر متغیر در انتگرال دوگانه (بخش اول)", "file_id": "BAACAgQAAxkBAAICpmpy7fnQpG5Qbu3zRAJW4wJP2SqEAALJHQACByd4U_q2zx5zWBQPPQQ"},
                    {"caption": "🎥تغییر متغیر در انتگرال دوگانه (بخش دوم)", "file_id": "BAACAgQAAxkBAAICqGpy7f7b-VacKM-N6a2lkJNycE2RAALMHQACByd4U9mO-Oxwiug2PQQ"},
                    {"caption": "🎥تغییر متغیر در انتگرال دوگانه (بخش سوم)", "file_id": "BAACAgQAAxkBAAICqmpy7gRLSjly2Mxc80VUzdz1UsAEAALNHQACByd4UzbySh9ElD66PQQ"},
                ],
            },
            "v_m2_triple_int": {
                "title": "انتگرال سه‌گانه",
                "count": 4,
                "videos": [
                    {"caption": "🎥قضیه دیورژانس (بخش اول)", "file_id": "BAACAgQAAxkBAAICrGpy7jPcxOEJqGC6cyd4slFfgUq0AAK5HQACByd4U24_Bt18DeVSPQQ"},
                    {"caption": "🎥قضیه دیورژانس (بخش دوم)", "file_id": "BAACAgQAAxkBAAICrmpy7jgY11d2gXR3keZUw9kwV-fyAAK6HQACByd4U6sSdNTOqGDLPQQ"},
                    {"caption": "🎥قضیه دیورژانس (بخش سوم)", "file_id": "BAACAgQAAxkBAAICsGpy7j02w1JT_YoymmZ9S-_4B7kEAAK8HQACByd4UxkEitJRHZLIPQQ"},
                    {"caption": "🎥انتگرال سه‌گانه در مختصات کروی", "file_id": "BAACAgQAAxkBAAICsmpy7kOfMEnuyKSdzxwkGPg1tuRQAALQHQACByd4UzluIliGlLkTPQQ"},
                ],
            },
            "v_m2_summary": {
                "title": "جمع‌بندی",
                "count": 2,
                "videos": [
                    {"caption": "🎥 ویدیوی شماره ۱ جمع‌بندی ریاضی عمومی ۲", "file_id": "BAACAgQAAxkBAAICtGpy7qUwA0pzheV-Jzoz8xvsoLiMAAJSHwAC6jd5U_gEJQVg0_xDPQQ"},
                    {"caption": "🎥 ویدیوی شماره ۲ جمع‌بندی ریاضی عمومی ۲", "file_id": "BAACAgQAAxkBAAICtmpy7qvjnLyGaqrxquOBmi8K5Dl5AAKPHQACByd4U6R50fkgCb5uPQQ"},
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
                    {"caption": "🎥 مشتق ضمنی (بخش اول)", "file_id": "BAACAgQAAxkBAAICuWpy78Xjdf9eOC-oUrqEbCoiDpg-AAKqHQACByd4U1jUajEdsuFxPQQ"},
                    {"caption": "🎥مشتق ضمنی (بخش دوم)", "file_id": "BAACAgQAAxkBAAICu2py78oZpIs8rNN9-pJpBFPpRf4dAAKsHQACByd4U3EPXM055jEnPQQ"},
                ],
            },
            "v_eq_first_order": {
                "title": "معادلات دیفرانسیل مرتبه اول",
                "count": 5,
                "videos": [
                    {"caption": "🎥معادلات کلرو (بخش اول)", "file_id": "BAACAgQAAxkBAAICvWpy78-KwKjPsqTr0pwrmLp8gNhDAAK2HQACByd4U7F8kF4UCsBKPQQ"},
                    {"caption": "🎥 معادلات کلرو (بخش دوم)", "file_id": "BAACAgQAAxkBAAICv2py79S5w30_P21DELbX2Kpip3-UAAK4HQACByd4U84mjvwZyG24PQQ"},
                    {"caption": "🎥 معادلات همگن", "file_id": "BAACAgQAAxkBAAICwWpy79k8SeYSVGFNTl7y2Kd_kCD0AALIHQACByd4U-Ps_HID6SxbPQQ"},
                    {"caption": "🎥معادلات ناهمگن", "file_id": "BAACAgQAAxkBAAICw2py795js1l7C_Pab71UEVNWAAF44QAC0R0AAgcneFNQjGHhk1AMLD0E"},
                    {"caption": "🎥 حل دستگاه معادلات به روش حذفی", "file_id": "BAACAgQAAxkBAAICxWpy7-Oy4j2q-b8uU0EkKr6gPq61AALaHQACByd4U8A_EJ7txEcIPQQ"},
                ],
            },
            "v_eq_methods": {
                "title": "روش‌های حل معادلات دیفرانسیل",
                "count": 3,
                "videos": [
                    {"caption": "🎥تبدیل لاپلاس", "file_id": "BAACAgQAAxkBAAICx2py7-hSlkaXqUDiBuD-y1J3qkuQAALPHQACByd4U-L4rEOvG9hLPQQ"},
                    {"caption": "🎥مشتق و انتگرال لاپلاس (بخش اول)", "file_id": "BAACAgQAAxkBAAICyWpy7-2kNsGaeCZM6Yypojgyb6frAALSHQACByd4UxCe5lmPce12PQQ"},
                    {"caption": "🎥 مشتق و انتگرال لاپلاس (بخش دوم)", "file_id": "BAACAgQAAxkBAAICy2py7_FqBQOt4GK-QzNeP56q5odNAALTHQACByd4U0ol4Bw3JfqgPQQ"},
                ],
            },
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
    btn1 = KeyboardButton("🔗 لینک‌های مفید 🔵")
    btn2 = KeyboardButton("🎙️ نشریات و پادکست 🟣")
    btn3 = KeyboardButton("🎬 ویدیوهای آموزشی 🟠")
    btn4 = KeyboardButton("📚 چارت و تقویم آموزشی 🟡")
    btn5 = KeyboardButton("📄 جزوات دروس ریاضی 🟢")
    btn6 = KeyboardButton("📖 منابع و کتاب‌ها 🟤")
    btn7 = KeyboardButton("📞 ارسال فایل و گزارش 🟥")
    btn8 = KeyboardButton("☎️ کانال‌های ارتباطی 🟦")

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


def get_references_main_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton(
            "📐 دروس تخصصی ریاضی", callback_data="ref_specialized"
        ),
        InlineKeyboardButton("📚 دروس عمومی", callback_data="ref_general"),
        InlineKeyboardButton(
            "🎓 دروس صلاحیت معلمی و تربیتی", callback_data="ref_educational"
        ),
        InlineKeyboardButton(
            "📚 کتب درسی ریاضی متوسطه", callback_data="ref_high_school_math"
        ),
        InlineKeyboardButton(
            "🔙 بازگشت به منوی اصلی", callback_data="back_to_main"
        ),
    )
    return markup


def get_references_specialized_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    for key, val in REFERENCES_SPECIALIZED.items():
        markup.add(InlineKeyboardButton(f"🔹 {val['title']}", callback_data=key))
    markup.add(InlineKeyboardButton("🔙 بازگشت", callback_data="menu_references"))
    return markup


def get_references_general_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    for key, val in REFERENCES_GENERAL.items():
        markup.add(InlineKeyboardButton(f"🔹 {val['title']}", callback_data=key))
    markup.add(InlineKeyboardButton("🔙 بازگشت", callback_data="menu_references"))
    return markup


def get_references_educational_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    for key, val in REFERENCES_EDUCATIONAL.items():
        markup.add(InlineKeyboardButton(f"🔹 {val['title']}", callback_data=key))
    markup.add(InlineKeyboardButton("🔙 بازگشت", callback_data="menu_references"))
    return markup


def get_high_school_math_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton(f"📚 {HIGH_SCHOOL_MATH['middle_school']['title']}", callback_data="hs_middle_school"),
        InlineKeyboardButton(f"📚 {HIGH_SCHOOL_MATH['high_school_fields']['title']}", callback_data="hs_high_school"),
        InlineKeyboardButton("🔙 بازگشت", callback_data="menu_references"),
    )
    return markup


def get_middle_school_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    for key, val in HIGH_SCHOOL_MATH["middle_school"]["sub_items"].items():
        markup.add(InlineKeyboardButton(f"🔹 {val['title']}", callback_data=f"hs_sub_{key}"))
    markup.add(InlineKeyboardButton("🔙 بازگشت", callback_data="ref_high_school_math"))
    return markup


def get_high_school_streams_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    for stream_key, stream_val in HIGH_SCHOOL_MATH["high_school_fields"]["streams"].items():
        markup.add(InlineKeyboardButton(f"🔹 {stream_val['title']}", callback_data=f"hs_stream_{stream_key}"))
    markup.add(InlineKeyboardButton("🔙 بازگشت", callback_data="ref_high_school_math"))
    return markup


def get_high_school_sub_menu(stream_key):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    stream_data = HIGH_SCHOOL_MATH["high_school_fields"]["streams"][stream_key]
    for key, val in stream_data["sub_items"].items():
        markup.add(InlineKeyboardButton(f"🔹 {val['title']}", callback_data=f"hs_sub_{key}"))
    markup.add(InlineKeyboardButton("🔙 بازگشت", callback_data="hs_high_school"))
    return markup


def get_videos_main_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    for key, val in VIDEOS_DATA.items():
        markup.add(InlineKeyboardButton(f"🎬 {val['title']}", callback_data=f"vid_main_{key}"))
    markup.add(
        InlineKeyboardButton("🔙 بازگشت به منوی اصلی", callback_data="back_to_main")
    )
    return markup


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
            "🎓 تحصیلات تکمیلی",
            url="https://www.sru.ac.ir",
        ),
        InlineKeyboardButton(
            "📢 کانال‌های رسمی دانشگاه", callback_data="links_uni_channels"
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
            "سامانه گلستان",
            url="https://portal.sru.ac.ir/forms/authenticateuser/main.htm",
        ),
        InlineKeyboardButton(
            "سامانه ال‌ام‌اس", url="https://lms.sru.ac.ir"
        ),
        InlineKeyboardButton(
            "سامانه نگارستان", url="https://negarestan.sru.ac.ir"
        ),
        InlineKeyboardButton("سماد رجائی", url="https://food.sru.ac.ir/index.rose"),
        InlineKeyboardButton(
            "سامانه کتابخانه", url="https://lib.sru.ac.ir/dl/usersearch/"
        ),
        InlineKeyboardButton(
            "سامانه کارورزی", url="https://karvarzi.sru.ac.ir"
        ),
        InlineKeyboardButton(
            "سامانه رویدادهای پژوهشی دانشگاه",
            url="https://events.sru.ac.ir/users/login.php",
        ),
        InlineKeyboardButton("سامانه تکدا", url="http://takda.sru.ac.ir"),
        InlineKeyboardButton("🔙 بازگشت", callback_data="menu_useful_links"),
    )
    return markup


def get_useful_links_uni_channels_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton(
            "کانال رسمی دانشگاه", url="https://eitaa.com/sruinfo"
        ),
        InlineKeyboardButton(
            "کانال معاونت فرهنگی", url="https://eitaa.com/srufarhang"
        ),
        InlineKeyboardButton(
            "کانال معاونت پژوهش و فناوری", url="https://eitaa.com/SRTTU_Research"
        ),
        InlineKeyboardButton(
            "کانال مرکز آموزش‌های مجازی", url="https://eitaa.com/sru_elearning"
        ),
        InlineKeyboardButton(
            "کانال امور دانشجویی", url="https://eitaa.com/portal_srttu1402"
        ),
        InlineKeyboardButton(
            "کانال دانشکده علوم پایه", url="https://eitaa.com/science401"
        ),
        InlineKeyboardButton(
            "کانال نهاد رهبری", url="https://eitaa.com/nahadrajaee"
        ),
        InlineKeyboardButton("🔙 بازگشت", callback_data="menu_useful_links"),
    )
    return markup


def get_useful_links_student_channels_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton(
            "SRTTU | رسانه دانشجویی", url="https://t.me/srttu_ir"
        ),
        InlineKeyboardButton(
            " انجمن‌های علمی دانشجویی", callback_data="sci_associations_list"
        ),
        InlineKeyboardButton(
            " کانون‌های فرهنگی هنری", callback_data="cultural_cannons_list"
        ),
        InlineKeyboardButton(
            " شورای صنفی دانشجویی", url="https://t.me/srttu_senfi"
        ),
        InlineKeyboardButton(
            " بسیج دانشجویی", url="https://t.me/basijrajaee"
        ),
        InlineKeyboardButton(
            " جامعه اسلامی ", url="https://t.me/JADSRTTU"
        ),
        InlineKeyboardButton(
            " انجمن اسلامی مستقل", url="https://t.me/Mostaghel_Srttu"
        ),
        InlineKeyboardButton(
            "هیئت محبان اهل بیت", url="https://t.me/mohebban_srttu"
        ),
        InlineKeyboardButton("🔙 بازگشت", callback_data="menu_useful_links"),
    )
    return markup


def get_scientific_associations_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    items = [
        "دفتر مرکزی انجمن‌های علمی", "انجمن علمی ریاضی", "انجمن علمی شیمی", "انجمن علمی فیزیک", 
        "انجمن علمی آموزش علوم", "انجمن علمی نجوم", "انجمن علمی زبان", "انجمن علمی رباتیک و هوش مصنوعی", 
        "انجمن علمی کامپیوتر", "انجمن علمی برنامه نویسی", "انجمن علمی صنایع مبلمان", "انجمن علمی برق", 
        "انجمن علمی مواد و متالورژی", "انجمن علمی عمران", "انجمن علمی معماری", "انجمن علمی گرافیک", 
        "انجمن علمی علوم ورزشی", "انجمن علمی تربیت بدنی", "انجمن علمی مکانیک", "شاخه دانشجویی IEEE"
    ]
    for idx, name in enumerate(items):
        markup.add(InlineKeyboardButton(name, callback_data=f"sci_assoc_{idx}"))
    markup.add(InlineKeyboardButton("🔙 بازگشت", callback_data="links_student_channels"))
    return markup


def get_cultural_cannons_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    items = [
        "روابط عمومی کانون‌های فرهنگی هنری", "کانون کتاب و کتابخوانی", "کانون عکاسی", "کانون هنرهای تجسمی", 
        "کانون فن و مهارت", "کانون دبیران جوان", "کانون نقاشی", "کانون گویندگی و فن بیان", 
        "کانون هلال احمر", "کانون مهدویت", "کانون شعر و ادب", "کانون همیاران سلامت", 
        "کانون موسیقی", "کانون کارآفرینی و فناوری", "کانون گردشگری", "کانون تئاتر", 
        "کانون رسانه", "کانون فیلم و عکس"
    ]
    for idx, name in enumerate(items):
        markup.add(InlineKeyboardButton(name, callback_data=f"cult_cannon_{idx}"))
    markup.add(InlineKeyboardButton("🔙 بازگشت", callback_data="links_student_channels"))
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
# 🚀 هندلر دستور /start و /sendall
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


@bot.message_handler(commands=["sendall"])
def broadcast_message(message):
    if message.from_user.id != ADMIN_ID:
        return
    bot.reply_to(message, "📢 قابلیت ارسال پیام همگانی برای کاربران فعال شد.")


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
        warning_text = (
            "❌ برای دسترسی به خدمات ربات، لطفاً ابتدا در کانال انجمن عضو شوید و سپس دکمه بررسی دوباره را بزنید:"
        )
        bot.send_message(
            call.message.chat.id, warning_text, reply_markup=get_join_channel_menu()
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
                call.id, "❌ هنوزه تو کانال نشدی که!", show_alert=True
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

    elif call.data == "sci_associations_list":
        bot.answer_callback_query(call.id)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="📐 **انجمن‌های علمی دانشجویی**\n\nانجمن مورد نظر را انتخاب کنید:",
            parse_mode="Markdown",
            reply_markup=get_scientific_associations_menu(),
        )

    elif call.data == "cultural_cannons_list":
        bot.answer_callback_query(call.id)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="🎭 **کانون‌های فرهنگی هنری**\n\nکانون مورد نظر را انتخاب کنید:",
            parse_mode="Markdown",
            reply_markup=get_cultural_cannons_menu(),
        )

    elif call.data.startswith("sci_assoc_") or call.data.startswith("cult_cannon_"):
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "🔗 لینک مربوطه: [لینک دلخواه شما]")

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
            text="📚 **متوسطه دوم**\n\nرشته تحصیلی رو انتخاب کن:",
            parse_mode="Markdown",
            reply_markup=get_high_school_streams_menu(),
        )

    elif call.data.startswith("hs_stream_"):
        bot.answer_callback_query(call.id)
        stream_key = call.data.replace("hs_stream_", "")
        stream_title = HIGH_SCHOOL_MATH["high_school_fields"]["streams"][stream_key]["title"]
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f"📚 **{stream_title}**\n\nپایه و درس مورد نظر رو انتخاب کن:",
            parse_mode="Markdown",
            reply_markup=get_high_school_sub_menu(stream_key),
        )

    elif call.data.startswith("hs_sub_"):
        bot.answer_callback_query(call.id)
        key = call.data.replace("hs_sub_", "")
        found_item = None
        if key in HIGH_SCHOOL_MATH["middle_school"]["sub_items"]:
            found_item = HIGH_SCHOOL_MATH["middle_school"]["sub_items"][key]
        else:
            for stream_key, stream_data in HIGH_SCHOOL_MATH["high_school_fields"]["streams"].items():
                if key in stream_data["sub_items"]:
                    found_item = stream_data["sub_items"][key]
                    break

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
            f"📖 رفرنس مربوط به **{course['title']}**:",
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
        bot.send_message(
            call.message.chat.id,
            f"📖 منبع عمومی مربوط به **{course['title']}**:",
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
        if course["title"] == "کاربست فناوری در یادگیری":
            bot.send_message(call.message.chat.id, "هنوز فایلی برای این درس بارگذاری نشده است!")
            return

        bot.send_message(
            call.message.chat.id,
            f"📖 منبع تربیتی مربوط به **{course['title']}**:",
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
        "🎬 ویدیوهای آموزشی 🟠",
        "📚 چارت و تقویم آموزشی 🟡",
        "📄 جزوات دروس ریاضی 🟢",
        "📖 منابع و کتاب‌ها 🟤",
        "📞 ارسال فایل و گزارش 🟥",
        "☎️ کانال‌های ارتباطی 🟦",
    ]
)
def handle_reply_keyboard_buttons(message):
    user_id = message.from_user.id
    if not check_subscription(user_id):
        warning_text = (
            "❌ برای دسترسی به خدمات ربات، لطفاً ابتدا در کانال انجمن عضو شوید و سپس دکمه بررسی دوباره را بزنید:"
        )
        bot.send_message(
            message.chat.id,
            warning_text,
            reply_markup=get_join_channel_menu(),
        )
        return

    text = message.text

    if "چارت و تقویم آموزشی" in text:
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

    elif "جزوات دروس ریاضی" in text:
        bot.send_message(
            message.chat.id,
            "📄 **بانک جزوات ریاضی**\n\nکدوم درس رو نیاز داری؟",
            parse_mode="Markdown",
            reply_markup=get_handouts_menu(),
        )

    elif "منابع و کتاب‌ها" in text:
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

    elif "ارسال فایل و گزارش" in text:
        sup_text = (
            "📞 **ارتباط با پشتیبانی و ارسال فایل**\n\nهر گونه پیشنهاد، انتقاد یا"
            " فایلی داری بفرست تا به دست ادمین برسه: 👇"
        )
        sent_msg = bot.send_message(message.chat.id, sup_text, parse_mode="Markdown")
        bot.register_next_step_handler(sent_msg, receive_user_file_or_message)

    elif "کانال‌های ارتباطی" in text:
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
# 📥 مدیریت دریافت فایل/پیام کاربر
# ==========================================
@bot.message_handler(
    content_types=["photo", "document", "video", "audio", "voice", "text"]
)
def handle_all_messages(message):
    if message.from_user.id == ADMIN_ID:
        if message.reply_to_message:
            reply_text = message.reply_to_message.text or message.reply_to_message.caption or ""
            target_user_id = None
            if "شناسه کاربر:" in reply_text:
                try:
                    lines = reply_text.split("\n")
                    for line in lines:
                        if "شناسه کاربر:" in line:
                            target_user_id = int(line.replace("شناسه کاربر:", "").replace("`", "").strip())
                except Exception as e:
                    print(f"Error extracting user ID: {e}")

            if target_user_id:
                try:
                    bot.copy_message(chat_id=target_user_id, from_chat_id=message.chat.id, message_id=message.message_id)
                    bot.reply_to(message, "✅ پاسخ شما با موفقیت به کاربر ارسال شد.")
                    return
                except Exception as e:
                    bot.reply_to(message, f"❌ خطا در ارسال پاسخ به کاربر: {e}")
                    return

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
        menu_buttons = [
            "🔗 لینک‌های مفید 🔵", "🎙️ نشریات و پادکست 🟣", "🎬 ویدیوهای آموزشی 🟠",
            "📚 چارت و تقویم آموزشی 🟡", "📄 جزوات دروس ریاضی 🟢", "📖 منابع و کتاب‌ها 🟤",
            "📞 ارسال فایل و گزارش 🟥", "☎️ کانال‌های ارتباطی 🟦"
        ]
        if message.text in menu_buttons:
            return
        
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
            message, "✅ پیام یا فایل شما با موفقیت به دست ادمین رسید."
        )
    except Exception as e:
        bot.reply_to(message, "❌ خطا در ارسال پیام به ادمین.")


# ==========================================
# ▶️ اجرای ربات
# ==========================================
if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
