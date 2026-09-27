# -*- coding: utf-8 -*-
"""
Data for the two extra sheets of Table_final.xlsx:
  «برنامه‌ها»           — one row per English-taught master's programme (all 6 countries, 8 fields)
  «حوزه‌ها و بازار کار» — the 8 computing fields, their 2026 job market and fit with Shayan's profile
Figures checked on 2026-09-27 against the programme/fee pages listed in the source column.
"""

# ---- FX (same as main table) ------------------------------------------------
RATES = {"EUR": 1.14, "GBP": 1.325, "SEK": 1 / 9.9, "DKK": 1 / 6.55}

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
     "خوب: پیش‌زمینهٔ Computer Engineering + Python؛ ولی برای برنامه‌های Reach (Tübingen، UvA، KTH، Sheffield) معدل ۱۵.۷۷ کافی نیست — برنامه‌های کاربردی (Passau AI Eng، FAU، Northumbria/Teesside AI، UL AI&ML، Umeå) هدف بگیرید",
     "رقابت ورودی شدید؛ بخشی از آگهی‌ها «AI» در عنوان دارند ولی کار مهندسی نرم‌افزار معمولی است؛ مدرک به‌تنهایی بدون پورتفولیو/پروژه کافی نیست",
     "LinkedIn/WEF ژانویه ۲۰۲۶ (۱.۳ میلیون شغل جدید AI؛ AI Engineer سریع‌ترین‌رشد)؛ Bitkom 2025"],
    ["مهندسی نرم‌افزار / علوم کامپیوتر", "۴ — بیشترین حجم",
     "مرجع (آلمان €48–55k · هلند €40–50k · سوئد SEK 420–540k · دانمارک DKK 500–540k · ایرلند €35–45k · انگلستان £28–35k)",
     "بسیار خوب",
     "بهترین تناسب با سابقهٔ شما (۲ سال IT + Unity/C#)؛ پذیرش ساده‌تر (2:2)؛ در همهٔ کشورها گزینهٔ Safe دارد",
     "آگهی‌های جونیور از ۲۰۲۳ کم شده (اثر GenAI)؛ در بریتانیا ۶–۷٪ بیکاری فارغ‌التحصیلان CS — سابقهٔ کار واقعی شما را از این گروه جدا می‌کند",
     "Bitkom 2025 (۱۰۹ هزار جای خالی IT در آلمان، ۷.۷ ماه زمان پرکردن)؛ IW 2024 (آگهی‌ها ۲۶٪ کمتر از ۲۰۲۳)"],
    ["امنیت سایبری", "۴ — کمبود ساختاری",
     "مساوی تا کمی بالاتر؛ در انگلستان (NCSC-certified) و ایرلند (مراکز امنیت شرکت‌های آمریکایی) خوب",
     "خوب — ولی مشاغل دولتی/دفاعی معمولاً به تابعیت یا اقامت بلندمدت نیاز دارند",
     "خوب: MSc Cyber با 2:2 در Teesside/Northumbria/MMU/Kent/Royal Holloway/TU Dublin؛ Saarland (رایگان ولی IELTS 7)؛ AAU کپنهاگ",
     "عدد «۴.۸ میلیون کمبود» ISC2 در گزارش ۲۰۲۵ حذف شد (نیاز اعلام‌شده بود نه آگهی واقعی)؛ کمبود بودجه دلیل اول جای خالی؛ ۳۱٪ تیم‌ها صفر جونیور دارند → برای اولین شغل، کارآموزی + گواهی (Security+، AZ-500) لازم است",
     "ISC2 Workforce Study 2024/2025؛ Kent/Surrey NCSC certification"],
    ["ابری / سیستم‌های توزیع‌شده / DevOps", "۴ — پایدار",
     "بالاتر از توسعه‌دهندهٔ عمومی (+۵ تا +۱۵٪)؛ DevOps/SRE در دانمارک و سوئد پرتقاضا",
     "بسیار خوب",
     "خوب: Leicester Cloud Computing، TU Darmstadt DSS، KTH SEDS، DCU Cloud major؛ گواهی AWS/Azure کنار مدرک",
     "کمتر «مدرک‌محور» است؛ برنامه‌های خالص Cloud کم‌اند — معمولاً گرایشِ CS/SE است",
     "tribexyz 2026 (Data/Cloud Engineer پرجست‌وجوترین در UK/DE)؛ آگهی‌های شرکت‌ها"],
    ["علم داده / تحلیل داده", "۳ — جونیور اشباع",
     "مساوی CS در سطح جونیور؛ بالاتر بعد از ۲–۳ سال",
     "بسیار خوب",
     "متوسط: مدرک‌های ارزان و Safe زیاد است (Maynooth €17k، Skövde، Brunel، ITU) ولی رقابت جونیور بالاست؛ اگر می‌روید، Data Engineering را انتخاب کنید",
     "تعداد فارغ‌التحصیل خیلی بیشتر از جای خالی جونیور؛ آگهی جونیور Data Engineering هم ↓۶۷٪؛ مسیر رایج: تحلیلگر/بک‌اند → مهندس داده",
     "research.com 2026؛ careery.pro 2026؛ datadriven.io 2026"],
    ["سیستم‌های نهفته / رباتیک / خودران", "۴ در آلمان/سوئد؛ ۳ در بقیه",
     "مساوی تا کمی بالاتر در صنعت (Bosch، Continental، ABB، Volvo)؛ پایین‌تر در بریتانیا/ایرلند",
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

# ---- programmes ---------------------------------------------------------------
# country, university (city), programme, field key, duration, fee text (local), (cur, annual amount low, high or None),
# entry requirement, IELTS, QS 2027, tier for GPA 15.77/20, note, source URL
P = []

def add(*a):
    P.append(a)

# ===== انگلستان (GBP) =====
add("انگلستان", "Teesside (Middlesbrough)", "MSc Computer Science", "SE", "۱ سال", "£17,000", ("GBP", 17000, None),
    "2:2 در رشتهٔ مرتبط", "6.0", "— (THE 601–800)", "Safe", "ارزان‌ترین گزینهٔ معتبر انگلستان؛ Middlesbrough ارزان ولی بازار کار محلی کوچک",
    "https://www.tees.ac.uk/postgraduate_courses/computing_&_cyber_security/msc_computer_science.cfm")
add("انگلستان", "Teesside (Middlesbrough)", "MSc Artificial Intelligence", "AI", "۱ سال", "£17,000", ("GBP", 17000, None),
    "2:2 در رشتهٔ مرتبط", "6.0", "—", "Safe", "همان باند شهریهٔ Teesside",
    "https://www.tees.ac.uk/postgraduate_courses/computing_&_cyber_security/msc_artificial_intelligence.cfm")
add("انگلستان", "Teesside (Middlesbrough)", "MSc Cyber Security (BCS accredited)", "CY", "۱ سال", "£17,000", ("GBP", 17000, None),
    "2:2 در رشتهٔ مرتبط", "6.0", "—", "Safe", "اعتبار BCS؛ بدون NCSC",
    "https://www.tees.ac.uk/postgraduate_courses/computing_&_cyber_security/msc_cyber_security.cfm")
add("انگلستان", "Northumbria (Newcastle)", "MSc Advanced Computer Science", "SE", "۱ سال", "£21,500", ("GBP", 21500, None),
    "2:2 در رشتهٔ کامپیوتری", "6.5", "=528", "Safe", "Newcastle: شهر دانشجویی ارزان با بازار فناوری متوسط",
    "https://www.northumbria.ac.uk/study-at-northumbria/courses/msc-advanced-computer-science-dtfava6/")
add("انگلستان", "Northumbria (Newcastle)", "MSc Artificial Intelligence", "AI", "۱ سال", "£21,500", ("GBP", 21500, None),
    "2:2 در رشتهٔ کامپیوتری/ریاضی", "6.5", "=528", "Safe", "شهریهٔ رسمی 2026/27",
    "https://www.northumbria.ac.uk/study-at-northumbria/courses/msc-artificial-intelligence-dtfari6/")
add("انگلستان", "Nottingham Trent (Nottingham)", "MSc Artificial Intelligence", "AI", "۱ سال", "≈ £19,900", ("GBP", 19900, None),
    "2:2 (≈ ۵۵٪)", "6.5", "=639", "Safe", "رقم از دو مرجع ثانویه؛ صفحهٔ رسمی 2026/27 را قبل از اقدام چک کنید",
    "https://www.ntu.ac.uk/study-and-courses/courses")
add("انگلستان", "Nottingham Trent (Nottingham)", "MSc Cyber Security", "CY", "۱ سال", "≈ £19,900", ("GBP", 19900, None),
    "2:2", "6.5", "=639", "Safe", "همان باند NTU (≈)",
    "https://www.ntu.ac.uk/study-and-courses/courses")
add("انگلستان", "Manchester Metropolitan (Manchester)", "MSc Cyber Security", "CY", "۱ سال", "£21,000", ("GBP", 21000, None),
    "2:2 در رشتهٔ کامپیوتری", "6.5", "≈ 600–650", "Safe", "Manchester دومین قطب فناوری انگلستان؛ شهریهٔ رسمی overseas 2026/27",
    "https://www.mmu.ac.uk/study/postgraduate/course/msc-cyber-security")
add("انگلستان", "Essex (Colchester)", "MSc Advanced Computer Science", "SE", "۱ سال", "£24,675", ("GBP", 24675, None),
    "2:2؛ Computer Engineering پذیرفته می‌شود", "6.0", "=438", "Safe/Target", "۵۰ دقیقه تا لندن؛ دانشکدهٔ CSEE قوی در AI",
    "https://www.essex.ac.uk/courses/pg00435/1/msc-advanced-computer-science")
add("انگلستان", "Essex (Colchester)", "MSc Artificial Intelligence", "AI", "۱ سال", "£24,675", ("GBP", 24675, None),
    "2:2 در رشتهٔ کامپیوتری/ریاضی", "6.0", "=438", "Safe/Target", "ورودی اکتبر ۲۰۲۶ تأیید شده",
    "https://www.essex.ac.uk/courses/pg00457/1/msc-artificial-intelligence")
add("انگلستان", "Leicester", "MSc Advanced Computer Science", "SE", "۱ سال", "£24,250", ("GBP", 24250, None),
    "2:1 (سابقهٔ کار مرتبط جبران می‌کند)", "6.5", "=314", "Target", "رتبهٔ بهتر با شهریهٔ نزدیک Essex",
    "https://le.ac.uk/courses/advanced-computer-science-msc/2026")
add("انگلستان", "Leicester", "MSc Artificial Intelligence", "AI", "۱ سال", "£24,250", ("GBP", 24250, None),
    "2:1", "6.5", "=314", "Target", "",
    "https://le.ac.uk/courses/artificial-intelligence-msc/2026")
add("انگلستان", "Leicester", "MSc Cloud Computing", "CLOUD", "۱ سال", "£24,250", ("GBP", 24250, None),
    "2:1", "6.5", "=314", "Target", "یکی از معدود ارشدهای خالص Cloud در انگلستان",
    "https://le.ac.uk/courses/cloud-computing-msc/2026")
add("انگلستان", "Brunel (London)", "MSc Artificial Intelligence", "AI", "۱ سال", "£24,795", ("GBP", 24795, None),
    "2:2", "6.5", "353", "Safe/Target", "لندن = بازار کار بزرگ ولی زندگی £1,400–1,800/ماه؛ بورس تا £6,000 تضمینی نیست",
    "https://www.brunel.ac.uk/study/courses/artificial-intelligence-msc")
add("انگلستان", "Brunel (London)", "MSc Data Science and Analytics", "DS", "۱ سال", "£24,795", ("GBP", 24795, None),
    "2:2", "6.5", "353", "Safe/Target", "",
    "https://www.brunel.ac.uk/study/courses/data-science-and-analytics-msc")
add("انگلستان", "Kent (Canterbury)", "MSc Cyber Security (NCSC fully certified + BCS)", "CY", "۱ سال", "≈ £23,500", ("GBP", 23500, None),
    "«good 2:2»", "6.5", "415", "Target", "گواهی کامل NCSC = معتبرترین برچسب امنیت در بریتانیا؛ رقم شهریه از مرجع ثانویه",
    "https://www.kent.ac.uk/courses/postgraduate/1225/cyber-security")
add("انگلستان", "Royal Holloway (Egham، حومهٔ لندن)", "MSc Information and Cyber Security", "CY", "۱ سال", "£25,500", ("GBP", 25500, None),
    "2:2", "6.5", "=485", "Target", "قدیمی‌ترین گروه امنیت اطلاعات بریتانیا (ISG)؛ NCSC certified",
    "https://www.royalholloway.ac.uk/studying-here/postgraduate/information-security/information-and-cyber-security/")
add("انگلستان", "Goldsmiths (London)", "MSc Computer Games Programming", "GD", "۱ سال", "£22,000", ("GBP", 22000, None),
    "مدرک second-class در رشتهٔ برنامه‌نویسی", "6.5 (6.0)", "≈ 800–1000", "Safe/Target", "پورتفولیوی Unity/C# شما اینجا مستقیماً به کار می‌آید؛ بازار بازی ۲۰۲۲–۲۵ ضعیف",
    "https://www.gold.ac.uk/pg/msc-computer-games-programming/")
add("انگلستان", "Surrey (Guildford)", "MSc Artificial Intelligence", "AI", "۱ سال", "≈ £26,900–27,500", ("GBP", 26900, 27500),
    "2:2", "6.5", "=246", "Target", "Guildford قطب بازی‌سازی و امنیت بریتانیا (نزدیک لندن)؛ رقم 2025/26 + برآورد 2026/27",
    "https://www.surrey.ac.uk/postgraduate/artificial-intelligence-msc")
add("انگلستان", "Surrey (Guildford)", "MSc Cyber Security (NCSC)", "CY", "۱ سال", "£25,900", ("GBP", 25900, None),
    "2:2", "6.5 (W 6.0)", "=246", "Target", "",
    "https://www.surrey.ac.uk/postgraduate/cyber-security-msc")
add("انگلستان", "York", "MSc Advanced Computer Science", "SE", "۱ سال", "£32,900", ("GBP", 32900, None),
    "2:2 با پیش‌زمینهٔ قوی", "6.5", "=158", "Target/Reach", "Russell Group؛ گران",
    "https://www.york.ac.uk/study/postgraduate-taught/courses/msc-advanced-computer-science/")
add("انگلستان", "York", "MSc Human-Centred Interactive Technologies", "HCI", "۱ سال", "£32,900", ("GBP", 32900, None),
    "2:2", "6.5", "=158", "Target", "بهترین برنامهٔ HCI انگلستان برای معدل شما؛ ولی بازار UX ضعیف",
    "https://www.york.ac.uk/study/postgraduate-taught/courses/msc-human-centred-interactive-technologies/")
add("انگلستان", "Newcastle", "MSc Computer Game Engineering", "GD", "۱ سال", "£32,300", ("GBP", 32300, None),
    "2:1 (2:2 با سابقه بررسی می‌شود)", "6.5", "149", "Reach", "معتبرترین ارشد مهندسی بازی انگلستان؛ گران",
    "https://www.ncl.ac.uk/postgraduate/")
add("انگلستان", "Lancaster", "MSc Cyber Security", "CY", "۱ سال", "£30,000 (بورس خودکار £4,500 با 2:1)", ("GBP", 30000, None),
    "2:1", "6.5", "164", "Reach", "NCSC-certified؛ شرط 2:1 برای معدل شما سخت است",
    "https://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/cyber-security-msc/2026/")
add("انگلستان", "Sheffield", "MSc Artificial Intelligence", "AI", "۱ سال", "£34,340", ("GBP", 34340, None),
    "2:1", "6.5", "82", "Reach", "رتبهٔ بالا، شهریه و شرط ورود بالا",
    "https://www.sheffield.ac.uk/postgraduate/taught/courses")

# ===== ایرلند (EUR) =====
add("ایرلند", "TU Dublin (Blanchardstown)", "MSc Computing in Applied Cyber Security", "CY", "۱ سال (حضوری + آنلاین)", "€14,500 (کل دوره)", ("EUR", 14500, None),
    "2:2 (GPA 2.5) در Computing", "6.5 (6.0)", "791–800", "Safe", "ارزان‌ترین ارشد امنیت ایرلند در یک دانشگاه دولتی",
    "https://www.tudublin.ie/study/postgraduate/courses/applied-cyber-security/")
add("ایرلند", "TU Dublin (Grangegorman)", "MSc Computer Science (Data Science)", "DS", "۱–۱.۵ سال", "€21,750 (کل دوره)", ("EUR", 21750, None),
    "2:1، یا 2:2 + ۲ سال سابقهٔ توسعهٔ نرم‌افزار", "6.5 (6.0)", "791–800", "Target", "۲ سال سابقهٔ کار شما اینجا شرط ورود را جبران می‌کند",
    "https://www.tudublin.ie/study/postgraduate/courses/computing-data-science/")
add("ایرلند", "TU Dublin (Grangegorman)", "MSc Computing (Advanced Software Development)", "SE", "۱ سال", "≈ €15,000–15,500", ("EUR", 15000, 15500),
    "2:2", "6.5", "791–800", "Safe", "گزینهٔ Safe جدول اصلی",
    "https://www.tudublin.ie/study/postgraduate/")
add("ایرلند", "Maynooth", "MSc Data Science and Analytics (۱۲ ماهه، conversion)", "DS", "۱ سال", "≈ €17,000", ("EUR", 17000, None),
    "مدرک Level 8 با محتوای ریاضی", "6.5", "721–730", "Safe", "ورود آسان؛ ولی حوزهٔ اشباع جونیور",
    "https://www.maynoothuniversity.ie/study-maynooth/postgraduate-studies/courses/msc-data-science-and-analytics")
add("ایرلند", "Maynooth", "MSc (Computer Science) Software Engineering", "SE", "۱ سال", "€18,000 (2025/26) → ≈ €18,500", ("EUR", 18500, None),
    "2:2", "6.5", "721–730", "Safe/Target", "۲۵ دقیقه تا Dublin با قطار؛ اجاره کمتر از Dublin",
    "https://www.maynoothuniversity.ie/study-maynooth/postgraduate-studies")
add("ایرلند", "University of Limerick", "MSc Artificial Intelligence and Machine Learning", "AI", "۱ سال", "€20,800", ("EUR", 20800, None),
    "first یا second class honours در CS/Computer Engineering", "6.5", "388", "Target", "شهریهٔ رسمی 2026/27؛ Limerick ارزان‌تر از Dublin",
    "https://www.ul.ie/study/postgraduate/artificial-intelligence-and-machine-learning-msc")
add("ایرلند", "University of Limerick", "MSc Software Engineering", "SE", "۱ سال", "€20,800", ("EUR", 20800, None),
    "2:2", "6.5", "388", "Target", "گزینهٔ Target جدول اصلی",
    "https://www.ul.ie/study/postgraduate")
add("ایرلند", "Munster TU – MTU (Cork)", "MSc Cybersecurity", "CY", "۱ سال", "≈ €12,000–15,000", ("EUR", 12000, 15000),
    "مدرک Level 8 honours در Computing", "6.0", "—", "Safe", "Cork: مقر اروپایی Apple و ده‌ها شرکت امنیت؛ رقم از مراجع ثانویه",
    "https://www.mtu.ie/courses/")
add("ایرلند", "Munster TU – MTU (Cork)", "MSc Artificial Intelligence", "AI", "۱ سال", "≈ €15,000", ("EUR", 15000, None),
    "Level 8 honours در CS/Eng + ریاضی و کدنویسی قوی", "6.5", "—", "Safe/Target", "",
    "https://www.mtu.ie/courses/")
add("ایرلند", "Dublin City University (Dublin)", "MSc in Computing — Majors: AI with NLP / Data Analytics / Secure Software Engineering / Cloud Computing", "MULTI", "۱ سال", "€25,000 (−€5,000 بورس دانشکده برای غیر-EU ⇒ €20,000)", ("EUR", 20000, 25000),
    "2:1 در CS/Computing", "6.5", "408", "Target/Reach", "شرط 2:1؛ ورودی ژانویه ۲۰۲۷ هم دارد",
    "https://www.dcu.ie/courses/postgraduate/school-computing/msc-computing-major-options")
add("ایرلند", "University of Galway", "MSc Computer Science (Artificial Intelligence)", "AI", "۱ سال", "€28,000", ("EUR", 28000, None),
    "First Class (یا 2:1 خوب با تأیید مدیر برنامه)", "6.5", "275", "Reach", "شرط ورود بالا؛ گران",
    "http://cs.universityofgalway.ie/")
add("ایرلند", "University College Cork (Cork)", "MSc Data Science and Artificial Intelligence", "DS", "۱ سال", "€28,000", ("EUR", 28000, None),
    "2:1 در CS/ریاضی", "6.5", "220", "Reach", "UCD (QS 100) و TCD (QS 75) هم ≈ €30k و 2:1 → برای معدل شما Reach",
    "https://www.ucc.ie/en/study/postgrad/")

# ===== آلمان (EUR) =====
add("آلمان", "Universität Stuttgart", "M.Sc. Computer Science (انگلیسی، بدون NC)", "SE", "۲ سال", "€1,500 در ترم + ≈ €200 سهم ترم = ≈ €3,400/سال", ("EUR", 3400, None),
    "کارشناسی CS/مرتبط؛ بدون NC", "7.0 (C1)", "318", "Target", "شهریهٔ بادن-وورتمبرگ برای غیر-EU",
    "https://www.uni-stuttgart.de/en/study/study-programs/")
add("آلمان", "Universität Stuttgart", "M.Sc. Information Technology (INFOTECH)", "EMB", "۲ سال", "€1,500 در ترم + سهم ترم ≈ €3,400/سال", ("EUR", 3400, None),
    "کارشناسی EE/CS/Computer Engineering؛ گزینش", "7.0 (C1)", "318", "Target", "گرایش‌های Embedded/Communication؛ Bosch و Daimler همان شهر",
    "https://www.mygermanuniversity.com/master/information-technology-infotech/678")
add("آلمان", "FAU Erlangen-Nürnberg", "M.Sc. Artificial Intelligence", "AI", "۲ سال", "€0 + ≈ €130 سهم ترم (≈ €260/سال)", ("EUR", 260, None),
    "کارشناسی CS/مرتبط؛ بررسی ریزنمرات", "B2 (IELTS 6.0)", "218", "Target", "Siemens/adidas/Schaeffler در منطقه",
    "https://www.fau.eu/degree-program/artificial-intelligence-m-sc/")
add("آلمان", "FAU Erlangen-Nürnberg", "M.Sc. Autonomy Technologies", "EMB", "۲ سال", "€0 + ≈ €130 سهم ترم", ("EUR", 260, None),
    "کارشناسی مرتبط؛ آلمانی لازم نیست", "B2 (IELTS 6.0)", "218", "Target", "رباتیک/خودران؛ صفحهٔ رسمی سپتامبر ۲۰۲۶",
    "https://www.fau.eu/degree-program/autonomy-technologies-m-sc/")
add("آلمان", "TU Darmstadt", "M.Sc. Distributed Software Systems (انگلیسی)", "CLOUD", "۲ سال", "€0 + ≈ €300 سهم ترم (≈ €600/سال)", ("EUR", 600, None),
    "کارشناسی CS با پیش‌نیازهای مشخص", "≈ 7.0 (C1) — چک شود", "250", "Target/Reach", "منطقهٔ Rhein-Main (SAP، Deutsche Bank، Software AG)",
    "https://www.tu-darmstadt.de/studieren/")
add("آلمان", "TU Dresden", "M.Sc. Computer Science (انگلیسی)", "SE", "۲ سال", "€0 + ≈ €300 سهم ترم", ("EUR", 600, None),
    "کارشناسی CS؛ ارزیابی استعداد", "7.0", "185", "Reach", "Dresden ارزان‌ترین شهر جدول؛ GlobalFoundries/Infineon/Bosch",
    "https://tu-dresden.de/studium/vor-dem-studium/studienangebot")
add("آلمان", "Saarland University (Saarbrücken)", "M.Sc. Cybersecurity", "CY", "۲ سال", "€0 + ≈ €394 سهم ترم (≈ €790/سال)", ("EUR", 790, None),
    "کارشناسی CS + اثبات دروس پایه + ۲ توصیه‌نامه؛ بدون NC", "7.0 (C1؛ MOI پذیرفته نمی‌شود)", "=588 (CS ≈ 251)", "Target", "CISPA — بهترین مرکز امنیت آلمان؛ IELTS 7 شرط سخت شماست",
    "https://www.uni-saarland.de/en/study/programmes/master/cybersecurity.html")
add("آلمان", "Saarland University (Saarbrücken)", "M.Sc. Data Science and Artificial Intelligence", "AI", "۲ سال", "€0 + ≈ €394 سهم ترم", ("EUR", 790, None),
    "کارشناسی CS/مرتبط؛ بدون NC", "7.0 (C1)", "=588 (CS ≈ 251)", "Target", "MPI Informatics و DFKI در همان کمپوس",
    "https://www.uni-saarland.de/en/study/programmes/master/data-science.html")
add("آلمان", "TU Chemnitz", "M.Sc. Automotive Software Engineering", "EMB", "۲ سال", "€0 + ≈ €320 سهم ترم (≈ €640/سال)", ("EUR", 640, None),
    "کارشناسی CS/مرتبط؛ بدون محدودیت پذیرش", "B2 (IELTS 5.5)", "—", "Safe", "آسان‌ترین ورود؛ شهر ارزان؛ ولی صنعت خودرو ۲۰۲۴–۲۵ ضعیف و آلمانی در کارفرمایان محلی",
    "https://www.mygermanuniversity.com/master/automotive-software-engineering/91")
add("آلمان", "Universität Passau", "M.Sc. Artificial Intelligence Engineering", "AI", "۲ سال", "€0 + ≈ €100–200 سهم ترم", ("EUR", 300, None),
    "معدل آلمانی ≤ 2.7 (معدل شما ≈ 2.3 ✓)؛ ۳۵ ECTS ریاضی + ۴۰ ECTS CS", "B2؛ + آلمانی A1 تا پایان سال اول (کلاس رایگان)", "—", "Safe", "کاملاً انگلیسی؛ شهر کوچک و ارزان",
    "https://www.uni-passau.de/en/msc-ai-eng")
add("آلمان", "OVGU Magdeburg", "M.Sc. Data and Knowledge Engineering", "DS", "۲ سال", "€0 + ≈ €311 سهم ترم", ("EUR", 620, None),
    "معدل آلمانی ≤ 2.3 (معدل شما ≈ 2.27 — دقیقاً مرزی)؛ کارشناسی CS", "6.0–7.0 (منابع متناقض؛ رسمی را چک کنید)", "—", "Safe/Target", "",
    "https://www.dke.ovgu.de/")
add("آلمان", "TH Köln – Cologne Game Lab", "M.A. Game Development and Research", "GD", "۲ سال", "€2,500 در ترم (غیر-EU) + €277 سهم ترم ≈ €5,550/سال", ("EUR", 5550, None),
    "هر کارشناسی + ≥ ۱۲ ماه سابقهٔ مرتبط + آزمون استعداد (مهلت ۳۱ مارس)", "B2", "— (UAS)", "Target", "معتبرترین مدرسهٔ بازی آلمان؛ ۷ ماه Unity + ۲ سال IT شما احتمالاً شرط ۱۲ ماه را می‌پوشاند — بپرسید",
    "https://colognegamelab.de/study-programs/post-graduate-programs/game-development-research-ma/faqs/")
add("آلمان", "Universität Siegen", "M.Sc. Human Computer Interaction", "HCI", "۲ سال", "€0 + ≈ €372 سهم ترم", ("EUR", 745, None),
    "معدل آلمانی ≤ 2.5؛ کارشناسی CS/IS/Design/Psychology", "6.5", "—", "Safe", "شروع زمستان و تابستان؛ شهر کوچک",
    "https://www2.daad.de/deutschland/studienangebote/international-programmes/en/detail/4686/")
add("آلمان", "Hochschule Bonn-Rhein-Sieg (Sankt Augustin)", "M.Sc. Autonomous Systems", "EMB", "۲ سال", "€0 + €349 سهم ترم", ("EUR", 700, None),
    "معدل آلمانی ≤ 2.5؛ ۲۵ جای محدود؛ آزمون استعداد؛ uni-assist", "6.5 (B2+)", "— (UAS)", "Target", "رباتیک کاربردی با Fraunhofer؛ نزدیک Bonn/Köln",
    "https://www.h-brs.de/en/inf/admission-application-master-autonomous-systems")
add("آلمان", "RWTH Aachen", "M.Sc. Software Systems Engineering", "SE", "۲ سال", "€0 + ≈ €330 سهم ترم", ("EUR", 660, None),
    "کارشناسی CS، معدل ≥ ۶۵٪ (شما ۷۹٪ ✓)؛ ۲ درس پیشرفتهٔ سیستم؛ مهلت ۱ مارس", "B2 (IELTS 5.5)", "104", "Reach", "TU9؛ رقابتی — معدل شما حداقل را رد می‌کند ولی متقاضیان قوی‌ترند",
    "https://sc.informatik.rwth-aachen.de/en/studium/master/sse/")
add("آلمان", "Universität Tübingen", "M.Sc. Machine Learning", "AI", "۲ سال", "€1,500 در ترم + ≈ €200 = ≈ €3,400/سال", ("EUR", 3400, None),
    "کارشناسی CS/ریاضی؛ آزمون توانایی؛ مهلت ۳۰ آوریل", "7.0", "=230", "Reach", "Cyber Valley — بهترین ML آلمان؛ پذیرش بسیار سخت",
    "https://uni-tuebingen.de/fakultaeten/mathematisch-naturwissenschaftliche-fakultaet/fachbereiche/informatik/studium/studierende/lehre-studienorganisation/studiengaenge/machine-learning/admission-and-application/")
add("آلمان", "TU München (Garching)", "M.Sc. Informatics", "SE", "۲ سال", "€6,000 در ترم برای غیر-EU (€12,000/سال) + €97", ("EUR", 12200, None),
    "کارشناسی CS؛ ارزیابی استعداد؛ بسیار رقابتی", "6.5", "≈ 25", "Reach", "⚠️ TUM از ۲۰۲۴ شهریهٔ غیر-EU می‌گیرد — دیگر «رایگان» نیست؛ Munich گران‌ترین شهر آلمان",
    "https://www.tum.de/en/studies/degree-programs/detail/informatics-master-of-science-msc")

# ===== هلند (EUR) =====
add("هلند", "University of Twente (Enschede)", "MSc Computer Science (گرایش‌ها: Cyber Security، Data Science، Software Tech، ...)", "SE", "۲ سال", "€21,700", ("EUR", 21700, None),
    "حداقل رسمی برای مدرک ایرانی ۱۵/۲۰", "6.5", "223", "Target", "گزینهٔ Target جدول اصلی",
    "https://www.utwente.nl/en/education/master/programmes/computer-science/")
add("هلند", "University of Twente (Enschede)", "MSc Embedded Systems", "EMB", "۲ سال", "€21,700", ("EUR", 21700, None),
    "CGPA ≥ ۷۰–۷۵٪؛ کارشناسی CS/EE/Computer Eng", "6.5", "223", "Target", "شهریهٔ رسمی 2026/27؛ مهلت غیر-EU ۱ مه",
    "https://www.utwente.nl/en/education/master/programmes/embedded-systems/finance/")
add("هلند", "University of Twente (Enschede)", "MSc Interaction Technology", "HCI", "۲ سال", "€21,700", ("EUR", 21700, None),
    "کارشناسی CS/مرتبط", "6.5", "223", "Target", "HCI فنی (نه طراحی صرف)",
    "https://www.utwente.nl/en/education/master/programmes/interaction-technology/")
add("هلند", "Radboud (Nijmegen)", "MSc Computing Science (گرایش‌ها: Cyber Security، Data Science، Software Science)", "SE", "۲ سال", "€19,714 (2025/26) → ≈ €20,500", ("EUR", 20500, None),
    "کارشناسی CS با ریاضی/الگوریتم کافی", "6.5", "283", "Target", "گزینهٔ Target جدول اصلی",
    "https://www.ru.nl/en/education/masters/computing-science")
add("هلند", "Radboud (Nijmegen)", "MSc Artificial Intelligence", "AI", "۲ سال", "€19,714 (2025/26) → ≈ €20,500", ("EUR", 20500, None),
    "کارشناسی CS/AI/مرتبط", "6.5", "283", "Target", "AI شناختی (Donders Institute)",
    "https://www.ru.nl/en/education/masters/artificial-intelligence")
add("هلند", "Leiden", "MSc Computer Science (گرایش‌ها: Artificial Intelligence، Data Science، ...)", "MULTI", "۲ سال", "€22,500", ("EUR", 22500, None),
    "کارشناسی CS", "6.5", "119", "Target/Reach", "شهریهٔ رسمی 2026/27؛ نزدیک Den Haag/Amsterdam",
    "https://www.universiteitleiden.nl/en/education/study-programmes/master/computer-science/artificial-intelligence/admission-and-application/tuition-fees")
add("هلند", "Groningen", "MSc Artificial Intelligence", "AI", "۲ سال", "€24,900", ("EUR", 24900, None),
    "کارشناسی AI/CS با ریاضی", "6.5", "157", "Target/Reach", "شهریهٔ رسمی 2026/27؛ بورس ASML €5k",
    "https://www.rug.nl/masters/artificial-intelligence/?lang=en")
add("هلند", "Groningen", "MSc Computing Science", "SE", "۲ سال", "≈ €21,400 (2025) → ≈ €22,500", ("EUR", 22500, None),
    "کارشناسی CS", "6.5", "157", "Target", "",
    "https://www.rug.nl/masters/computing-science/?lang=en")
add("هلند", "Utrecht", "MSc Game and Media Technology", "GD", "۲ سال", "€25,306", ("EUR", 25306, None),
    "کارشناسی CS؛ ارشد پژوهشی گزینشی", "6.5", "113", "Reach", "تنها ارشد پژوهشی بازی هلند؛ Utrecht قطب استودیوهای بازی",
    "https://www.uu.nl/en/masters/game-and-media-technology")
add("هلند", "Utrecht", "MSc Artificial Intelligence", "AI", "۲ سال", "€25,306", ("EUR", 25306, None),
    "کارشناسی CS/AI؛ گزینشی", "6.5", "113", "Reach", "همان باند شهریهٔ Utrecht 2026/27",
    "https://www.uu.nl/en/masters/artificial-intelligence")
add("هلند", "Universiteit van Amsterdam (UvA)", "MSc Software Engineering (۱ ساله!)", "SE", "۱ سال", "≈ €23,540", ("EUR", 23540, None),
    "کارشناسی CS", "6.5", "60", "Target/Reach", "تنها ارشد ۱ سالهٔ معتبر هلند → کل هزینه نصف؛ اما اجارهٔ Amsterdam €900–1,300",
    "https://www.uva.nl/en/programmes/masters/software-engineering/software-engineering.html")
add("هلند", "Universiteit van Amsterdam (UvA)", "MSc Artificial Intelligence", "AI", "۲ سال", "≈ €26,000", ("EUR", 26000, None),
    "کارشناسی AI/CS با ریاضی قوی؛ بسیار رقابتی", "6.5", "60", "Reach", "",
    "https://www.uva.nl/en/programmes/masters/artificial-intelligence/artificial-intelligence.html")
add("هلند", "TU Eindhoven", "MSc Data Science and Artificial Intelligence", "DS", "۲ سال", "€21,700", ("EUR", 21700, None),
    "کارشناسی CS/ریاضی؛ گزینش بر اساس معدل", "6.5", "152", "Reach", "Brainport (ASML، Philips، NXP)",
    "https://www.tue.nl/en/education/graduate-school/master-data-science-and-artificial-intelligence")
add("هلند", "TU Eindhoven", "MSc Embedded Systems", "EMB", "۲ سال", "€21,700", ("EUR", 21700, None),
    "کارشناسی CS/EE؛ گزینش", "6.5", "152", "Reach", "ASML/NXP بزرگ‌ترین کارفرمایان Embedded اروپا",
    "https://www.tue.nl/en/education/graduate-school/master-embedded-systems")
add("هلند", "TU Delft", "MSc Computer Science / MSc Computer & Embedded Systems Engineering", "SE", "۲ سال", "€22,290 (2025/26) → ≈ €23,000", ("EUR", 23000, None),
    "معدل ≥ ۷۵٪ / ۲۰٪ برتر", "7.0", "48", "Reach", "معتبرترین، ولی برای معدل ۱۵.۷۷ دور از دسترس",
    "https://www.tudelft.nl/onderwijs/opleidingen/masters/cs/msc-computer-science")
add("هلند", "Breda University of Applied Sciences (BUas)", "Master Game Technology (۱ ساله)", "GD", "۱ سال", "≈ €15,200", ("EUR", 15200, None),
    "کارشناسی IT/برنامه‌نویسی/بازی + پیشنهاد پروژه", "6.0", "— (UAS)", "Safe/Target", "برنامهٔ بازی BUas در اروپا شناخته‌شده است؛ مدرک UAS (نه پژوهشی)",
    "https://www.topuniversities.com/universities/breda-university-applied-sciences/postgrad/master-game-technology")

# ===== سوئد (SEK) =====
add("سوئد", "Linköping (LiU)", "MSc Computer Science", "SE", "۲ سال", "SEK 166,000", ("SEK", 166000, None),
    "گزینش بر اساس گروه معدل", "6.5", "308", "Target", "گزینهٔ Target جدول اصلی",
    "https://liu.se/en/education/program/6mics")
add("سوئد", "Linköping (LiU)", "MSc Statistics and Machine Learning", "AI", "۲ سال", "≈ SEK 166,000 (همان باند)", ("SEK", 166000, None),
    "کارشناسی با ≥ ۳۰ واحد ریاضی/آمار + برنامه‌نویسی", "6.5", "308", "Target", "",
    "https://liu.se/en/education/program/f7msl")
add("سوئد", "Halmstad", "MSc Embedded and Intelligent Systems (120 cr)", "EMB", "۲ سال", "≈ SEK 151,000", ("SEK", 151000, None),
    "کارشناسی CS/EE", "6.5", "—", "Safe", "Volvo/HMS در منطقه؛ بدون رتبهٔ QS",
    "https://www.hh.se/english/education/programmes.html")
add("سوئد", "Blekinge Tekniska Högskola – BTH (Karlskrona)", "MSc Software Engineering (120 cr)", "SE", "۲ سال", "SEK 140,000", ("SEK", 140000, None),
    "≥ ۹۰ واحد CS/SE", "6.5", "—", "Safe/Target", "Ericsson و Telenor در Karlskrona؛ ⚠️ نسخهٔ ۶۰ واحدی از راه دور است",
    "https://www.bth.se/eng/programmes/")
add("سوئد", "KTH (Stockholm)", "MSc Machine Learning", "AI", "۲ سال", "SEK 190,000", ("SEK", 190000, None),
    "کارشناسی CS/ریاضی قوی؛ بسیار رقابتی", "6.5", "82", "Reach", "Stockholm گران (اتاق SEK 7–10k)",
    "https://www.kth.se/en/studies/master/machine-learning")
add("سوئد", "KTH (Stockholm)", "MSc Cybersecurity", "CY", "۲ سال", "SEK 190,000", ("SEK", 190000, None),
    "کارشناسی CS", "6.5", "82", "Reach", "",
    "https://www.kth.se/en/studies/master/cybersecurity")
add("سوئد", "KTH (Stockholm – Kista)", "MSc Software Engineering of Distributed Systems", "CLOUD", "۲ سال", "SEK 180,000–190,000", ("SEK", 180000, 190000),
    "کارشناسی CS", "6.5", "82", "Target/Reach", "Kista = قطب ICT سوئد (Ericsson)",
    "https://www.kth.se/en/studies/master/software-engineering-of-distributed-systems")
add("سوئد", "Chalmers (Gothenburg)", "MSc Data Science and AI", "DS", "۲ سال", "SEK 160,000", ("SEK", 160000, None),
    "کارشناسی CS/ریاضی", "6.5", "174", "Target/Reach", "Volvo، Ericsson، Zenseact؛ مهلت ۱۵ ژانویه",
    "https://www.chalmers.se/en/education/find-masters-programme/data-science-and-ai-msc/")
add("سوئد", "Chalmers (Gothenburg)", "MSc Software Engineering and Technology", "SE", "۲ سال", "SEK 160,000", ("SEK", 160000, None),
    "کارشناسی CS/SE", "6.5", "174", "Target", "",
    "https://www.chalmers.se/en/education/find-masters-programme/software-engineering-and-technology-msc/")
add("سوئد", "Chalmers (Gothenburg)", "MSc Interaction Design and Technologies", "HCI", "۲ سال", "SEK 160,000", ("SEK", 160000, None),
    "کارشناسی CS/Design", "6.5", "174", "Target", "",
    "https://www.chalmers.se/en/education/find-masters-programme/interaction-design-and-technologies-msc/")
add("سوئد", "University of Gothenburg (با Chalmers)", "MSc Game Design & Technology", "GD", "۲ سال", "SEK 145,000 (کل ۲۹۰k؛ ورودی ۲۰۲۷: ۲۹۴k)", ("SEK", 145000, 147000),
    "کارشناسی CS/Design/Media", "6.5", "225", "Target", "Gothenburg: استودیوهای EA DICE/Ghost؛ بازار بازی ضعیف",
    "https://www.gu.se/en/study-gothenburg/game-design-technology-masters-programme-n2gdt")
add("سوئد", "Uppsala", "MSc Computer Science", "SE", "۲ سال", "≈ SEK 145,000–150,000", ("SEK", 145000, 150000),
    "کارشناسی CS", "6.5", "87", "Target/Reach", "رتبهٔ بالا با شهریهٔ پایین‌تر از KTH",
    "https://www.uu.se/en/study/programme/masters-programme-in-computer-science")
add("سوئد", "Umeå", "MSc Artificial Intelligence", "AI", "۲ سال", "SEK 152,300", ("SEK", 152300, None),
    "کارشناسی CS/ریاضی", "6.5", "438", "Target", "شمال سوئد، شهر دانشجویی ارزان؛ کل دوره SEK 304,600",
    "https://www.umu.se/en/education/master/masters-programme-in-artificial-intelligence/")
add("سوئد", "Skövde", "MSc Data Science (120 cr)", "DS", "۲ سال", "SEK 135,000", ("SEK", 135000, None),
    "کارشناسی CS/مرتبط", "6.5", "—", "Safe", "ارزان؛ Skövde قطب بازی سوئد (Sweden Game Arena)",
    "https://www.his.se/en/education/")
add("سوئد", "Mälardalen – MDU (Västerås)", "MSc Intelligent Embedded Systems", "EMB", "۲ سال", "≈ SEK 135,000", ("SEK", 135000, None),
    "کارشناسی CS/EE", "6.5", "—", "Safe", "ABB و Westinghouse در Västerås؛ رقم 2024/25",
    "https://www.mdu.se/en/malardalen-university/education")
add("سوئد", "Mälardalen – MDU (Västerås)", "MSc Software Engineering", "SE", "۲ سال", "≈ SEK 135,000", ("SEK", 135000, None),
    "کارشناسی CS/SE", "6.5", "—", "Safe", "",
    "https://www.mdu.se/en/malardalen-university/education")

# ===== دانمارک (EUR/DKK) =====
add("دانمارک", "Aalborg University (Aalborg)", "MSc Computer Science (IT)", "SE", "۲ سال", "€14,910 (€7,455 در ترم)", ("EUR", 14910, None),
    "کارشناسی CS/SE", "6.5", "=329", "Target", "گزینهٔ Target جدول اصلی؛ PBL (پروژه‌محور)",
    "https://www.en.aau.dk/education/master/computer-science-it")
add("دانمارک", "Aalborg University (Aalborg)", "MSc Software", "SE", "۲ سال", "€14,910", ("EUR", 14910, None),
    "کارشناسی SE/CS", "6.5", "=329", "Target", "",
    "https://www.en.aau.dk/education/master/software")
add("دانمارک", "Aalborg University (Copenhagen)", "MSc Eng Cyber Security", "CY", "۲ سال", "€14,910", ("EUR", 14910, None),
    "کارشناسی CS/EE مرتبط؛ مهلت ۱ مارس", "6.5", "=329", "Target", "کمپوس کپنهاگ: اجاره بالاتر ولی بازار کار بزرگ",
    "https://www.en.aau.dk/education/master/cyber-security/")
add("دانمارک", "Aalborg University (Aalborg / Copenhagen)", "MSc Medialogy", "HCI", "۲ سال", "€14,910", ("EUR", 14910, None),
    "کارشناسی مرتبط (Medialogy، CS، Media Tech)", "6.5", "=329", "Target", "تعامل، AR/VR، بازی؛ بین HCI و Game",
    "https://www.en.aau.dk/education/master/medialogy-aal")
add("دانمارک", "SDU (Odense)", "MSc Computer Science", "SE", "۲ سال", "€17,300 (از ورودی سپتامبر ۲۰۲۶؛ قبلاً €13,900)", ("EUR", 17300, None),
    "≥ ۱۰۰ ECTS دروس CS؛ ظرفیت محدود + آزمون", "6.5", "=283", "Target", "⚠️ افزایش شهریهٔ ۲۰۲۶ — جدول اصلی اصلاح شد",
    "https://www.sdu.dk/en/uddannelse/fees_and_funding/tuition")
add("دانمارک", "SDU (Odense)", "MSc Eng Software Engineering", "SE", "۲ سال", "€17,300", ("EUR", 17300, None),
    "کارشناسی SE/CS", "6.5", "=283", "Target", "گرایش‌های Interactive Tech & Games، Cyber-security & Data Intelligence",
    "https://www.sdu.dk/en/uddannelse/kandidat/softwareengineering")
add("دانمارک", "SDU (Odense)", "MSc Artificial Intelligence", "AI", "۲ سال", "€17,300", ("EUR", 17300, None),
    "کارشناسی CS/AI", "6.5", "=283", "Target", "شروع سپتامبر و فوریه",
    "https://www.sdu.dk/en/studyscience")
add("دانمارک", "SDU (Odense)", "MSc Eng Robot Systems", "EMB", "۲ سال", "€17,300", ("EUR", 17300, None),
    "کارشناسی مرتبط (CS/EE/Mechatronics)", "6.5", "=283", "Target", "Odense Robotics cluster (Universal Robots، MiR)",
    "https://www.sdu.dk/en/uddannelse/kandidat/alle-kandidatuddannelser")
add("دانمارک", "SDU (Kolding)", "MSc Data Science", "DS", "۲ سال", "€17,300", ("EUR", 17300, None),
    "کارشناسی با محتوای کمی/برنامه‌نویسی", "6.5", "=283", "Target", "",
    "https://www.sdu.dk/en/uddannelse/kandidat/alle-kandidatuddannelser")
add("دانمارک", "IT University of Copenhagen (ITU)", "MSc Games — track Game Technology", "GD", "۲ سال", "€13,400 (€6,700 در ترم)", ("EUR", 13400, None),
    "برای track فنی: کارشناسی CS", "6.5", "— (تخصصی)", "Target", "شناخته‌شده‌ترین ارشد بازی اسکاندیناوی؛ Copenhagen (IO Interactive، Unity Copenhagen)",
    "https://studyindenmark.dk/portal/it-university-of-copenhagen-itu/kobenhavn/games")
add("دانمارک", "IT University of Copenhagen (ITU)", "MSc Computer Science", "SE", "۲ سال", "€13,400", ("EUR", 13400, None),
    "کارشناسی CS/SE با برنامه‌نویسی قابل توجه", "6.5", "— (تخصصی)", "Target", "ارزان‌ترین شهریهٔ کپنهاگ",
    "https://studyindenmark.dk/portal/it-university-of-copenhagen-itu/kobenhavn/computer-science")
add("دانمارک", "IT University of Copenhagen (ITU)", "MSc Data Science", "DS", "۲ سال", "€13,400", ("EUR", 13400, None),
    "کارشناسی مرتبط با داده/CS", "6.5", "— (تخصصی)", "Target", "",
    "https://studyindenmark.dk/portal/it-university-of-copenhagen-itu/kobenhavn/data-science")
add("دانمارک", "DTU (Kgs. Lyngby)", "MSc Eng Human-Centered Artificial Intelligence", "AI", "۲ سال", "€15,000", ("EUR", 15000, None),
    "ظرفیت محدود؛ امتیازدهی: معدل ۶۰٪ + سابقهٔ کار ۱۰٪", "6.5", "105", "Reach", "معدل ۱۵.۷۷ در رقابت DTU ضعیف است",
    "https://www.dtu.dk/english/education/graduate/msc-programmes/human-centered-artificial-intelligence")
add("دانمارک", "DTU (Kgs. Lyngby)", "MSc Eng Autonomous Systems", "EMB", "۲ سال", "€15,000", ("EUR", 15000, None),
    "۸۰–۹۰ ECTS دروس مرتبط؛ ظرفیت محدود", "6.5", "105", "Reach", "",
    "https://www.dtu.dk/english/education/graduate/msc-programmes/autonomous-systems/prerequisites")
add("دانمارک", "DTU (Kgs. Lyngby)", "MSc Eng Computer Science and Engineering", "SE", "۲ سال", "€15,000", ("EUR", 15000, None),
    "ظرفیت محدود؛ گزینش با معدل", "6.5", "105", "Reach", "",
    "https://www.dtu.dk/english/education/graduate/msc-programmes/computer-science-and-engineering")
add("دانمارک", "Aarhus University", "MSc Computer Science", "SE", "۲ سال", "€17,300", ("EUR", 17300, None),
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
