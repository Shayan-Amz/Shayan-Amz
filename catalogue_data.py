# -*- coding: utf-8 -*-
"""
Data for the two extra sheets of Table_final.xlsx:
  «برنامه‌ها»           — one row per English-taught master's programme (all 6 countries incl. Switzerland, 8 fields)
  «حوزه‌ها و بازار کار» — the 8 computing fields, their 2026 job market and fit with Shayan's profile
Figures checked on 2026-09-27 against the programme/fee pages listed in the source column.
"""

# ---- FX (same as main table) ------------------------------------------------
RATES = {"EUR": 1.14, "GBP": 1.325, "SEK": 1 / 9.9, "DKK": 1 / 6.55, "CHF": 1.21}

# ---- fields -----------------------------------------------------------------
# key: (label, market score 1-5, one-line market note used in the programme sheet)
FIELDS = {
    "AI":    ("هوش مصنوعی / یادگیری ماشین", 5,
              "داغ‌ترین بازار؛ «AI Engineer» سریع‌ترین‌رشد (LinkedIn 2026)؛ ولی برنامه‌های ریاضی‌محور (Tübingen، UvA، KTH) بسیار رقابتی‌اند"),
    "SE":    ("مهندسی نرم‌افزار / علوم کامپیوتر", 4,
              "بیشترین حجم آگهی در هر ۶ کشور؛ ورود جونیور از ۲۰۲۳ سخت‌تر شده — سابقهٔ کار شما مزیت است"),
    "CY":    ("امنیت سایبری", 4,
              "کمبود ساختاری (Bitkom: جزو ۳ کمبود اصلی آلمان)؛ اما ۳۱٪ تیم‌ها هیچ نیروی جونیور ندارند → کارآموزی/گواهی لازم است"),
    "CLOUD": ("ابری / سیستم‌های توزیع‌شده / DevOps", 4,
              "تقاضای پایدار و کمتر مدرک‌محور؛ گواهی AWS/Azure کنار مدرک وزن زیادی دارد"),
    "DS":    ("علم داده / تحلیل داده", 3,
              "بازار ارشد/سینیور خوب، ولی سطح جونیور اشباع (ده‌ها هزار فارغ‌التحصیل مشابه)؛ Data Engineer کم‌رقابت‌تر از Data Scientist"),
    "EMB":   ("سیستم‌های نهفته / رباتیک / خودران", 4,
              "در آلمان و سوئد قوی (خودرو، Bosch، ABB، Ericsson)؛ ولی کارفرمایان صنعتی خارج از شهرهای بزرگ اغلب آلمانی/سوئدی می‌خواهند"),
    "HCI":   ("HCI / طراحی تعامل / UX", 2,
              "آگهی‌های UX/UXR از ۲۰۲۲ حدود ۷۰٪ کم شده و از ۲۰۲۳ ثابت مانده؛ رقابت شدید، حقوق شروع کمتر از توسعه‌دهنده"),
    "GD":    ("توسعه بازی", 2,
              "≈۴۵ هزار اخراج ۲۰۲۲–۲۰۲۵؛ ۲۶٪ توسعه‌دهندگان اروپایی حداقل یک‌بار اخراج شده‌اند؛ حقوق برنامه‌نویس Unity تا ۵۰٪ افت — سابقهٔ Unity شما مزیت ورود است، نه تضمین"),
    "MULTI": ("چندحوزه‌ای (انتخاب گرایش)", 4,
              "گرایش را بعد از ورود انتخاب می‌کنید؛ امتیاز بازار = گرایشی که برمی‌دارید"),
}

# ---- the field/market sheet ---------------------------------------------------
# label, market 1-5, junior pay vs. general CS, English-only friendliness, fit with Shayan, risks, sources
FIELD_ROWS = [
    ["هوش مصنوعی / یادگیری ماشین", "۵ — قوی‌ترین رشد",
     "بالاتر (+۱۰ تا +۲۵٪؛ در آلمان €52–60k، انگلستان £35–45k خارج لندن)",
     "بسیار خوب — تیم‌های AI/ML در همهٔ ۶ کشور انگلیسی‌زبان‌اند",
     "خوب: پیش‌زمینهٔ Computer Engineering + Python؛ ولی برای برنامه‌های Reach (Tübingen، UvA، KTH، Sheffield) معدل ۱۵.۷۷ کافی نیست — برنامه‌های کاربردی (Passau AI Eng، FAU، Northumbria/Teesside AI، USI AI (Lugano)، Umeå) هدف بگیرید",
     "رقابت ورودی شدید؛ بخشی از آگهی‌ها «AI» در عنوان دارند ولی کار مهندسی نرم‌افزار معمولی است؛ مدرک به‌تنهایی بدون پورتفولیو/پروژه کافی نیست",
     "LinkedIn/WEF ژانویه ۲۰۲۶ (۱.۳ میلیون شغل جدید AI؛ AI Engineer سریع‌ترین‌رشد)؛ Bitkom 2025"],
    ["مهندسی نرم‌افزار / علوم کامپیوتر", "۴ — بیشترین حجم",
     "مرجع (آلمان €48–55k · هلند €40–50k · سوئد SEK 420–540k · دانمارک DKK 500–540k · سوئیس CHF 85–105k (بالاترین) · انگلستان £28–35k)",
     "بسیار خوب",
     "بهترین تناسب با سابقهٔ شما (۲ سال IT + Unity/C#)؛ پذیرش ساده‌تر (2:2)؛ در همهٔ کشورها گزینهٔ Safe دارد",
     "آگهی‌های جونیور از ۲۰۲۳ کم شده (اثر GenAI)؛ در بریتانیا ۶–۷٪ بیکاری فارغ‌التحصیلان CS — سابقهٔ کار واقعی شما را از این گروه جدا می‌کند",
     "Bitkom 2025 (۱۰۹ هزار جای خالی IT در آلمان، ۷.۷ ماه زمان پرکردن)؛ IW 2024 (آگهی‌ها ۲۶٪ کمتر از ۲۰۲۳)"],
    ["امنیت سایبری", "۴ — کمبود ساختاری",
     "مساوی تا کمی بالاتر؛ در انگلستان (NCSC-certified) و سوئیس (بانک‌ها، بیمه‌ها، ETH/EPFL Cyber؛ حقوق بالا) خوب",
     "خوب — ولی مشاغل دولتی/دفاعی معمولاً به تابعیت یا اقامت بلندمدت نیاز دارند",
     "خوب: MSc Cyber با 2:2 در Teesside/Northumbria/MMU/Kent/Royal Holloway؛ Saarland (رایگان ولی IELTS 7)؛ AAU کپنهاگ؛ ZHAW MSE Information & Cyber Security (سوئیس، نیاز به معدل A/B)",
     "عدد «۴.۸ میلیون کمبود» ISC2 در گزارش ۲۰۲۵ حذف شد (نیاز اعلام‌شده بود نه آگهی واقعی)؛ کمبود بودجه دلیل اول جای خالی؛ ۳۱٪ تیم‌ها صفر جونیور دارند → برای اولین شغل، کارآموزی + گواهی (Security+، AZ-500) لازم است",
     "ISC2 Workforce Study 2024/2025؛ Kent/Surrey NCSC certification"],
    ["ابری / سیستم‌های توزیع‌شده / DevOps", "۴ — پایدار",
     "بالاتر از توسعه‌دهندهٔ عمومی (+۵ تا +۱۵٪)؛ DevOps/SRE در دانمارک و سوئد پرتقاضا",
     "بسیار خوب",
     "خوب: Leicester Cloud Computing، TU Darmstadt DSS، KTH SEDS، USI Software & Data Engineering؛ گواهی AWS/Azure کنار مدرک",
     "کمتر «مدرک‌محور» است؛ برنامه‌های خالص Cloud کم‌اند — معمولاً گرایشِ CS/SE است",
     "tribexyz 2026 (Data/Cloud Engineer پرجست‌وجوترین در UK/DE)؛ آگهی‌های شرکت‌ها"],
    ["علم داده / تحلیل داده", "۳ — جونیور اشباع",
     "مساوی CS در سطح جونیور؛ بالاتر بعد از ۲–۳ سال",
     "بسیار خوب",
     "متوسط: مدرک‌های ارزان و Safe زیاد است (HSLU Lucerne ≈ CHF 3,150/سال، Skövde، Brunel، ITU €16.5k) ولی رقابت جونیور بالاست؛ اگر می‌روید، Data Engineering را انتخاب کنید",
     "تعداد فارغ‌التحصیل خیلی بیشتر از جای خالی جونیور؛ آگهی جونیور Data Engineering هم ↓۶۷٪؛ مسیر رایج: تحلیلگر/بک‌اند → مهندس داده",
     "research.com 2026؛ careery.pro 2026؛ datadriven.io 2026"],
    ["سیستم‌های نهفته / رباتیک / خودران", "۴ در آلمان/سوئد؛ ۳ در بقیه",
     "مساوی تا کمی بالاتر در صنعت (Bosch، Continental، ABB، Volvo)؛ پایین‌تر در بریتانیا؛ در سوئیس (ABB، رباتیک ETH) بالا ولی آلمانی‌محور",
     "متوسط ⚠️ — تیم‌های R&D انگلیسی‌اند ولی شرکت‌های صنعتی متوسط آلمان/سوئد در عمل زبان محلی می‌خواهند",
     "خوب از نظر پیش‌زمینه (Computer Engineering)؛ گزینه‌ها: Twente ES، Stuttgart INFOTECH، H-BRS Autonomous Systems، FAU Autonomy Tech، Halmstad، MDU، SDU Robot Systems، DTU Autonomous Systems",
     "با معیار «فقط انگلیسی» شما ضعیف‌تر از AI/SE/Cyber؛ وابسته به صنعت خودرو که در ۲۰۲۴–۲۵ آگهی‌هایش کم شد",
     "Bitkom/IW 2024–25؛ Twente/H-BRS/FAU program pages"],
    ["HCI / طراحی تعامل / UX", "۲ — رو به کاهش",
     "پایین‌تر از توسعه‌دهنده (−۱۰ تا −۲۵٪)",
     "خوب",
     "ضعیف برای هدف «حقوق شروع بالا»؛ فقط اگر واقعاً به طراحی علاقه دارید (Siegen رایگان، Twente I-Tech، York HCIT، Chalmers IxD، AAU Medialogy)",
     "آگهی UX ↓۷۱٪ و UXR ↓۷۳٪ نسبت به ۲۰۲۲ و از ۲۰۲۳ ثابت؛ متقاضی به ازای هر آگهی دو برابر شده",
     "Indeed Hiring Lab تا Q4 2025 (thevoiceofuser, 2026)؛ uxdesigninstitute 2024؛ academyux Q1 2025"],
    ["توسعه بازی", "۲ — کوچک و پرنوسان",
     "پایین‌تر از نرم‌افزار عمومی (−۲۰ تا −۴۰٪)؛ استودیوهای بزرگ استثنا",
     "خوب (استودیوهای بزرگ انگلیسی‌زبان: لندن، Guildford، Stockholm، Malmö، Copenhagen، Cologne)",
     "تنها حوزه‌ای که سابقهٔ Unity/C# شما در آن مستقیماً مزیت است؛ اما بازار ۲۰۲۲–۲۵ بدترین دورهٔ خود را داشت — پیشنهاد: ارشد Software/AI بگیرید و بازی را به‌عنوان تخصص/پورتفولیو نگه دارید، مگر Goldsmiths (£22k) یا Cologne Game Lab را با چشم باز انتخاب کنید",
     "≈۴۵ هزار اخراج ۲۰۲۲–ژوئیهٔ ۲۰۲۵؛ بیش از ۳۰ استودیو کاملاً بسته شد؛ حقوق برنامه‌نویس Unity ≈۵۰٪ افت؛ Unity Technologies شش دور اخراج",
     "Wikipedia «2022–2026 video game industry layoffs» (GDC State of the Industry 2026؛ 80.lv)"],
]


# ---- cities ------------------------------------------------------------------
# key: (display name "English (فارسی)", approximate student cost-of-living tier incl. rent, per month)
CITIES = {
    # انگلستان
    "Middlesbrough": ("Middlesbrough (میدلزبرو) — شمال شرق انگلستان", "ارزان — £950–1,150"),
    "Newcastle": ("Newcastle upon Tyne (نیوکاسل) — شمال شرق", "ارزان تا متوسط — £950–1,250"),
    "Nottingham": ("Nottingham (ناتینگهام) — میدلندز", "متوسط — £1,000–1,300"),
    "Manchester": ("Manchester (منچستر) — دومین قطب فناوری انگلستان", "متوسط — £1,050–1,350"),
    "Colchester": ("Colchester (کولچستر) — Essex، ۵۰ دقیقه تا لندن", "متوسط — £1,000–1,350"),
    "Leicester": ("Leicester (لستر) — میدلندز", "متوسط — £1,000–1,300"),
    "London-Uxbridge": ("London – Uxbridge (لندن، غرب؛ کمپوس Brunel)", "خیلی گران — £1,400–1,800"),
    "Egham": ("Egham، Surrey (اگام؛ ۴۰ دقیقه تا لندن)", "گران — £1,300–1,600"),
    "London-NewCross": ("London – New Cross (لندن، جنوب شرق؛ Goldsmiths)", "خیلی گران — £1,400–1,800"),
    "Canterbury": ("Canterbury (کنتربری) — Kent", "متوسط — £1,000–1,350"),
    "Guildford": ("Guildford (گیلفورد) — Surrey، ۳۵ دقیقه تا لندن؛ قطب بازی‌سازی", "گران — £1,300–1,600"),
    "York": ("York (یورک) — شمال انگلستان", "متوسط — £1,000–1,350"),
    "Lancaster": ("Lancaster (لنکستر) — شمال غرب", "ارزان تا متوسط — £950–1,250"),
    "Sheffield": ("Sheffield (شفیلد) — یورکشایر", "ارزان تا متوسط — £950–1,250"),
    "London-Central": ("London – مرکز (South Kensington / Bloomsbury / Strand؛ Imperial، UCL، KCL)", "خیلی گران — £1,600–1,900 (برآورد خود Imperial: £16.4–17k برای ۹ ماه)"),
    "Coventry": ("Coventry (کاونتری) — کمپوس Warwick؛ میدلندز", "متوسط — £1,000–1,250"),
    "Bristol": ("Bristol (بریستول) — جنوب غرب؛ قطب فناوری/هوافضا", "گران — £1,200–1,450"),
    "Durham": ("Durham (دورهام) — شمال شرق؛ ۱۵ دقیقه تا نیوکاسل", "ارزان تا متوسط — £950–1,200"),
    # سوئیس
    "Zuerich": ("Zürich (زوریخ) — Google، UBS، ETH؛ گران‌ترین شهر دانشگاهی اروپا", "خیلی گران — CHF 1,900–2,500"),
    "Zuerich-Winterthur": ("Zürich / Winterthur (زوریخ / وینترتور؛ کمپوس‌های ZHAW)", "خیلی گران — CHF 1,800–2,400"),
    "Lausanne": ("Lausanne (لوزان) — کنار دریاچهٔ ژنو؛ فرانسه‌زبان؛ EPFL", "خیلی گران — CHF 1,700–2,200"),
    "Bern": ("Bern (برن) — پایتخت؛ آلمانی‌زبان", "گران — CHF 1,600–2,000"),
    "Basel": ("Basel (بازل) — Roche، Novartis؛ مرز آلمان/فرانسه", "گران — CHF 1,600–2,100"),
    "Fribourg": ("Fribourg (فریبورگ) — دوزبانه (آلمانی/فرانسه)", "گران — CHF 1,450–1,800"),
    "Neuchatel": ("Neuchâtel (نوشاتل) — فرانسه‌زبان؛ کنار دریاچه؛ ۳۵ دقیقه تا برن", "متوسط تا گران — CHF 1,350–1,750"),
    "Lugano": ("Lugano (لوگانو) — تیچینو، ایتالیایی‌زبان؛ IDSIA؛ ارزان‌ترین شهر دانشگاهی سوئیس", "گران — CHF 1,400–1,800"),
    "Luzern": ("Lucerne / Luzern (لوسرن) — مرکز سوئیس، ۴۵ دقیقه تا زوریخ", "گران — CHF 1,550–1,950"),
    # آلمان
    "Stuttgart": ("Stuttgart (اشتوتگارت) — Bosch، Mercedes، Porsche", "گران — €1,100–1,350"),
    "Erlangen": ("Erlangen / Nürnberg (ارلانگن / نورنبرگ) — Siemens", "متوسط — €950–1,150"),
    "Darmstadt": ("Darmstadt (دارمشتات) — ۲۵ دقیقه تا فرانکفورت", "گران — €1,050–1,300"),
    "Dresden": ("Dresden (درسدن) — «سیلیکون ساکسونی»", "ارزان — €850–1,050"),
    "Saarbruecken": ("Saarbrücken (زاربروکن) — مرز فرانسه؛ CISPA/DFKI", "متوسط — €900–1,100"),
    "Chemnitz": ("Chemnitz (کمنیتس) — ساکسونی", "ارزان — €800–1,000"),
    "Passau": ("Passau (پاساو) — شهر کوچک، مرز اتریش", "متوسط — €900–1,100"),
    "Magdeburg": ("Magdeburg (ماگدبورگ) — ساکسونی-آنهالت", "ارزان — €850–1,000"),
    "Koeln": ("Köln / Cologne (کلن) — چهارمین شهر آلمان", "گران — €1,050–1,300"),
    "Siegen": ("Siegen (زیگن) — شهر کوچک، NRW", "متوسط — €900–1,100"),
    "SanktAugustin": ("Sankt Augustin (زانکت آگوستین) — حومهٔ Bonn", "متوسط — €950–1,200"),
    "Aachen": ("Aachen (آخن) — مرز هلند/بلژیک", "متوسط — €950–1,200"),
    "Tuebingen": ("Tübingen (توبینگن) — شهر دانشگاهی کوچک؛ Cyber Valley", "گران — €1,050–1,300"),
    "Muenchen": ("München – Garching (مونیخ، کمپوس گارشینگ)", "خیلی گران — €1,300–1,600"),
    # هلند
    "Enschede": ("Enschede (انسخده) — شرق هلند، مرز آلمان", "متوسط — €1,000–1,300"),
    "Nijmegen": ("Nijmegen (نایمخن) — شرق هلند", "متوسط — €1,050–1,350"),
    "Leiden": ("Leiden (لایدن) — بین Den Haag و Amsterdam", "گران — €1,200–1,500"),
    "Groningen": ("Groningen (خرونینگن) — شمال هلند", "متوسط — €1,050–1,350"),
    "Utrecht": ("Utrecht (اوترخت) — مرکز هلند؛ قطب استودیوهای بازی", "گران — €1,200–1,500"),
    "Amsterdam": ("Amsterdam (آمستردام)", "خیلی گران — €1,300–1,700"),
    "Eindhoven": ("Eindhoven (آیندهوون) — Brainport: ASML، Philips، NXP", "گران — €1,100–1,400"),
    "Delft": ("Delft (دلفت) — کنار Den Haag/Rotterdam", "گران — €1,200–1,500"),
    "Breda": ("Breda (بردا) — جنوب هلند", "متوسط — €1,000–1,300"),
    # سوئد
    "Linkoping": ("Linköping (لینشوپینگ) — Saab، Ericsson", "متوسط — SEK 10,500–12,500"),
    "Halmstad": ("Halmstad (هالمستاد) — غرب سوئد", "متوسط — SEK 10,000–12,000"),
    "Karlskrona": ("Karlskrona (کارلسکرونا) — Ericsson، Telenor", "ارزان — SEK 9,500–11,500"),
    "Stockholm": ("Stockholm (استکهلم)", "گران — SEK 12,500–15,000"),
    "Stockholm-Kista": ("Stockholm – Kista (استکهلم، شیستا؛ قطب ICT)", "گران — SEK 12,500–15,000"),
    "Gothenburg": ("Gothenburg / Göteborg (گوتنبرگ) — Volvo، Ericsson", "متوسط تا گران — SEK 11,500–13,500"),
    "Uppsala": ("Uppsala (اوپسالا) — ۴۰ دقیقه تا استکهلم", "متوسط تا گران — SEK 11,000–13,000"),
    "Umea": ("Umeå (اومئو) — شمال سوئد", "ارزان تا متوسط — SEK 10,000–12,000"),
    "Skovde": ("Skövde (شوده) — Sweden Game Arena", "ارزان — SEK 9,500–11,500"),
    "Vasteras": ("Västerås (وسترئوس) — ABB، Westinghouse؛ ۱ ساعت تا استکهلم", "متوسط — SEK 10,000–12,000"),
    # دانمارک
    "Aalborg": ("Aalborg (آلبورگ) — شمال یوتلند", "متوسط — DKK 8,000–9,500"),
    "Copenhagen-AAU": ("Copenhagen – Sydhavn (کپنهاگ؛ کمپوس AAU)", "خیلی گران — DKK 10,000–12,500"),
    "Aalborg-or-Copenhagen": ("Aalborg یا Copenhagen (هر دو کمپوس)", "متوسط (Aalborg) تا خیلی گران (Copenhagen)"),
    "Odense": ("Odense (اودنسه) — سومین شهر؛ خوشهٔ رباتیک", "متوسط — DKK 8,000–10,000"),
    "Kolding": ("Kolding (کولدینگ) — جنوب یوتلند", "ارزان تا متوسط — DKK 7,500–9,000"),
    "Copenhagen": ("Copenhagen (کپنهاگ)", "خیلی گران — DKK 10,000–12,500"),
    "Lyngby": ("Kgs. Lyngby (لینگبی) — ۱۵ کیلومتری کپنهاگ", "خیلی گران — DKK 9,500–12,000"),
    "Aarhus": ("Aarhus (آرهوس) — دومین شهر دانمارک", "گران — DKK 9,000–11,000"),
}

# ---- programmes ---------------------------------------------------------------
# country, university, city key (see CITIES), programme, field key, duration, fee text (local), (cur, annual amount low, high or None),
# entry requirement, IELTS, QS 2027, tier for GPA 15.77/20, note, source URL
P = []

def add(*a):
    P.append(a)

# ===== انگلستان (GBP) =====
add("انگلستان", "Teesside University", "Middlesbrough", "MSc Computer Science", "SE", "۱ سال", "£17,000", ("GBP", 17000, None),
    "2:2 در رشتهٔ مرتبط", "6.0", "— (THE 601–800)", "Safe", "ارزان‌ترین گزینهٔ معتبر انگلستان؛ Middlesbrough ارزان ولی بازار کار محلی کوچک",
    "https://www.tees.ac.uk/postgraduate_courses/computing_&_cyber_security/msc_computer_science.cfm")
add("انگلستان", "Teesside University", "Middlesbrough", "MSc Artificial Intelligence", "AI", "۱ سال", "£17,000", ("GBP", 17000, None),
    "2:2 در رشتهٔ مرتبط", "6.0", "—", "Safe", "همان باند شهریهٔ Teesside",
    "https://www.tees.ac.uk/postgraduate_courses/computing_&_cyber_security/msc_artificial_intelligence.cfm")
add("انگلستان", "Teesside University", "Middlesbrough", "MSc Cyber Security (BCS accredited)", "CY", "۱ سال", "£17,000", ("GBP", 17000, None),
    "2:2 در رشتهٔ مرتبط", "6.0", "—", "Safe", "اعتبار BCS؛ بدون NCSC",
    "https://www.tees.ac.uk/postgraduate_courses/computing_&_cyber_security/msc_cyber_security.cfm")
add("انگلستان", "Northumbria University", "Newcastle", "MSc Advanced Computer Science", "SE", "۱ سال", "£21,500", ("GBP", 21500, None),
    "2:2 در رشتهٔ کامپیوتری", "6.5", "=528", "Safe", "Newcastle: شهر دانشجویی ارزان با بازار فناوری متوسط",
    "https://www.northumbria.ac.uk/study-at-northumbria/courses/msc-advanced-computer-science-dtfava6/")
add("انگلستان", "Northumbria University", "Newcastle", "MSc Artificial Intelligence", "AI", "۱ سال", "£21,500", ("GBP", 21500, None),
    "2:2 در رشتهٔ کامپیوتری/ریاضی", "6.5", "=528", "Safe", "شهریهٔ رسمی 2026/27",
    "https://www.northumbria.ac.uk/study-at-northumbria/courses/msc-artificial-intelligence-dtfari6/")
add("انگلستان", "Nottingham Trent University (NTU)", "Nottingham", "MSc Artificial Intelligence", "AI", "۱ سال", "≈ £19,900", ("GBP", 19900, None),
    "2:2 (≈ ۵۵٪)", "6.5", "=639", "Safe", "رقم از دو مرجع ثانویه؛ صفحهٔ رسمی 2026/27 را قبل از اقدام چک کنید",
    "https://www.ntu.ac.uk/study-and-courses/courses")
add("انگلستان", "Nottingham Trent University (NTU)", "Nottingham", "MSc Cyber Security", "CY", "۱ سال", "≈ £19,900", ("GBP", 19900, None),
    "2:2", "6.5", "=639", "Safe", "همان باند NTU (≈)",
    "https://www.ntu.ac.uk/study-and-courses/courses")
add("انگلستان", "Manchester Metropolitan University (MMU)", "Manchester", "MSc Cyber Security", "CY", "۱ سال", "£21,000", ("GBP", 21000, None),
    "2:2 در رشتهٔ کامپیوتری", "6.5", "≈ 600–650", "Safe", "Manchester دومین قطب فناوری انگلستان؛ شهریهٔ رسمی overseas 2026/27",
    "https://www.mmu.ac.uk/study/postgraduate/course/msc-cyber-security")
add("انگلستان", "University of Essex", "Colchester", "MSc Advanced Computer Science", "SE", "۱ سال", "£24,675", ("GBP", 24675, None),
    "2:2؛ Computer Engineering پذیرفته می‌شود", "6.0", "=438", "Safe/Target", "۵۰ دقیقه تا لندن؛ دانشکدهٔ CSEE قوی در AI",
    "https://www.essex.ac.uk/courses/pg00435/1/msc-advanced-computer-science")
add("انگلستان", "University of Essex", "Colchester", "MSc Artificial Intelligence", "AI", "۱ سال", "£24,675", ("GBP", 24675, None),
    "2:2 در رشتهٔ کامپیوتری/ریاضی", "6.0", "=438", "Safe/Target", "ورودی اکتبر ۲۰۲۶ تأیید شده",
    "https://www.essex.ac.uk/courses/pg00457/1/msc-artificial-intelligence")
add("انگلستان", "University of Leicester", "Leicester", "MSc Advanced Computer Science", "SE", "۱ سال", "£24,250", ("GBP", 24250, None),
    "2:1 (سابقهٔ کار مرتبط جبران می‌کند)", "6.5", "=314", "Target", "رتبهٔ بهتر با شهریهٔ نزدیک Essex",
    "https://le.ac.uk/courses/advanced-computer-science-msc/2026")
add("انگلستان", "University of Leicester", "Leicester", "MSc Artificial Intelligence", "AI", "۱ سال", "£24,250", ("GBP", 24250, None),
    "2:1", "6.5", "=314", "Target", "",
    "https://le.ac.uk/courses/artificial-intelligence-msc/2026")
add("انگلستان", "University of Leicester", "Leicester", "MSc Cloud Computing", "CLOUD", "۱ سال", "£24,250", ("GBP", 24250, None),
    "2:1", "6.5", "=314", "Target", "یکی از معدود ارشدهای خالص Cloud در انگلستان",
    "https://le.ac.uk/courses/cloud-computing-msc/2026")
add("انگلستان", "Brunel University London", "London-Uxbridge", "MSc Artificial Intelligence", "AI", "۱ سال", "£24,795", ("GBP", 24795, None),
    "2:2", "6.5", "353", "Safe/Target", "لندن = بازار کار بزرگ ولی زندگی £1,400–1,800/ماه؛ بورس تا £6,000 تضمینی نیست",
    "https://www.brunel.ac.uk/study/courses/artificial-intelligence-msc")
add("انگلستان", "Brunel University London", "London-Uxbridge", "MSc Data Science and Analytics", "DS", "۱ سال", "£24,795", ("GBP", 24795, None),
    "2:2", "6.5", "353", "Safe/Target", "",
    "https://www.brunel.ac.uk/study/courses/data-science-and-analytics-msc")
add("انگلستان", "University of Kent", "Canterbury", "MSc Cyber Security (NCSC fully certified + BCS)", "CY", "۱ سال", "≈ £23,500", ("GBP", 23500, None),
    "«good 2:2»", "6.5", "415", "Target", "گواهی کامل NCSC = معتبرترین برچسب امنیت در بریتانیا؛ رقم شهریه از مرجع ثانویه",
    "https://www.kent.ac.uk/courses/postgraduate/1225/cyber-security")
add("انگلستان", "Royal Holloway, University of London", "Egham", "MSc Information and Cyber Security", "CY", "۱ سال", "£25,500", ("GBP", 25500, None),
    "2:2", "6.5", "=485", "Target", "قدیمی‌ترین گروه امنیت اطلاعات بریتانیا (ISG)؛ NCSC certified",
    "https://www.royalholloway.ac.uk/studying-here/postgraduate/information-security/information-and-cyber-security/")
add("انگلستان", "Goldsmiths, University of London", "London-NewCross", "MSc Computer Games Programming", "GD", "۱ سال", "£22,000", ("GBP", 22000, None),
    "مدرک second-class در رشتهٔ برنامه‌نویسی", "6.5 (6.0)", "≈ 800–1000", "Safe/Target", "پورتفولیوی Unity/C# شما اینجا مستقیماً به کار می‌آید؛ بازار بازی ۲۰۲۲–۲۵ ضعیف",
    "https://www.gold.ac.uk/pg/msc-computer-games-programming/")
add("انگلستان", "University of Surrey", "Guildford", "MSc Artificial Intelligence", "AI", "۱ سال", "≈ £26,900–27,500", ("GBP", 26900, 27500),
    "2:2", "6.5", "=246", "Target", "Guildford قطب بازی‌سازی و امنیت بریتانیا (نزدیک لندن)؛ رقم AI برآورد است (Cyber همین دانشگاه: £26,900 برای سپتامبر ۲۰۲۷ رسمی)",
    "https://www.surrey.ac.uk/postgraduate/artificial-intelligence-msc")
add("انگلستان", "University of Surrey", "Guildford", "MSc Cyber Security (NCSC)", "CY", "۱ سال", "£26,900 (ورودی سپتامبر ۲۰۲۷ — رسمی؛ فوریه ۲۰۲۷: £25,900)", ("GBP", 26900, None),
    "2:2", "6.5 (W 6.0)", "=246", "Target", "رقم رسمی دقیقاً برای سال ورود شما (سپتامبر ۲۰۲۷)",
    "https://www.surrey.ac.uk/postgraduate/cyber-security-msc")
add("انگلستان", "University of York", "York", "MSc Advanced Computer Science", "SE", "۱ سال", "£32,900", ("GBP", 32900, None),
    "2:2 با پیش‌زمینهٔ قوی", "6.5", "=158", "Target/Reach", "Russell Group؛ گران",
    "https://www.york.ac.uk/study/postgraduate-taught/courses/msc-advanced-computer-science/")
add("انگلستان", "University of York", "York", "MSc Human-Centred Interactive Technologies", "HCI", "۱ سال", "£32,900", ("GBP", 32900, None),
    "2:2", "6.5", "=158", "Target", "بهترین برنامهٔ HCI انگلستان برای معدل شما؛ ولی بازار UX ضعیف",
    "https://www.york.ac.uk/study/postgraduate-taught/courses/msc-human-centred-interactive-technologies/")
add("انگلستان", "Newcastle University (Russell Group)", "Newcastle", "MSc Computer Game Engineering", "GD", "۱ سال", "£32,300 (2026)", ("GBP", 32300, None),
    "2:2 در رشتهٔ کامپیوتری/ریاضی‌محور (طبق QS TopUniversities و IDP — صفحهٔ رسمی را چک کنید)", "6.5", "149", "Target/Reach", "معتبرترین ارشد مهندسی بازی انگلستان؛ گران",
    "https://www.ncl.ac.uk/postgraduate/")
add("انگلستان", "Lancaster University", "Lancaster", "MSc Cyber Security", "CY", "۱ سال", "£30,000 (بورس خودکار £4,500 با 2:1)", ("GBP", 30000, None),
    "2:1", "6.5", "164", "Reach", "NCSC-certified؛ شرط 2:1 برای معدل شما سخت است",
    "https://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/cyber-security-msc/2026/")
add("انگلستان", "University of Sheffield (Russell Group)", "Sheffield", "MSc Artificial Intelligence", "AI", "۱ سال", "≈ £32,900–34,340 (2026؛ MSc AI for Engineering همین دانشگاه رسماً £32,905)", ("GBP", 32900, 34340),
    "2:1", "6.5", "82", "Reach", "رتبهٔ بالا، شهریه و شرط ورود بالا؛ رقم دقیق MSc AI را از صفحهٔ رسمی بگیرید",
    "https://www.sheffield.ac.uk/postgraduate/taught/courses")

# ===== سوئیس (CHF) =====
add("انگلستان", "Imperial College London (Russell Group)", "London-Central", "MSc Computing (Artificial Intelligence and Machine Learning) / MSc Computing", "AI", "۱ سال", "£46,000 (2026/27 رسمی؛ 2027/28 هنوز اعلام نشده)", ("GBP", 46000, None),
    "First-class honours در رشته‌ای با محتوای قابل توجه Computing — برای مدرک ایرانی ≥ ۱۷–۱۸/۲۰ → با ۱۵.۷۷ رسماً واجد شرایط نیستید", "7.0 (higher requirement؛ هر بخش ≥ 6.5)", "=2", "Reach", "QS 2027 #2 · LEO: میانهٔ درآمد فارغ‌التحصیلان Computing پنج سال بعد £79,600 · دورهای ۲۰۲۷: ۶ ژانویه / ۱۰ مارس / ۲۸ آوریل · Imperial Inspires £15,000 (رقابتی) · ❌ عملاً بسته برای معدل شما",
    "https://www.imperial.ac.uk/study/courses/postgraduate-taught/computing-artificial-intelligence-msc/")
add("انگلستان", "UCL – University College London (Russell Group)", "London-Central", "MSc Software Systems Engineering / MSc Machine Learning (MSc Computer Science تبدیلی است و برای فارغ‌التحصیل CS باز نیست)", "SE", "۱ سال", "≈ £42,700–46,700 (2026/27؛ MSc Computer Science رسماً £42,700)", ("GBP", 42700, 46700),
    "2:1 (upper second) — جدول تطبیق ایرانِ UCL را نتوانستم رسمی تأیید کنم (معمولاً ۱۵–۱۶/۲۰)؛ ریاضی قوی؛ هزینهٔ درخواست £90؛ ودیعهٔ ۱۰٪ شهریه", "7.0 (Level 2؛ هر بخش ≥ 6.5)", "=9", "Reach", "QS 2027 #9 · High Fliers 2026: پنجمین دانشگاه هدف کارفرمایان بزرگ · لندن گران‌ترین زندگی · با ۱۵.۷۷ مرزی-پایین",
    "https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/computer-science-msc-2026")
add("انگلستان", "King's College London (Russell Group)", "London-Central", "MSc Advanced Computing / MSc Artificial Intelligence", "SE", "۱ سال", "£40,450 (2026)", ("GBP", 40450, None),
    "«high 2:1» = ۶۵٪ — جدول رسمی KCL برای ایران: ۱۷/۲۰ (2:1 معمولی = ۱۵/۲۰، First = ۱۸/۲۰) → با ۱۵.۷۷ زیر خط، مگر با سابقهٔ کار قابل توجه", "7.0 (هر بخش ≥ 6.5)", "=31", "Reach", "QS 2027 ≈ 31 · Strand، مرکز لندن · نیاز به ۱۷/۲۰ یعنی «high 2:1» — سابقهٔ کار ۲ ساله ممکن است جبران کند (خود KCL این را می‌گوید)، ولی امیدوار نباشید",
    "https://www.kcl.ac.uk/study-legacy/postgraduate/apply/entry-requirements/international")
add("انگلستان", "University of Warwick (Russell Group)", "Coventry", "MSc Computer Science", "SE", "۱ سال", "£37,460 (2026 entry)", ("GBP", 37460, None),
    "2:1 — جدول رسمی Warwick برای ایران: 1st = ۱۷/۲۰، 2:1 = ۱۵/۲۰، 2:2 = ۱۳/۲۰ → ۱۵.۷۷ ✓ (پذیرش PGT ≈ ۲۲٪، رقابتی)", "7.0 (اکثر PGT؛ بعضی 6.5)", "=69", "Target/Reach", "QS 2027 ≈ 69 · High Fliers 2026: چهارمین دانشگاه هدف کارفرمایان · Coventry ارزان‌تر از لندن · هزینهٔ درخواست £75، ودیعهٔ £2,500 · واقع‌بینانه‌ترین «برند بزرگ» برای معدل شما",
    "https://warwick.ac.uk/study/international/countryinformation/middleeast/iran/")
add("انگلستان", "University of Bristol (Russell Group)", "Bristol", "MSc Data Science (برای فارغ‌التحصیل CS/مهندسی؛ MSc Computer Science بریستول تبدیلی است)", "DS", "۱ سال", "£37,900 (2027/28 رسمی — ورودی سپتامبر ۲۰۲۷)", ("GBP", 37900, None),
    "«strong 2:1 (۶۵٪+)» در CS/مهندسی/علوم عددی؛ صفحهٔ ایرانِ بریستول: کارشناسی ۴ ساله از دانشگاه مورد تأیید با حداقل ۱۵/۲۰ → ۱۵.۷۷ حداقل را رد می‌کند ولی «strong» نیست", "6.5 (Profile E) — چک شود", "=54", "Reach", "QS 2027 ≈ 54 · LEO: میانهٔ Computing پنج سال بعد £70,300 · High Fliers: پنجم (۲۰۲۵) · Think Big Scholarship (رقابتی) · با ۱۵.۷۷ Reach",
    "https://www.bristol.ac.uk/study/postgraduate/taught/msc-data-science/")
add("انگلستان", "Durham University (Russell Group)", "Durham", "MSc Advanced Computer Science (و MSc Data Science)", "SE", "۱ سال", "£34,500 (2026 entry)", ("GBP", 34500, None),
    "2:1 در CS — جدول رسمی Durham برای ایران: 1st ≥ ۱۷/۲۰، 2:1 = ۱۴–۱۶/۲۰، 2:2 = ۱۲–۱۳/۲۰ (دانشگاه باید در فهرست Ecctis باشد) → ۱۵.۷۷ ✓", "6.5 (هر بخش ≥ 6.0)", "=94", "Target", "QS 2027 ≈ 94 · High Fliers 2025: دهم · ارزان‌ترین شهر بین این شش · ارزان‌ترین Russell Group این فهرست بعد از York/Newcastle · شروع سپتامبر ۲۰۲۶ اعلام شده؛ ۲۰۲۷ مشابه",
    "https://www.durham.ac.uk/study/courses/advanced-computer-science-g5t609/")
add("سوئیس", "USI – Università della Svizzera italiana", "Lugano", "MSc Informatics (گرایش‌ها: Artificial Intelligence، Software Development، Systems…)", "SE", "۲ سال (120 ECTS)", "CHF 4,000 در ترم برای غیرمقیم سوئیس (CHF 8,000/سال)", ("CHF", 8000, None),
    "کارشناسی CS/مرتبط؛ فارغ‌التحصیل UAS با ۳۰–۶۰ ECTS تکمیلی؛ بررسی موردی", "B2 در ورود (IELTS 5.5) → C1 (7.0) تا فارغ‌التحصیلی", "=456", "Target", "کم‌شرط‌ترین ورود سوئیس؛ Lugano ارزان‌ترین شهر دانشگاهی سوئیس؛ مهلت غیر-EU ۳۰ آوریل ۲۰۲۷؛ زبان شهر ایتالیایی",
    "https://www.usi.ch/en/education/master/informatics")
add("سوئیس", "USI – Università della Svizzera italiana", "Lugano", "MSc Artificial Intelligence (با IDSIA)", "AI", "۲ سال (120 ECTS)", "CHF 4,000 در ترم برای غیرمقیم (CHF 8,000/سال)", ("CHF", 8000, None),
    "کارشناسی CS/مرتبط با ریاضی و برنامه‌نویسی قوی؛ بررسی موردی", "6.5 (B2؛ C1 تا پایان دوره)", "=456", "Target", "اولین ارشد AI سوئیس؛ IDSIA (آزمایشگاه Schmidhuber/LSTM)؛ رقابتی‌تر از Informatics",
    "https://www.usi.ch/en/education/master/artificial-intelligence")
add("سوئیس", "USI – Università della Svizzera italiana", "Lugano", "MSc Software and Data Engineering", "DS", "۲ سال (120 ECTS)", "CHF 4,000 در ترم برای غیرمقیم (CHF 8,000/سال)", ("CHF", 8000, None),
    "کارشناسی CS/مرتبط", "B2 → C1", "=456", "Target", "ترکیب مهندسی نرم‌افزار + مهندسی داده (Data Engineering — همان توصیهٔ شیت حوزه‌ها)؛ کم‌رقابت‌تر از AI",
    "https://www.usi.ch/en/education/master/software-and-data-engineering")
add("سوئیس", "Hochschule Luzern (HSLU)", "Luzern", "MSc Applied Data Science and AI (نام جدید از اوت ۲۰۲۶؛ قبلاً Applied Information and Data Science)", "DS", "۲ سال (120 ECTS؛ معمولاً ۴ ترم، قابل تمدید تا ۸)", "CHF 1,300 در ترم (خارجی) + ≈ CHF 275 هزینهٔ جانبی ≈ CHF 3,150/سال؛ هزینهٔ درخواست CHF 250", ("CHF", 3150, None),
    "هر کارشناسی (دانشگاه یا UAS)؛ آزمون انگلیسی + آزمون استعداد HSLU", "C1 (B2 مشروط)", "—", "Safe/Target", "«باز برای تغییر رشته‌ای‌ها»، کاربردی و مدیریتی؛ ترکیبی (حضوری/آنلاین)؛ آلمانی لازم نیست؛ شروع سپتامبر/فوریه؛ ⚠️ مهلت ویزایی‌ها ۱ آوریل ۲۰۲۷ (رسمی؛ Swiss/EU تا ۱ ژوئن)",
    "https://www.hslu.ch/en/lucerne-school-of-business/degree-programmes/master/applied-data-science-and-ai/")
add("سوئیس", "University of Bern", "Bern", "Swiss Joint MSc Computer Science (Bern / Neuchâtel / Fribourg)", "SE", "۱.۵ سال (90 ECTS)", "CHF 850 + 1,700 اضافهٔ غیرسوئیسی‌ها (از پاییز ۲۰۲۶) + 34 + 25 = CHF 2,609 در ترم (≈ CHF 5,200/سال)", ("CHF", 5218, None),
    "کارشناسی Computer Science یا معادل (بررسی موردی؛ حداکثر ۶۰ ECTS تکمیلی — دروس تکمیلی ممکن است آلمانی/فرانسه باشند)", "بدون آزمون (B2 توصیه — FAQ رسمی)", "=191", "Target", "⚠️ شهریهٔ خارجی‌ها از پاییز ۲۰۲۶ سه‌برابر شد (رسمی unibe.ch) → همان مدرک مشترک را از Neuchâtel (CHF 790/ترم) یا Fribourg (CHF 985/ترم) بگیرید؛ مهلت ۳۰ آوریل — ویزایی‌ها مهلت دیرهنگام ندارند",
    "https://www.philnat.unibe.ch/studies/study_programs/master_s_in_computer_science/index_eng.html")
add("سوئیس", "University of Neuchâtel", "Neuchatel", "Swiss Joint MSc Computer Science (ثبت‌نام در Neuchâtel)", "SE", "۱.۵ سال (90 ECTS)", "CHF 790 در ترم (خارجی؛ شامل همهٔ هزینه‌ها) = CHF 1,580/سال", ("CHF", 1580, None),
    "کارشناسی CS یا معادل (بررسی موردی؛ حداکثر ۶۰ ECTS تکمیلی)", "بدون آزمون (B2 توصیه — FAQ رسمی)", "—", "Target", "ارزان‌ترین شهریهٔ سوئیس؛ همان مدرک مشترک Bern/Fribourg (دروس در سه شهر، بلیت قطار جبران می‌شود)؛ مهلت ۳۰ آوریل (خارجی‌ها: تا ۳۱ مارس بفرستید)؛ هزینهٔ پرونده CHF 100 از شهریه کم می‌شود؛ شهر فرانسه‌زبان",
    "https://mcs.unibnf.ch/")
add("سوئیس", "University of Fribourg", "Fribourg", "Swiss Joint MSc Computer Science (ثبت‌نام در Fribourg)", "SE", "۱.۵ سال (90 ECTS)", "CHF 870 + 115 = CHF 985 در ترم (خارجی؛ رسمی) = CHF 1,970/سال", ("CHF", 1970, None),
    "کارشناسی CS یا معادل (بررسی موردی؛ حداکثر ۶۰ ECTS تکمیلی)", "بدون آزمون (B2 توصیه — FAQ رسمی)", "=670", "Target", "همان برنامهٔ مشترک Bern/Neuchâtel؛ شهر دوزبانه و ارزان‌تر؛ ⚠️ مهلت ویزایی‌ها ۱–۲۸ فوریه ۲۰۲۷ (رسمی unifr.ch)",
    "https://www.unifr.ch/inf/en/")
add("سوئیس", "University of Basel", "Basel", "MSc Computer Science", "SE", "۱.۵ سال (90 ECTS)", "CHF 850 در ترم (برای همه؛ بدون اضافهٔ خارجی‌ها — رسمی 2026/27) = CHF 1,700/سال", ("CHF", 1700, None),
    "کارشناسی CS یا معادل با نمرات خوب؛ بررسی فردی", "B2–C1 (چک شود)", "=150", "Target/Reach", "رتبهٔ ۱۵۰؛ 90 ECTS انگلیسی؛ هزینهٔ درخواست CHF 100؛ ⚠️ کانتون Basel تمکن CHF 24,000/سال می‌خواهد؛ مهلت ۳۰ آوریل (رسمی)",
    "https://dmi.unibas.ch/en/studies/computer-science/masters/")
add("سوئیس", "University of Zurich (UZH)", "Zuerich", "MSc Informatics (گرایش‌ها: Software Systems، Data Science، People-Oriented Computing…)", "SE", "۱.۵–۲ سال (90/120 ECTS)", "CHF 720 + 100 (خارجی) + 59 = CHF 879 در ترم (≈ CHF 1,760/سال)", ("CHF", 1760, None),
    "کارشناسی Informatics/CS با نمرات بسیار خوب؛ فقط یک درخواست در هر ترم؛ هزینهٔ درخواست CHF 150", "C1 / IELTS 7.0", "=98", "Reach", "⚠️ مهلت ویزایی‌ها ۲۸ فوریه ۲۰۲۷ (بدون ویزا ۳۰ آوریل)؛ کانتون زوریخ: تمکن CHF 21,000 فقط در بانک سوئیسی به نام خودتان",
    "https://www.ifi.uzh.ch/en/studies/master.html")
add("سوئیس", "ZHAW School of Engineering", "Zuerich-Winterthur", "MSc in Engineering (MSE) — پروفایل Computer Science / Data Science / Information & Cyber Security", "MULTI", "۱.۵ سال (90 ECTS؛ پاره‌وقت تا ۳ سال)", "CHF 1,220 در ترم (خارجی) + CHF 60 ≈ CHF 2,560/سال", ("CHF", 2560, None),
    "کارشناسی با نمرات A یا B (≈ یک‌سوم بالای کلاس) — گواهی رتبهٔ کلاسی از سمنان بگیرید", "B2–C1", "851–900", "Target/Reach", "کاربردی و پروژه‌محور (کار در مؤسسات ZHAW، اغلب با حقوق دستیاری)؛ مهلت پایان آوریل؛ کانتون زوریخ (تمکن در بانک سوئیسی)",
    "https://www.zhaw.ch/en/engineering/study/masters-degree-programme")
add("سوئیس", "EPFL", "Lausanne", "MSc Computer Science", "SE", "۲ سال (120 ECTS)", "CHF 2,240 در ترم برای خارجی‌های غیرمقیم (از پاییز ۲۰۲۵؛ ≈ CHF 4,480/سال)", ("CHF", 4480, None),
    "کارشناسی CS با نمرات عالی (بالای کلاس)؛ فقط یک برنامه در سال", "مدرک زبان الزامی نیست (C1 عملاً لازم)", "=22", "Reach", "دور اول ۱۵ دسامبر ۲۰۲۶ (توصیه برای ویزایی‌ها؛ پاسخ اوایل آوریل)، دور دوم ۳۱ مارس ۲۰۲۷؛ ⚠️ احتمال افزایش دوبارهٔ شهریه (EP27)",
    "https://www.epfl.ch/education/master/programs/computer-science/")
add("سوئیس", "EPFL", "Lausanne", "MSc Data Science", "DS", "۲ سال (120 ECTS)", "CHF 2,240 در ترم (≈ CHF 4,480/سال)", ("CHF", 4480, None),
    "کارشناسی CS/ریاضی/مهندسی با نمرات عالی", "مدرک زبان الزامی نیست", "=22", "Reach", "بسیار رقابتی؛ کارآموزی صنعتی جزو برنامه است",
    "https://www.epfl.ch/education/master/programs/data-science/")
add("سوئیس", "ETH Zürich", "Zuerich", "MSc Computer Science", "SE", "۲ سال (120 ECTS)", "CHF 2,190 + ≈ CHF 74 = ≈ CHF 2,264 در ترم (≈ CHF 4,530/سال)", ("CHF", 4530, None),
    "کارشناسی CS با نمرات ممتاز (عملاً ۱۰٪ بالای کلاس)؛ هزینهٔ درخواست CHF 150؛ تا ۲ برنامه", "C1 / IELTS 7.0", "=8", "Reach", "بهترین دانشگاه قارهٔ اروپا؛ اپلای فقط ۱–۳۰ نوامبر ۲۰۲۶، پاسخ تا پایان مارس ۲۰۲۷، شروع ۲۰ سپتامبر ۲۰۲۷؛ با معدل ۱۵.۷۷ احتمال پذیرش کم",
    "https://ethz.ch/en/studies/master/degree-programmes/engineering-sciences/computer-science.html")
add("سوئیس", "ETH Zürich + EPFL", "Zuerich", "MSc Cyber Security (مشترک ETH–EPFL؛ یک سال در هر کدام)", "CY", "۲ سال (120 ECTS)", "شهریهٔ ETH: ≈ CHF 2,264 در ترم (≈ CHF 4,530/سال)", ("CHF", 4530, None),
    "کارشناسی CS با نمرات ممتاز؛ پیش‌زمینهٔ ریاضی/سیستم قوی", "C1 / IELTS 7.0", "=8", "Reach", "قوی‌ترین ارشد امنیت اروپا؛ همان پنجرهٔ نوامبر ETH؛ Reach",
    "https://ethz.ch/en/studies/master/degree-programmes/engineering-sciences/cyber-security.html")

# ===== آلمان (EUR) =====
add("آلمان", "Universität Stuttgart", "Stuttgart", "M.Sc. Computer Science (انگلیسی، بدون NC)", "SE", "۲ سال", "€1,500 در ترم + ≈ €200 سهم ترم = ≈ €3,400/سال", ("EUR", 3400, None),
    "کارشناسی CS/مرتبط؛ بدون NC", "7.0 (C1)", "318", "Target", "شهریهٔ بادن-وورتمبرگ برای غیر-EU",
    "https://www.uni-stuttgart.de/en/study/study-programs/")
add("آلمان", "Universität Stuttgart", "Stuttgart", "M.Sc. Information Technology (INFOTECH)", "EMB", "۲ سال", "€1,500 در ترم + سهم ترم ≈ €3,400/سال", ("EUR", 3400, None),
    "کارشناسی EE/CS/Computer Engineering؛ گزینش", "7.0 (C1)", "318", "Target", "گرایش‌های Embedded/Communication؛ Bosch و Daimler همان شهر",
    "https://www.mygermanuniversity.com/master/information-technology-infotech/678")
add("آلمان", "FAU Erlangen-Nürnberg", "Erlangen", "M.Sc. Artificial Intelligence", "AI", "۲ سال", "€4,000 در ترم برای غیر-EU از ترم تابستان ۲۰۲۷ (€8,000/سال) + €82 سهم ترم", ("EUR", 8164, None),
    "کارشناسی CS/مرتبط؛ بررسی ریزنمرات", "B2 (IELTS 6.0)", "218", "Target", "⚠️ FAU طبق BayHIG §13 از تابستان ۲۰۲۷ برای ورودی‌های جدید غیر-EU شهریه می‌گیرد (AI و CS: €4,000/ترم) — ورودی اکتبر ۲۰۲۷ شما مشمول است؛ دیگر «رایگان» نیست. Siemens/adidas/Schaeffler در منطقه",
    "https://www.fau.eu/degree-program/artificial-intelligence-m-sc/")
add("آلمان", "FAU Erlangen-Nürnberg", "Erlangen", "M.Sc. Autonomy Technologies", "EMB", "۲ سال", "€2,000 در ترم از تابستان ۲۰۲۷ (€4,000/سال) + €82 سهم ترم", ("EUR", 4164, None),
    "کارشناسی مرتبط؛ آلمانی لازم نیست", "B2 (IELTS 6.0)", "218", "Target", "رباتیک/خودران؛ ⚠️ مشمول شهریهٔ جدید FAU از ۲۰۲۷ (صفحهٔ رسمی شهریه، ۲۰۲۶)",
    "https://www.fau.eu/degree-program/autonomy-technologies-m-sc/")
add("آلمان", "TU Darmstadt", "Darmstadt", "M.Sc. Distributed Software Systems (انگلیسی)", "CLOUD", "۲ سال", "€0 + ≈ €300 سهم ترم (≈ €600/سال)", ("EUR", 600, None),
    "کارشناسی CS با پیش‌نیازهای مشخص", "≈ 7.0 (C1) — چک شود", "250", "Target/Reach", "منطقهٔ Rhein-Main (SAP، Deutsche Bank، Software AG)",
    "https://www.tu-darmstadt.de/studieren/")
add("آلمان", "TU Dresden", "Dresden", "M.Sc. Computer Science (انگلیسی)", "SE", "۲ سال", "€0 + ≈ €300 سهم ترم", ("EUR", 600, None),
    "کارشناسی CS؛ ارزیابی استعداد", "7.0", "185", "Reach", "Dresden ارزان‌ترین شهر جدول؛ GlobalFoundries/Infineon/Bosch",
    "https://tu-dresden.de/studium/vor-dem-studium/studienangebot")
add("آلمان", "Saarland University (UdS)", "Saarbruecken", "M.Sc. Cybersecurity", "CY", "۲ سال", "€0 + ≈ €394 سهم ترم (≈ €790/سال)", ("EUR", 790, None),
    "کارشناسی CS + اثبات دروس پایه + ۲ توصیه‌نامه؛ بدون NC", "7.0 (C1؛ MOI پذیرفته نمی‌شود)", "=588 (CS ≈ 251)", "Target", "CISPA — بهترین مرکز امنیت آلمان؛ IELTS 7 شرط سخت شماست",
    "https://www.uni-saarland.de/en/study/programmes/master/cybersecurity.html")
add("آلمان", "Saarland University (UdS)", "Saarbruecken", "M.Sc. Data Science and Artificial Intelligence", "AI", "۲ سال", "€0 + ≈ €394 سهم ترم", ("EUR", 790, None),
    "کارشناسی CS/مرتبط؛ بدون NC", "7.0 (C1)", "=588 (CS ≈ 251)", "Target", "MPI Informatics و DFKI در همان کمپوس",
    "https://www.uni-saarland.de/en/study/programmes/master/data-science.html")
add("آلمان", "TU Chemnitz", "Chemnitz", "M.Sc. Automotive Software Engineering", "EMB", "۲ سال", "€0 + ≈ €320 سهم ترم (≈ €640/سال)", ("EUR", 640, None),
    "کارشناسی CS/مرتبط؛ بدون محدودیت پذیرش", "B2 (IELTS 5.5)", "—", "Safe", "آسان‌ترین ورود؛ شهر ارزان؛ ولی صنعت خودرو ۲۰۲۴–۲۵ ضعیف و آلمانی در کارفرمایان محلی",
    "https://www.mygermanuniversity.com/master/automotive-software-engineering/91")
add("آلمان", "Universität Passau", "Passau", "M.Sc. Artificial Intelligence Engineering", "AI", "۲ سال", "€0 + ≈ €100–200 سهم ترم", ("EUR", 300, None),
    "معدل آلمانی ≤ 2.7 (معدل شما ≈ 2.3 ✓)؛ ۳۵ ECTS ریاضی + ۴۰ ECTS CS", "B2؛ + آلمانی A1 تا پایان سال اول (کلاس رایگان)", "—", "Safe", "کاملاً انگلیسی؛ شهر کوچک و ارزان؛ Passau رسماً اعلام کرده «فعلاً» شهریهٔ غیر-EU نمی‌گیرد (برخلاف FAU/TUM) ولی طبق قانون باواریا می‌تواند — قبل از اپلای چک کنید",
    "https://www.uni-passau.de/en/msc-ai-eng")
add("آلمان", "Otto-von-Guericke-Universität (OVGU)", "Magdeburg", "M.Sc. Data and Knowledge Engineering", "DS", "۲ سال", "€0 + ≈ €311 سهم ترم", ("EUR", 620, None),
    "معدل آلمانی ≤ 2.3 (معدل شما ≈ 2.27 — دقیقاً مرزی)؛ کارشناسی CS", "6.0–7.0 (منابع متناقض؛ رسمی را چک کنید)", "—", "Safe/Target", "",
    "https://www.dke.ovgu.de/")
add("آلمان", "TH Köln – Cologne Game Lab", "Koeln", "M.A. Game Development and Research", "GD", "۲ سال", "€2,500 در ترم (غیر-EU) + €277 سهم ترم ≈ €5,550/سال", ("EUR", 5550, None),
    "هر کارشناسی + ≥ ۱۲ ماه سابقهٔ مرتبط + آزمون استعداد (مهلت ۳۱ مارس)", "B2", "— (UAS)", "Target", "معتبرترین مدرسهٔ بازی آلمان؛ ۷ ماه Unity + ۲ سال IT شما احتمالاً شرط ۱۲ ماه را می‌پوشاند — بپرسید",
    "https://colognegamelab.de/study-programs/post-graduate-programs/game-development-research-ma/faqs/")
add("آلمان", "Universität Siegen", "Siegen", "M.Sc. Human Computer Interaction", "HCI", "۲ سال", "€0 + ≈ €372 سهم ترم", ("EUR", 745, None),
    "معدل آلمانی ≤ 2.5؛ کارشناسی CS/IS/Design/Psychology", "6.5", "—", "Safe", "شروع زمستان و تابستان؛ شهر کوچک",
    "https://www2.daad.de/deutschland/studienangebote/international-programmes/en/detail/4686/")
add("آلمان", "Hochschule Bonn-Rhein-Sieg (H-BRS)", "SanktAugustin", "M.Sc. Autonomous Systems", "EMB", "۲ سال", "€0 + €349 سهم ترم", ("EUR", 700, None),
    "معدل آلمانی ≤ 2.5؛ ۲۵ جای محدود؛ آزمون استعداد؛ uni-assist", "6.5 (B2+)", "— (UAS)", "Target", "رباتیک کاربردی با Fraunhofer؛ نزدیک Bonn/Köln",
    "https://www.h-brs.de/en/inf/admission-application-master-autonomous-systems")
add("آلمان", "RWTH Aachen", "Aachen", "M.Sc. Software Systems Engineering", "SE", "۲ سال", "€0 + ≈ €330 سهم ترم", ("EUR", 660, None),
    "کارشناسی CS، معدل ≥ ۶۵٪ (شما ۷۹٪ ✓)؛ ۲ درس پیشرفتهٔ سیستم؛ مهلت ۱ مارس", "B2 (IELTS 5.5)", "104", "Reach", "TU9؛ رقابتی — معدل شما حداقل را رد می‌کند ولی متقاضیان قوی‌ترند",
    "https://sc.informatik.rwth-aachen.de/en/studium/master/sse/")
add("آلمان", "Universität Tübingen", "Tuebingen", "M.Sc. Machine Learning", "AI", "۲ سال", "€1,500 در ترم + ≈ €200 = ≈ €3,400/سال", ("EUR", 3400, None),
    "کارشناسی CS/ریاضی؛ آزمون توانایی؛ مهلت ۳۰ آوریل", "7.0", "=230", "Reach", "Cyber Valley — بهترین ML آلمان؛ پذیرش بسیار سخت",
    "https://uni-tuebingen.de/fakultaeten/mathematisch-naturwissenschaftliche-fakultaet/fachbereiche/informatik/studium/studierende/lehre-studienorganisation/studiengaenge/machine-learning/admission-and-application/")
add("آلمان", "TU München (TUM)", "Muenchen", "M.Sc. Informatics", "SE", "۲ سال", "€6,000 در ترم برای غیر-EU (€12,000/سال) + €97", ("EUR", 12200, None),
    "کارشناسی CS؛ ارزیابی استعداد؛ بسیار رقابتی", "6.5", "≈ 25", "Reach", "⚠️ TUM از ۲۰۲۴ شهریهٔ غیر-EU می‌گیرد — دیگر «رایگان» نیست؛ Munich گران‌ترین شهر آلمان",
    "https://www.tum.de/en/studies/degree-programs/detail/informatics-master-of-science-msc")

# ===== هلند (EUR) =====
add("هلند", "University of Twente (UT)", "Enschede", "MSc Computer Science (گرایش‌ها: Cyber Security، Data Science، Software Tech، ...)", "SE", "۲ سال", "€21,700", ("EUR", 21700, None),
    "حداقل رسمی برای مدرک ایرانی ۱۵/۲۰", "6.5", "223", "Target", "گزینهٔ Target جدول اصلی",
    "https://www.utwente.nl/en/education/master/programmes/computer-science/")
add("هلند", "University of Twente (UT)", "Enschede", "MSc Embedded Systems", "EMB", "۲ سال", "€21,700", ("EUR", 21700, None),
    "CGPA ≥ ۷۰–۷۵٪؛ کارشناسی CS/EE/Computer Eng", "6.5", "223", "Target", "شهریهٔ رسمی 2026/27؛ مهلت غیر-EU ۱ مه",
    "https://www.utwente.nl/en/education/master/programmes/embedded-systems/finance/")
add("هلند", "University of Twente (UT)", "Enschede", "MSc Interaction Technology", "HCI", "۲ سال", "€21,700", ("EUR", 21700, None),
    "کارشناسی CS/مرتبط", "6.5", "223", "Target", "HCI فنی (نه طراحی صرف)",
    "https://www.utwente.nl/en/education/master/programmes/interaction-technology/")
add("هلند", "Radboud University", "Nijmegen", "MSc Computing Science (گرایش‌ها: Cyber Security، Data Science، Software Science)", "SE", "۲ سال", "€19,714 (2026/27 — نرخ رسمی دانشکدهٔ علوم)", ("EUR", 19714, None),
    "کارشناسی CS با ریاضی/الگوریتم کافی", "6.5", "283", "Target", "گزینهٔ Target جدول اصلی",
    "https://www.ru.nl/en/education/masters/computing-science")
add("هلند", "Radboud University", "Nijmegen", "MSc Artificial Intelligence", "AI", "۲ سال", "€19,714 (2026/27 — نرخ رسمی دانشکدهٔ علوم)", ("EUR", 19714, None),
    "کارشناسی CS/AI/مرتبط", "6.5", "283", "Target", "AI شناختی (Donders Institute)",
    "https://www.ru.nl/en/education/masters/artificial-intelligence")
add("هلند", "Leiden University", "Leiden", "MSc Computer Science (گرایش‌ها: Artificial Intelligence، Data Science، ...)", "MULTI", "۲ سال", "€22,500", ("EUR", 22500, None),
    "کارشناسی CS", "6.5", "119", "Target/Reach", "شهریهٔ رسمی 2026/27؛ نزدیک Den Haag/Amsterdam",
    "https://www.universiteitleiden.nl/en/education/study-programmes/master/computer-science/artificial-intelligence/admission-and-application/tuition-fees")
add("هلند", "University of Groningen (RUG)", "Groningen", "MSc Artificial Intelligence", "AI", "۲ سال", "€24,900", ("EUR", 24900, None),
    "کارشناسی AI/CS با ریاضی", "6.5", "157", "Target/Reach", "شهریهٔ رسمی 2026/27؛ بورس ASML €5k",
    "https://www.rug.nl/masters/artificial-intelligence/?lang=en")
add("هلند", "University of Groningen (RUG)", "Groningen", "MSc Computing Science", "SE", "۲ سال", "≈ €21,400 (2025) → ≈ €22,500", ("EUR", 22500, None),
    "کارشناسی CS", "6.5", "157", "Target", "",
    "https://www.rug.nl/masters/computing-science/?lang=en")
add("هلند", "Utrecht University", "Utrecht", "MSc Game and Media Technology", "GD", "۲ سال", "€25,306", ("EUR", 25306, None),
    "کارشناسی CS؛ ارشد پژوهشی گزینشی", "6.5", "113", "Reach", "تنها ارشد پژوهشی بازی هلند؛ Utrecht قطب استودیوهای بازی",
    "https://www.uu.nl/en/masters/game-and-media-technology")
add("هلند", "Utrecht University", "Utrecht", "MSc Artificial Intelligence", "AI", "۲ سال", "€25,306", ("EUR", 25306, None),
    "کارشناسی CS/AI؛ گزینشی", "6.5", "113", "Reach", "همان باند شهریهٔ Utrecht 2026/27",
    "https://www.uu.nl/en/masters/artificial-intelligence")
add("هلند", "University of Amsterdam (UvA)", "Amsterdam", "MSc Software Engineering (۱ ساله!)", "SE", "۱ سال", "≈ €23,540", ("EUR", 23540, None),
    "کارشناسی CS", "6.5", "60", "Target/Reach", "تنها ارشد ۱ سالهٔ معتبر هلند → کل هزینه نصف؛ اما اجارهٔ Amsterdam €900–1,300",
    "https://www.uva.nl/en/programmes/masters/software-engineering/software-engineering.html")
add("هلند", "University of Amsterdam (UvA)", "Amsterdam", "MSc Artificial Intelligence", "AI", "۲ سال", "≈ €26,000", ("EUR", 26000, None),
    "کارشناسی AI/CS با ریاضی قوی؛ بسیار رقابتی", "6.5", "60", "Reach", "",
    "https://www.uva.nl/en/programmes/masters/artificial-intelligence/artificial-intelligence.html")
add("هلند", "TU Eindhoven (TU/e)", "Eindhoven", "MSc Data Science and Artificial Intelligence", "DS", "۲ سال", "€22,400 (2027/28 رسمی؛ 2026/27: €21,700)", ("EUR", 22400, None),
    "کارشناسی CS/ریاضی؛ گزینش بر اساس معدل", "6.5", "152", "Reach", "Brainport (ASML، Philips، NXP)",
    "https://www.tue.nl/en/education/graduate-school/master-data-science-and-artificial-intelligence")
add("هلند", "TU Eindhoven (TU/e)", "Eindhoven", "MSc Embedded Systems", "EMB", "۲ سال", "€22,400 (2027/28 رسمی؛ 2026/27: €21,700)", ("EUR", 22400, None),
    "کارشناسی CS/EE؛ گزینش", "6.5", "152", "Reach", "ASML/NXP بزرگ‌ترین کارفرمایان Embedded اروپا",
    "https://www.tue.nl/en/education/graduate-school/master-embedded-systems")
add("هلند", "TU Delft", "Delft", "MSc Computer Science / MSc Computer & Embedded Systems Engineering", "SE", "۲ سال", "€22,290 (2025/26) → ≈ €23,000", ("EUR", 23000, None),
    "معدل ≥ ۷۵٪ / ۲۰٪ برتر", "7.0", "48", "Reach", "معتبرترین، ولی برای معدل ۱۵.۷۷ دور از دسترس",
    "https://www.tudelft.nl/onderwijs/opleidingen/masters/cs/msc-computer-science")
add("هلند", "Breda University of Applied Sciences (BUas)", "Breda", "Master Game Technology (۱ ساله)", "GD", "۱ سال", "≈ €15,200", ("EUR", 15200, None),
    "کارشناسی IT/برنامه‌نویسی/بازی + پیشنهاد پروژه", "6.0", "— (UAS)", "Safe/Target", "برنامهٔ بازی BUas در اروپا شناخته‌شده است؛ مدرک UAS (نه پژوهشی)",
    "https://www.topuniversities.com/universities/breda-university-applied-sciences/postgrad/master-game-technology")

# ===== سوئد (SEK) =====
add("سوئد", "Linköping University (LiU)", "Linkoping", "MSc Computer Science", "SE", "۲ سال", "SEK 166,000", ("SEK", 166000, None),
    "گزینش بر اساس گروه معدل", "6.5", "308", "Target", "گزینهٔ Target جدول اصلی",
    "https://liu.se/en/education/program/6mics")
add("سوئد", "Linköping University (LiU)", "Linkoping", "MSc Statistics and Machine Learning", "AI", "۲ سال", "≈ SEK 166,000 (همان باند)", ("SEK", 166000, None),
    "کارشناسی با ≥ ۳۰ واحد ریاضی/آمار + برنامه‌نویسی", "6.5", "308", "Target", "",
    "https://liu.se/en/education/program/f7msl")
add("سوئد", "Halmstad University", "Halmstad", "MSc Embedded and Intelligent Systems (120 cr)", "EMB", "۲ سال", "≈ SEK 151,000", ("SEK", 151000, None),
    "کارشناسی CS/EE", "6.5", "—", "Safe", "Volvo/HMS در منطقه؛ بدون رتبهٔ QS",
    "https://www.hh.se/english/education/programmes.html")
add("سوئد", "Blekinge Institute of Technology (BTH)", "Karlskrona", "MSc Software Engineering (120 cr)", "SE", "۲ سال", "SEK 140,000", ("SEK", 140000, None),
    "≥ ۹۰ واحد CS/SE", "6.5", "—", "Safe/Target", "Ericsson و Telenor در Karlskrona؛ ⚠️ نسخهٔ ۶۰ واحدی از راه دور است",
    "https://www.bth.se/eng/programmes/")
add("سوئد", "KTH Royal Institute of Technology", "Stockholm", "MSc Machine Learning", "AI", "۲ سال", "≈ SEK 180,000–190,000 (کل دوره ≈ 360k–380k)", ("SEK", 180000, 190000),
    "کارشناسی CS/ریاضی قوی؛ بسیار رقابتی", "6.5", "82", "Reach", "Stockholm گران (اتاق SEK 7–10k)؛ رقم دقیق روی kth.se فقط در سامانهٔ اپلای نمایش داده می‌شود",
    "https://www.kth.se/en/studies/master/machine-learning")
add("سوئد", "KTH Royal Institute of Technology", "Stockholm", "MSc Cybersecurity", "CY", "۲ سال", "≈ SEK 180,000–190,000", ("SEK", 180000, 190000),
    "کارشناسی CS", "6.5", "82", "Reach", "",
    "https://www.kth.se/en/studies/master/cybersecurity")
add("سوئد", "KTH Royal Institute of Technology", "Stockholm-Kista", "MSc Software Engineering of Distributed Systems", "CLOUD", "۲ سال", "SEK 180,000–190,000", ("SEK", 180000, 190000),
    "کارشناسی CS", "6.5", "82", "Target/Reach", "Kista = قطب ICT سوئد (Ericsson)",
    "https://www.kth.se/en/studies/master/software-engineering-of-distributed-systems")
add("سوئد", "Chalmers University of Technology", "Gothenburg", "MSc Data Science and AI", "DS", "۲ سال", "≈ SEK 175,000 (2026/27؛ 2025/26: 160,000)", ("SEK", 175000, None),
    "کارشناسی CS/ریاضی", "6.5", "174", "Target/Reach", "Volvo، Ericsson، Zenseact؛ مهلت ۱۵ ژانویه؛ ⚠️ طبق صفحهٔ شهریهٔ Chalmers دانشگاه‌های سوئد فعلاً نمی‌توانند از ایران پول دریافت کنند (تحریم بانکی) — پرداخت از کشور ثالث",
    "https://www.chalmers.se/en/education/find-masters-programme/data-science-and-ai-msc/")
add("سوئد", "Chalmers University of Technology", "Gothenburg", "MSc Software Engineering and Technology", "SE", "۲ سال", "≈ SEK 175,000 (2026/27)", ("SEK", 175000, None),
    "کارشناسی CS/SE", "6.5", "174", "Target", "",
    "https://www.chalmers.se/en/education/find-masters-programme/software-engineering-and-technology-msc/")
add("سوئد", "Chalmers University of Technology", "Gothenburg", "MSc Interaction Design and Technologies", "HCI", "۲ سال", "≈ SEK 175,000 (2026/27)", ("SEK", 175000, None),
    "کارشناسی CS/Design", "6.5", "174", "Target", "",
    "https://www.chalmers.se/en/education/find-masters-programme/interaction-design-and-technologies-msc/")
add("سوئد", "University of Gothenburg (مشترک با Chalmers)", "Gothenburg", "MSc Game Design & Technology", "GD", "۲ سال", "SEK 147,000 (ورودی ۲۰۲۷: کل دوره SEK 294,000 رسمی)", ("SEK", 147000, None),
    "کارشناسی CS/Design/Media", "6.5", "225", "Target", "Gothenburg: استودیوهای EA DICE/Ghost؛ بازار بازی ضعیف",
    "https://www.gu.se/en/study-gothenburg/game-design-technology-masters-programme-n2gdt")
add("سوئد", "Uppsala University", "Uppsala", "MSc Computer Science", "SE", "۲ سال", "≈ SEK 145,000–150,000", ("SEK", 145000, 150000),
    "کارشناسی CS", "6.5", "87", "Target/Reach", "رتبهٔ بالا با شهریهٔ پایین‌تر از KTH",
    "https://www.uu.se/en/study/programme/masters-programme-in-computer-science")
add("سوئد", "Umeå University", "Umea", "MSc Artificial Intelligence", "AI", "۲ سال", "SEK 152,300", ("SEK", 152300, None),
    "کارشناسی CS/ریاضی", "6.5", "438", "Target", "شمال سوئد، شهر دانشجویی ارزان؛ کل دوره SEK 304,600",
    "https://www.umu.se/en/education/master/masters-programme-in-artificial-intelligence/")
add("سوئد", "University of Skövde", "Skovde", "MSc Data Science (120 cr)", "DS", "۲ سال", "SEK 135,000", ("SEK", 135000, None),
    "کارشناسی CS/مرتبط", "6.5", "—", "Safe", "ارزان؛ Skövde قطب بازی سوئد (Sweden Game Arena)",
    "https://www.his.se/en/education/")
add("سوئد", "Mälardalen University (MDU)", "Vasteras", "MSc Intelligent Embedded Systems", "EMB", "۲ سال", "≈ SEK 135,000", ("SEK", 135000, None),
    "کارشناسی CS/EE", "6.5", "—", "Safe", "ABB و Westinghouse در Västerås؛ رقم 2024/25",
    "https://www.mdu.se/en/malardalen-university/education")
add("سوئد", "Mälardalen University (MDU)", "Vasteras", "MSc Software Engineering", "SE", "۲ سال", "≈ SEK 135,000", ("SEK", 135000, None),
    "کارشناسی CS/SE", "6.5", "—", "Safe", "",
    "https://www.mdu.se/en/malardalen-university/education")

# ===== دانمارک (EUR/DKK) =====
add("دانمارک", "Aalborg University (AAU)", "Aalborg", "MSc Computer Science (IT)", "SE", "۲ سال", "≈ €14,910 (2025/26: €7,455 در ترم؛ نرخ ۲۰۲۶ روی سایت AAU منتشر نشده — mastersportal: €15,340)", ("EUR", 14910, 15340),
    "رسمی: حداقل ۱۵۰ ECTS دروس مرتبط با CS (برنامه‌نویسی ۱۵، مهندسی نرم‌افزار ۵، الگوریتم ۵، پایگاه داده ۵، ریاضیات گسسته ۵)؛ از ورودی ۲۰۲۷ سابقهٔ کار و انگیزه‌نامه هم در رتبه‌بندی حساب می‌شود", "6.5 (هر بخش ≥ 6.0)", "=329", "Target", "گزینهٔ Target جدول اصلی؛ PBL (پروژه‌محور)؛ ظرفیت محدود",
    "https://www.en.aau.dk/education/master/computer-science-it")
add("دانمارک", "Aalborg University (AAU)", "Aalborg", "MSc Software", "SE", "۲ سال", "≈ €14,910–15,340", ("EUR", 14910, 15340),
    "کارشناسی SE/CS", "6.5", "=329", "Target", "",
    "https://www.en.aau.dk/education/master/software")
add("دانمارک", "Aalborg University (AAU)", "Copenhagen-AAU", "MSc Eng Cyber Security", "CY", "۲ سال", "≈ €14,910–15,340", ("EUR", 14910, 15340),
    "کارشناسی CS/EE مرتبط؛ مهلت ۱ مارس", "6.5", "=329", "Target", "کمپوس کپنهاگ: اجاره بالاتر ولی بازار کار بزرگ",
    "https://www.en.aau.dk/education/master/cyber-security/")
add("دانمارک", "Aalborg University (AAU)", "Aalborg-or-Copenhagen", "MSc Medialogy", "HCI", "۲ سال", "≈ €14,910–15,340", ("EUR", 14910, 15340),
    "کارشناسی مرتبط (Medialogy، CS، Media Tech)", "6.5", "=329", "Target", "تعامل، AR/VR، بازی؛ بین HCI و Game",
    "https://www.en.aau.dk/education/master/medialogy-aal")
add("دانمارک", "University of Southern Denmark (SDU)", "Odense", "MSc Computer Science", "SE", "۲ سال", "€17,300 (از ورودی سپتامبر ۲۰۲۶؛ قبلاً €13,900)", ("EUR", 17300, None),
    "≥ ۱۰۰ ECTS دروس CS؛ ظرفیت محدود + آزمون", "6.5", "=283", "Target", "⚠️ افزایش شهریهٔ ۲۰۲۶ — جدول اصلی اصلاح شد",
    "https://www.sdu.dk/en/uddannelse/fees_and_funding/tuition")
add("دانمارک", "University of Southern Denmark (SDU)", "Odense", "MSc Eng Software Engineering", "SE", "۲ سال", "€17,300", ("EUR", 17300, None),
    "کارشناسی SE/CS", "6.5", "=283", "Target", "گرایش‌های Interactive Tech & Games، Cyber-security & Data Intelligence",
    "https://www.sdu.dk/en/uddannelse/kandidat/softwareengineering")
add("دانمارک", "University of Southern Denmark (SDU)", "Odense", "MSc Artificial Intelligence", "AI", "۲ سال", "€17,300", ("EUR", 17300, None),
    "کارشناسی CS/AI", "6.5", "=283", "Target", "شروع سپتامبر و فوریه",
    "https://www.sdu.dk/en/studyscience")
add("دانمارک", "University of Southern Denmark (SDU)", "Odense", "MSc Eng Robot Systems", "EMB", "۲ سال", "€17,300", ("EUR", 17300, None),
    "کارشناسی مرتبط (CS/EE/Mechatronics)", "6.5", "=283", "Target", "Odense Robotics cluster (Universal Robots، MiR)",
    "https://www.sdu.dk/en/uddannelse/kandidat/alle-kandidatuddannelser")
add("دانمارک", "University of Southern Denmark (SDU)", "Kolding", "MSc Data Science", "DS", "۲ سال", "€17,300", ("EUR", 17300, None),
    "کارشناسی با محتوای کمی/برنامه‌نویسی", "6.5", "=283", "Target", "",
    "https://www.sdu.dk/en/uddannelse/kandidat/alle-kandidatuddannelser")
add("دانمارک", "IT University of Copenhagen (ITU)", "Copenhagen", "MSc Games — track Game Technology", "GD", "۲ سال", "€16,500 (€8,250 در ترم؛ ورودی ۲۰۲۶ — رسمی)", ("EUR", 16500, None),
    "برای track فنی: کارشناسی CS", "6.5", "— (تخصصی)", "Target", "شناخته‌شده‌ترین ارشد بازی اسکاندیناوی؛ Copenhagen (IO Interactive، Unity Copenhagen)",
    "https://en.itu.dk/Programmes/MSc-Programmes/Applying-to-a-MSc-programme/Non-EU-EOES")
add("دانمارک", "IT University of Copenhagen (ITU)", "Copenhagen", "MSc Computer Science", "SE", "۲ سال", "€16,500 (€8,250 در ترم)", ("EUR", 16500, None),
    "کارشناسی CS/SE با برنامه‌نویسی قابل توجه", "6.5", "— (تخصصی)", "Target", "ارزان‌تر از DTU/KU در کپنهاگ؛ رقم قدیمی €13,400 (پورتال studyindenmark) منسوخ است",
    "https://en.itu.dk/Programmes/MSc-Programmes/Applying-to-a-MSc-programme/Non-EU-EOES")
add("دانمارک", "IT University of Copenhagen (ITU)", "Copenhagen", "MSc Data Science", "DS", "۲ سال", "€16,500 (€8,250 در ترم)", ("EUR", 16500, None),
    "کارشناسی مرتبط با داده/CS", "6.5", "— (تخصصی)", "Target", "",
    "https://en.itu.dk/Programmes/MSc-Programmes/Applying-to-a-MSc-programme/Non-EU-EOES")
add("دانمارک", "Technical University of Denmark (DTU)", "Lyngby", "MSc Eng Human-Centered Artificial Intelligence", "AI", "۲ سال", "€15,000", ("EUR", 15000, None),
    "ظرفیت محدود؛ امتیازدهی: معدل ۶۰٪ + سابقهٔ کار ۱۰٪", "6.5", "105", "Reach", "معدل ۱۵.۷۷ در رقابت DTU ضعیف است",
    "https://www.dtu.dk/english/education/graduate/msc-programmes/human-centered-artificial-intelligence")
add("دانمارک", "Technical University of Denmark (DTU)", "Lyngby", "MSc Eng Autonomous Systems", "EMB", "۲ سال", "€15,000", ("EUR", 15000, None),
    "۸۰–۹۰ ECTS دروس مرتبط؛ ظرفیت محدود", "6.5", "105", "Reach", "",
    "https://www.dtu.dk/english/education/graduate/msc-programmes/autonomous-systems/prerequisites")
add("دانمارک", "Technical University of Denmark (DTU)", "Lyngby", "MSc Eng Computer Science and Engineering", "SE", "۲ سال", "€15,000", ("EUR", 15000, None),
    "ظرفیت محدود؛ گزینش با معدل", "6.5", "105", "Reach", "",
    "https://www.dtu.dk/english/education/graduate/msc-programmes/computer-science-and-engineering")
add("دانمارک", "Aarhus University (AU)", "Aarhus", "MSc Computer Science", "SE", "۲ سال", "€17,300", ("EUR", 17300, None),
    "کارشناسی CS با واحدهای مشخص", "6.5", "128", "Target/Reach", "Aarhus: دومین شهر، ارزان‌تر از کپنهاگ",
    "https://masters.au.dk/computerscience")

PROGRAMS = P


def fee_usd(cur, lo, hi):
    """Annual tuition in USD, rounded to the nearest $100."""
    r = RATES[cur]
    def f(x):
        return int(round(x * r / 100.0)) * 100
    if hi is None:
        return f"${f(lo):,}"
    return f"${f(lo):,}–{f(hi):,}"
