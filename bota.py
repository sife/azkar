import asyncio
import logging
import datetime
import random
import pytz
from telegram import Bot, constants

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


# ---------------------- دالة حساب الأيام ----------------------
def get_ramadan_message():
    today = datetime.datetime.now(RIYADH_TZ).date()
    if today < RAMADAN_START:
        days_left = (RAMADAN_START - today).days
        return f"✨🌟 تبقى {days_left} يومًا على دخول شهر رمضان المبارك 🌟✨"
    elif RAMADAN_START <= today < RAMADAN_START + datetime.timedelta(days=RAMADAN_DAYS):
        days_left = RAMADAN_DAYS - (today - RAMADAN_START).days - 1  # ✅ خصم يوم إضافي لحساب صحيح
        if days_left < 0:  # إذا اليوم الأخير
            days_left = 0
        return f"🌟✨ تبقى {days_left} يومًا على نهاية شهر رمضان المبارك ✨🌟"
    else:
        return "✨🌟 نسأل الله أن يتقبل منا ومنكم صالح الأعمال 🌟✨"


# ---------------------- دالة إرسال الأذكار ----------------------
async def send_azkar():
    bot = Bot(token=TOKEN)
    
    while True:  # حلقة مستمرة لضمان استمرار تشغيل البوت
        try:
            azkar = random.choice(AZKAR_LIST)
            ramadan_msg = get_ramadan_message()
            message = f"{azkar}\n\n{ramadan_msg}\n\n🌙 بوت SA Forex أذكار رمضان 🌙"
            
            await bot.send_message(chat_id=CHANNEL_ID, text=message, parse_mode=constants.ParseMode.HTML)
            logging.info(f"تم إرسال الذكر: {message}")

        except Exception as e:
            logging.error(f"❌ خطأ أثناء إرسال الرسالة: {e}")

        await asyncio.sleep(14200)  # الانتظار (حوالي 4 ساعات) بين كل إرسال


# ---------------------- تشغيل الكود ----------------------
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    loop = asyncio.get_event_loop()
    loop.create_task(send_azkar())  # تشغيل المهمة في الخلفية
    loop.run_forever()  # تشغيل مستمر للسكريبت
