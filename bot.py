import asyncio
import logging
import datetime
import telegram
import random
from telegram import Bot

# إعداد التوكن والمعرف
TOKEN = "7876105293:AAG6wsc8X7ifkNaPyrdCFNH5tW8Kln1fHyU"
CHANNEL_ID = "@testbotseaf"
RAMADAN_START = datetime.date(2025, 3, 1)
RAMADAN_DAYS = 30

# قائمة الأذكار
AZKAR_LIST = [
    "\u2728 \ud83d\ude4f سبحان الله وبحمده، سبحان الله العظيم \ud83d\ude4f \u2728",
    "\ud83d\udc9b لا إله إلا الله وحده لا شريك له، له الملك وله الحمد وهو على كل شيء قدير \ud83d\udc9b",
    "\ud83c\udf1f أستغفر الله العظيم وأتوب إليه \ud83c\udf1f",
    "\ud83d\udc96 اللهم صل وسلم على نبينا محمد \ud83d\udc96",
    "\ud83c\udf1f لا حول ولا قوة إلا بالله العلي العظيم \ud83c\udf1f",
    "\ud83c\udf1f اللهم انك عفو تحب العفو فاعف عنا \ud83c\udf1f",
    "\ud83d\ude4f رَبَّنَا آتِنَا فِي الدُّنْيَا حَسَنَةً وَفِي الآخِرَةِ حَسَنَةً وَقِنَا عَذَابَ النَّارِ \ud83d\ude4f",
    "\ud83c\udf1f لا إله إلا الله وحده لا شريك له ، له الملك ، وله الحمد ، وهو على كل شيء قدير \ud83c\udf1f",
    "\ud83d\udc96 لا إله إلا الله العظيم الحليم ، لا إله إلا الله ربّ العرش العظيم ، لا إله إلا الله ربّ السَّماوات ، وربّ الأرض ، وربّ العرش الكريم .. \ud83d\udc96",
    "\u2728 سُبْحَان الله عدد مافي السماوات والأرض. \u2728",
    "\ud83d\ude4f ياحي ياقيوم برحمتك ٲستغيث ٲصلح لي شأني كله و لا تكلني ٳلى نفسي طرفة عين \ud83d\ude4f",
    "\ud83c\udf1f حسبي الله لا إله إلا هو عليه توكلت وهو رب العرش العظيم \ud83c\udf1f"
]

def get_ramadan_message():
    today = datetime.date.today()
    if today < RAMADAN_START:
        days_left = (RAMADAN_START - today).days
        return f"\u2728\ud83c\udf1f تبقى {days_left} يومًا على دخول شهر رمضان المبارك \ud83c\udf1f\u2728"
    elif RAMADAN_START <= today < RAMADAN_START + datetime.timedelta(days=RAMADAN_DAYS):
        days_left = RAMADAN_DAYS - (today - RAMADAN_START).days
        return f"\ud83c\udf1f\u2728 تبقى {days_left} يومًا على نهاية شهر رمضان المبارك \u2728\ud83c\udf1f"
    else:
        return "\u2728\ud83c\udf1f نسأل الله أن يتقبل منا ومنكم صالح الأعمال \ud83c\udf1f\u2728"

async def send_azkar():
    bot = Bot(token=TOKEN)
    while True:
        azkar = random.choice(AZKAR_LIST)
        ramadan_msg = get_ramadan_message()
        message = f"{azkar}\n\n{ramadan_msg}"
        try:
            await bot.send_message(chat_id=CHANNEL_ID, text=message, parse_mode=telegram.constants.ParseMode.HTML)
        except Exception as e:
            logging.error(f"Error sending message: {e}")
        await asyncio.sleep(3600)  # الانتظار لمدة ساعة

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(send_azkar())
