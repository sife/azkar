import asyncio
import logging
import datetime
import telegram
import random
import pytz
from telegram import Bot

# إعداد التوكن والمعرف
TOKEN = "7876105293:AAG6wsc8X7ifkNaPyrdCFNH5tW8Kln1fHyU"
CHANNEL_ID = "@jordangold"
RAMADAN_START = datetime.date(2025, 3, 1)
RAMADAN_DAYS = 30

# تعيين التوقيت المحلي للرياض
RIYADH_TZ = pytz.timezone("Asia/Riyadh")

# قائمة الأذكار والأدعية
AZKAR_LIST = [
    "✨ 🙏 سبحان الله وبحمده، سبحان الله العظيم 🙏 ✨",
    "💛 لا إله إلا الله وحده لا شريك له، له الملك وله الحمد وهو على كل شيء قدير 💛",
    "🌟 أستغفر الله العظيم وأتوب إليه 🌟",
    "💖 اللهم صل وسلم على نبينا محمد 💖",
    "🌟 لا حول ولا قوة إلا بالله العلي العظيم 🌟",
    "🌟 اللهم إنك عفو تحب العفو فاعف عنا 🌟",
    "🙏 رَبَّنَا آتِنَا فِي الدُّنْيَا حَسَنَةً وَفِي الآخِرَةِ حَسَنَةً وَقِنَا عَذَابَ النَّارِ 🙏",
    "🌟 لا إله إلا الله وحده لا شريك له ، له الملك ، وله الحمد ، وهو على كل شيء قدير 🌟",
    "💖 لا إله إلا الله العظيم الحليم ، لا إله إلا الله ربّ العرش العظيم ، لا إله إلا الله ربّ السَّماوات ، وربّ الأرض ، وربّ العرش الكريم .. 💖",
    "✨ سُبْحَان الله عدد مافي السماوات والأرض. ✨",
    "🙏 ياحي ياقيوم برحمتك ٲستغيث ٲصلح لي شأني كله ولا تكلني ٳلى نفسي طرفة عين 🙏",
    "🌟 حسبي الله لا إله إلا هو عليه توكلت وهو رب العرش العظيم 🌟",
    "🌙 اللهم اغفر لي خطيئتي وجهلي وإسرافي في أمري وما أنت أعلم به مني، اللهم اغفر لي هزلي وجدي وخطئي وعمدي وكل ذلك عندي 🌙",
    "✨ اللهم اجعل صيامي فيه صيام الصائمين، وقيامي فيه قيام القائمين، ونبّهني فيه عن نومة الغافلين، وهب لي جرمي فيه يا إله العالمين، واعفُ عني يا عافياً عن المجرمين. ✨",
    "💖 اللهم اجعلني في هذا الشهر من المقبولين، ولا تجعلني فيه من المحرومين، واغفر لي ذنوبي يا أكرم الأكرمين. 💖",
    "🙏 اللهم اجعل لنا في هذا الشهر الكريم نصيبًا من الرحمة والمغفرة والعتق من النار 🙏"
]

def get_ramadan_message():
    today = datetime.datetime.now(RIYADH_TZ).date()
    if today < RAMADAN_START:
        days_left = (RAMADAN_START - today).days
        return f"✨🌟 تبقى {days_left} يومًا على دخول شهر رمضان المبارك 🌟✨"
    elif RAMADAN_START <= today < RAMADAN_START + datetime.timedelta(days=RAMADAN_DAYS):
        days_left = RAMADAN_DAYS - (today - RAMADAN_START).days
        return f"🌟✨ تبقى {days_left} يومًا على نهاية شهر رمضان المبارك ✨🌟"
    else:
        return "✨🌟 نسأل الله أن يتقبل منا ومنكم صالح الأعمال 🌟✨"

async def send_azkar():
    bot = Bot(token=TOKEN)
    
    while True:
        now = datetime.datetime.now(RIYADH_TZ)
        target_time = now.replace(hour=0, minute=0, second=0, microsecond=0) + datetime.timedelta(days=1)  # منتصف الليل الرياض
        seconds_until_midnight = (target_time - now).total_seconds()
        
        logging.info(f"النوم حتى بداية اليوم الجديد: {seconds_until_midnight} ثانية")
        await asyncio.sleep(seconds_until_midnight)  # الانتظار حتى بداية اليوم

        for _ in range(8):  # إرسال 8 أذكار يوميًا
            azkar = random.choice(AZKAR_LIST)
            ramadan_msg = get_ramadan_message()
            message = f"{azkar}\n\n{ramadan_msg}\n\n🌙 بوت SA Forex أذكار رمضان 🌙"
            
            try:
                await bot.send_message(chat_id=CHANNEL_ID, text=message, parse_mode=telegram.constants.ParseMode.HTML)
                logging.info(f"تم إرسال الذكر: {message}")
            except Exception as e:
                logging.error(f"خطأ أثناء إرسال الرسالة: {e}")

            await asyncio.sleep(3 * 60 * 60)  # الانتظار 3 ساعات بين كل إرسال

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(send_azkar())
