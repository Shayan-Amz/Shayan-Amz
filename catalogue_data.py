# -*- coding: utf-8 -*-
"""
Data for the two extra sheets of Table_final.xlsx:
  «برنامه‌ها»           — one row per English-taught master's programme (all 8 countries incl. Switzerland, Finland and Canada without Quebec, 8 fields)
  «حوزه‌ها و بازار کار» — the 8 computing fields, their 2026 job market and fit with Shayan's profile
Figures checked on 2026-09-27 against the programme/fee pages listed in the source column.
"""

import re

# ---- FX (same as main table) ------------------------------------------------
RATES = {"EUR": 1.14, "GBP": 1.325, "SEK": 1 / 9.9, "DKK": 1 / 6.55, "CHF": 1.21, "CAD": 1 / 1.419, "USD": 1.0}

# ---- display currency ----------------------------------------------------------
# Every sheet is rendered in ONE currency. Source strings keep the official local
# figures; `convert()` rewrites them at build time. Change TARGET to "EUR" to get euros.
TARGET = "USD"
_SYM = {"USD": "$", "EUR": "€"}
_CUR = {"€": "EUR", "£": "GBP", "CHF": "CHF", "SEK": "SEK", "DKK": "DKK", "CAD": "CAD", "C$": "CAD", "$": "USD"}
_AMT = re.compile(r"(€|£|CHF ?|SEK ?|DKK ?|CAD ?|C\$|\$)(\d[\d,]*(?:\.\d+)?)(k?)(?:([–-])(\d[\d,]*(?:\.\d+)?)(k?))?")


def _num(t):
    return float(t.replace(",", ""))


def _round(v, dec):
    if v < 100:
        return round(v, 1) if dec else float(round(v))
    if v < 1000:
        return float(int(v / 5 + 0.5) * 5)
    if v < 10000:
        return float(int(v / 10 + 0.5) * 10)
    if v < 100000:
        return float(int(v / 100 + 0.5) * 100)
    return float(int(v / 500 + 0.5) * 500)


def _fmt(v, dec=False):
    r = _round(v, dec)
    if r < 100 and dec and r != int(r):
        return f"{r:.1f}"
    return f"{int(r):,}"


def _fmtk(v, dec):
    kv = v / 1000.0
    return (f"{kv:.1f}".rstrip("0").rstrip(".")) if dec else f"{int(kv + 0.5)}"


def rate(cur, target=None):
    return RATES[cur] / RATES[target or TARGET]


def convert(text, keep=False, target=None):
    """Rewrite every currency amount inside `text` in the target currency.
    keep=True appends the original amount in parentheses (used in the audit sheet)."""
    target = target or TARGET
    if not isinstance(text, str) or not text:
        return text
    sym = _SYM[target]

    def repl(m):
        cur_s, lo, klo, dash, hi, khi = m.groups()
        cur = _CUR[cur_s.strip()]
        if cur == target:
            return m.group(0)
        r = rate(cur, target)
        anyk = bool(klo or khi)
        dec = ("." in lo) or (hi is not None and "." in hi)
        vlo = _num(lo) * (1000 if anyk else 1) * r
        if hi is None:
            out = sym + ((_fmtk(vlo, dec or vlo < 10000) + "k") if anyk else _fmt(vlo, dec))
        else:
            vhi = _num(hi) * (1000 if anyk else 1) * r
            if anyk:
                d = dec or vlo < 10000
                out = f"{sym}{_fmtk(vlo, d)}–{_fmtk(vhi, d)}k"
            else:
                out = f"{sym}{_fmt(vlo, dec)}–{_fmt(vhi, dec)}"
        if keep:
            out += f" ({m.group(0).strip()})"
        return out
    return _AMT.sub(repl, text)


def first_amount(text, target=None):
    """(lo, hi) of the first currency amount in `text`, in the target currency (floats)."""
    m = _AMT.search(text or "")
    if not m:
        return None
    cur_s, lo, klo, dash, hi, khi = m.groups()
    r = rate(_CUR[cur_s.strip()], target)
    k = 1000 if (klo or khi) else 1
    vlo = _num(lo) * k * r
    vhi = _num(hi) * k * r if hi else vlo
    return vlo, vhi


def money(lo, hi=None, target=None):
    """'$12,600' or '$12,600–14,100' with sensible rounding."""
    sym = _SYM[target or TARGET]
    if hi is None or abs(hi - lo) < 1:
        return sym + _fmt(lo)
    return f"{sym}{_fmt(lo)}–{_fmt(hi)}"


def money_k(lo, hi=None, target=None):
    """'$38–42k' style for totals (nearest $1k; one decimal under $10k)."""
    sym = _SYM[target or TARGET]
    def k(v):
        return f"{v/1000:.1f}".rstrip("0").rstrip(".") if v < 10000 else f"{int(v/1000 + 0.5)}"
    if hi is None or abs(hi - lo) < 500:
        return f"{sym}{k(lo)}k"
    return f"{sym}{k(lo)}–{k(hi)}k"

# ---- fields -----------------------------------------------------------------
# key: (label, market score 1-5, one-line market note used in the programme sheet)
FIELDS = {
    "AI":    ("هوش مصنوعی / یادگیری ماشین", 5,
              "داغ‌ترین بازار؛ «AI Engineer» سریع‌ترین‌رشد (LinkedIn 2026)؛ ولی برنامه‌های ریاضی‌محور (Tübingen، UvA، KTH) بسیار رقابتی‌اند"),
    "SE":    ("مهندسی نرم‌افزار / علوم کامپیوتر", 4,
              "بیشترین حجم آگهی در هر ۸ کشور؛ ورود جونیور از ۲۰۲۳ سخت‌تر شده — سابقهٔ کار شما مزیت است"),
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
     "بالاتر (+۱۰ تا +۲۵٪؛ آلمان €52–60k، انگلستان £35–45k خارج لندن، سوئیس ≈ CHF 95–120k در زوریخ)",
     "بسیار خوب — تیم‌های AI/ML در همهٔ ۸ کشور انگلیسی‌زبان‌اند؛ زوریخ (Google، ETH AI Center، آزمایشگاه‌های AI) یکی از قطب‌های اروپاست و کاملاً انگلیسی؛ فنلاند: FCAI (Aalto/Helsinki) و Silo AI/AMD در هلسینکی، انگلیسی‌محور ولی کوچک",
     "خوب: پیش‌زمینهٔ Computer Engineering + Python؛ ولی برای برنامه‌های Reach (Tübingen، UvA، KTH، Sheffield) معدل ۱۵.۷۷ کافی نیست — برنامه‌های کاربردی (Passau AI Eng، FAU، USI AI (Lugano)، Umeå) هدف بگیرید؛ در انگلستان (فقط Russell Group) Nottingham ACS(AI) و Sheffield AI با 2:1 = ۱۴–۱۵/۲۰ Target‌اند، Southampton AI مرزی؛ کانادا (بدون کبک): Memorial MAI (۱۶ ماه، داخل بودجه) Target، Toronto MScAC (CAD 90,050) Reach و خارج بودجه",
     "رقابت ورودی شدید؛ بخشی از آگهی‌ها «AI» در عنوان دارند ولی کار مهندسی نرم‌افزار معمولی است؛ مدرک به‌تنهایی بدون پورتفولیو/پروژه کافی نیست",
     "LinkedIn/WEF ژانویه ۲۰۲۶ (۱.۳ میلیون شغل جدید AI؛ AI Engineer سریع‌ترین‌رشد)؛ Bitkom 2025"],
    ["مهندسی نرم‌افزار / علوم کامپیوتر", "۴ — بیشترین حجم",
     "مرجع (آلمان €48–55k · هلند €40–50k · سوئد SEK 420–540k · دانمارک DKK 500–540k · سوئیس CHF 85–105k (بالاترین) · انگلستان £28–35k · فنلاند €31–43k)",
     "بسیار خوب",
     "بهترین تناسب با سابقهٔ شما (۲ سال IT + Unity/C#)؛ پذیرش ساده‌تر (2:2)؛ در همهٔ کشورها گزینهٔ Safe دارد؛ کانادا (بدون کبک): MSc پایان‌نامه‌ای Memorial / Manitoba / Saskatchewan / Alberta / Calgary / UVic با TA/RA (Target — استاد راهنما لازم) و Windsor MAC (Safe ولی خارج بودجه)",
     "آگهی‌های جونیور از ۲۰۲۳ کم شده (اثر GenAI)؛ در بریتانیا ۶–۷٪ بیکاری فارغ‌التحصیلان CS — سابقهٔ کار واقعی شما را از این گروه جدا می‌کند",
     "Bitkom 2025 (۱۰۹ هزار جای خالی IT در آلمان، ۷.۷ ماه زمان پرکردن)؛ IW 2024 (آگهی‌ها ۲۶٪ کمتر از ۲۰۲۳)"],
    ["امنیت سایبری", "۴ — کمبود ساختاری",
     "مساوی تا کمی بالاتر؛ در انگلستان (NCSC-certified) و سوئیس (بانک‌ها، بیمه‌ها، ETH/EPFL Cyber؛ حقوق بالا) خوب",
     "خوب — ولی مشاغل دولتی/دفاعی معمولاً به تابعیت یا اقامت بلندمدت نیاز دارند",
     "خوب: MSc Cyber در Russell Group انگلستان (Newcastle، York، Birmingham، Southampton با تأیید NCSC + Sheffield Cybersecurity & AI؛ 2:1 — York 2:2)؛ Saarland (رایگان ولی IELTS 7)؛ AAU کپنهاگ؛ ZHAW MSE Information & Cyber Security (سوئیس، نیاز به معدل A/B)؛ کانادا (بدون کبک): ارشد تخصصی امنیت با شهریهٔ رسمی تأییدشده در فهرست نیست — امنیت را به‌عنوان موضوع پایان‌نامه داخل MSc CS (Calgary / Carleton / UVic، با استاد راهنمای امنیت) بردارید",
     "عدد «۴.۸ میلیون کمبود» ISC2 در گزارش ۲۰۲۵ حذف شد (نیاز اعلام‌شده بود نه آگهی واقعی)؛ کمبود بودجه دلیل اول جای خالی؛ ۳۱٪ تیم‌ها صفر جونیور دارند → برای اولین شغل، کارآموزی + گواهی (Security+، AZ-500) لازم است",
     "ISC2 Workforce Study 2024/2025؛ فهرست مدارک تأییدشدهٔ NCSC (ncsc.gov.uk)"],
    ["ابری / سیستم‌های توزیع‌شده / DevOps", "۴ — پایدار",
     "بالاتر از توسعه‌دهندهٔ عمومی (+۵ تا +۱۵٪)؛ DevOps/SRE در دانمارک و سوئد پرتقاضا؛ سوئیس: بانک‌ها/بیمه‌ها و Google زوریخ (≈ CHF 90–110k)",
     "بسیار خوب",
     "خوب: Newcastle Cloud Computing (Russell Group)، TU Darmstadt DSS، KTH SEDS، USI Software & Data Engineering؛ کانادا: ارشد خالص Cloud نیست — گرایش داخل MSc CS / Alberta course-based / Windsor MAC؛ گواهی AWS/Azure کنار مدرک",
     "کمتر «مدرک‌محور» است؛ برنامه‌های خالص Cloud کم‌اند — معمولاً گرایشِ CS/SE است",
     "tribexyz 2026 (Data/Cloud Engineer پرجست‌وجوترین در UK/DE)؛ آگهی‌های شرکت‌ها"],
    ["علم داده / تحلیل داده", "۳ — جونیور اشباع",
     "مساوی CS در سطح جونیور؛ بالاتر بعد از ۲–۳ سال",
     "بسیار خوب",
     "متوسط: مدرک‌های ارزان و Safe زیاد است (سوئیس: HSLU Lucerne ≈ CHF 3,150/سال و USI Software & Data Eng CHF 8,000/سال، EPFL Data Science فقط Reach؛ سوئد: Skövde؛ انگلستان (Russell Group): Liverpool DS&AI ≈ £34k، Bristol DS £37.9k؛ دانمارک: ITU €16.5k؛ کانادا: Carleton MCS گرایش Data Science & AI (خارج بودجه بدون فاندینگ) و Memorial MAI داخل بودجه) ولی رقابت جونیور بالاست؛ اگر می‌روید، Data Engineering را انتخاب کنید",
     "تعداد فارغ‌التحصیل خیلی بیشتر از جای خالی جونیور؛ آگهی جونیور Data Engineering هم ↓۶۷٪؛ مسیر رایج: تحلیلگر/بک‌اند → مهندس داده",
     "research.com 2026؛ careery.pro 2026؛ datadriven.io 2026"],
    ["سیستم‌های نهفته / رباتیک / خودران", "۴ در آلمان/سوئد؛ ۳ در بقیه",
     "مساوی تا کمی بالاتر در صنعت (Bosch، Continental، ABB، Volvo)؛ پایین‌تر در بریتانیا؛ در سوئیس (ABB، رباتیک ETH) بالا ولی آلمانی‌محور؛ فنلاند: Nokia (Oulu/Espoo، 5G/6G) و Wärtsilä/KONE — R&D انگلیسی",
     "متوسط ⚠️ — تیم‌های R&D انگلیسی‌اند ولی شرکت‌های صنعتی متوسط آلمان/سوئد در عمل زبان محلی می‌خواهند",
     "خوب از نظر پیش‌زمینه (Computer Engineering)؛ گزینه‌ها: Twente ES، Stuttgart INFOTECH، H-BRS Autonomous Systems، FAU Autonomy Tech، Halmstad، MDU، SDU Robot Systems، DTU Autonomous Systems؛ سوئیس: ETH Robotics فقط Reach، ZHAW MSE گرایش مهندسی (آلمانی‌محور)؛ کانادا: برنامه‌های فهرست همه CS / AI / SE‌اند — رباتیک فقط به‌عنوان موضوع پایان‌نامه (Alberta / Calgary)",
     "با معیار «فقط انگلیسی» شما ضعیف‌تر از AI/SE/Cyber؛ وابسته به صنعت خودرو که در ۲۰۲۴–۲۵ آگهی‌هایش کم شد",
     "Bitkom/IW 2024–25؛ Twente/H-BRS/FAU program pages"],
    ["HCI / طراحی تعامل / UX", "۲ — رو به کاهش",
     "پایین‌تر از توسعه‌دهنده (−۱۰ تا −۲۵٪)",
     "خوب",
     "ضعیف برای هدف «حقوق شروع بالا»؛ فقط اگر واقعاً به طراحی علاقه دارید (Siegen رایگان، Twente I-Tech، York HCIT، Chalmers IxD، AAU Medialogy؛ سوئیس برنامهٔ انگلیسی مناسب ندارد — ZHdK آلمانی؛ کانادا: در فهرست نیست)",
     "آگهی UX ↓۷۱٪ و UXR ↓۷۳٪ نسبت به ۲۰۲۲ و از ۲۰۲۳ ثابت؛ متقاضی به ازای هر آگهی دو برابر شده",
     "Indeed Hiring Lab تا Q4 2025 (thevoiceofuser, 2026)؛ uxdesigninstitute 2024؛ academyux Q1 2025"],
    ["توسعه بازی", "۲ — کوچک و پرنوسان",
     "پایین‌تر از نرم‌افزار عمومی (−۲۰ تا −۴۰٪)؛ استودیوهای بزرگ استثنا",
     "خوب (استودیوهای بزرگ انگلیسی‌زبان: لندن، Guildford، Stockholm، Malmö، Copenhagen، Cologne، هلسینکی (Supercell، Rovio، Remedy، Housemarque؛ Unity دفتر بزرگ در تامپره/هلسینکی)؛ سوئیس صنعت بازی کوچکی دارد — Zürich: Giants Software — و ارشد انگلیسی بازی ندارد)",
     "تنها حوزه‌ای که سابقهٔ Unity/C# شما در آن مستقیماً مزیت است؛ اما بازار ۲۰۲۲–۲۵ بدترین دورهٔ خود را داشت — پیشنهاد: ارشد Software/AI بگیرید و بازی را به‌عنوان تخصص/پورتفولیو نگه دارید، مگر Newcastle Game Engineering (£32.3k)، QMUL Computer Games (£36.95k)، Leeds HPG & Games (£34.6k)، Cologne Game Lab یا Aalto Game Design & Development (€17k، ۸ نفر، Reach) را با چشم باز انتخاب کنید؛ کانادا: استودیوهای بزرگ (Ubisoft Toronto، EA Vancouver) هستند ولی مونترال = کبک (حذف)؛ Unity/C# شما اینجا پورتفولیوی co-op (Windsor MAC) یا کارآموزی MScAC است، نه رشتهٔ تحصیل",
     "≈۴۵ هزار اخراج ۲۰۲۲–ژوئیهٔ ۲۰۲۵؛ بیش از ۳۰ استودیو کاملاً بسته شد؛ حقوق برنامه‌نویس Unity ≈۵۰٪ افت؛ Unity Technologies شش دور اخراج",
     "Wikipedia «2022–2026 video game industry layoffs» (GDC State of the Industry 2026؛ 80.lv)"],
]


# ---- cities ------------------------------------------------------------------
# key: (display name "English (فارسی)", approximate student cost-of-living tier incl. rent, per month)
CITIES = {
    # انگلستان
    "Liverpool": ("Liverpool (لیورپول) — شمال غرب؛ ارزان‌ترین شهر بزرگ Russell Group", "ارزان تا متوسط — £950–1,250"),
    "Leeds": ("Leeds (لیدز) — یورکشایر؛ قطب مالی/دیجیتال شمال", "متوسط — £1,000–1,300"),
    "Exeter": ("Exeter (اکستر) — جنوب غرب؛ شهر کوچک دانشگاهی", "متوسط تا گران — £1,050–1,350"),
    "Southampton": ("Southampton (ساوتهمپتون) — ساحل جنوب؛ ۷۵ دقیقه تا لندن", "متوسط — £1,050–1,350"),
    "Birmingham": ("Birmingham (بیرمنگام) — دومین شهر انگلستان؛ میدلندز", "متوسط — £1,000–1,300"),
    "London-MileEnd": ("London – Mile End (لندن شرقی؛ کمپوس QMUL)", "خیلی گران — £1,500–1,800 (تمکن ویزا: £1,570 × ۹)"),
    "Newcastle": ("Newcastle upon Tyne (نیوکاسل) — شمال شرق", "ارزان تا متوسط — £950–1,250"),
    "Nottingham": ("Nottingham (ناتینگهام) — میدلندز", "متوسط — £1,000–1,300"),
    "Manchester": ("Manchester (منچستر) — دومین قطب فناوری انگلستان", "متوسط — £1,050–1,350"),
    "York": ("York (یورک) — شمال انگلستان", "متوسط — £1,000–1,350"),
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
    # فنلاند — اجاره‌های بنیادهای خوابگاهی (TOAS/PSOAS/TYS/LOAS/HOAS) ارزان است؛ بازهٔ زیر با اتاق مشترک یا استودیوی ارزان + خوراک/حمل‌ونقل/بیمه
    "Tampere": ("Tampere (تامپره) — Nokia، Unity، Intel؛ دومین قطب فناوری فنلاند", "ارزان — €800–1,000"),
    "Oulu": ("Oulu (اولو) — Nokia، خوشهٔ 5G/6G؛ شمال", "ارزان — €750–950"),
    "Turku": ("Turku (تورکو) — سومین شهر؛ Bayer، Meyer، Wärtsilä", "ارزان — €800–1,000"),
    "Lappeenranta": ("Lappeenranta (لاپین‌رانتا) — شهر کوچک دانشگاهی، شرق", "ارزان — €700–900"),
    "Espoo": ("Espoo (اسپو) — پردیس Otaniemi؛ Nokia، Rovio، Supercell در منطقهٔ هلسینکی", "متوسط — €950–1,200"),
    "Helsinki": ("Helsinki (هلسینکی) — پایتخت؛ Wolt، Supercell، Remedy، Unity", "متوسط — €1,000–1,300"),
    "Kolding": ("Kolding (کولدینگ) — جنوب یوتلند", "ارزان تا متوسط — DKK 7,500–9,000"),
    "Copenhagen": ("Copenhagen (کپنهاگ)", "خیلی گران — DKK 10,000–12,500"),
    "Lyngby": ("Kgs. Lyngby (لینگبی) — ۱۵ کیلومتری کپنهاگ", "خیلی گران — DKK 9,500–12,000"),
    "Aarhus": ("Aarhus (آرهوس) — دومین شهر دانمارک", "گران — DKK 9,000–11,000"),
    # کانادا (بدون کبک) — اجاره‌ها CMHC اکتبر ۲۰۲۵ (یک‌خوابه) و برآورد رسمی دانشگاه‌ها؛ زندگی دانشجو = اتاق در خانهٔ مشترک + خوراک + رفت‌وآمد + تلفن/بیمه
    "StJohns": ("St. John's (سنت جانز، نیوفاندلند) — پایتخت استان؛ کوچک، ارزان، دور", "ارزان — CAD 1,450–1,750"),
    "Winnipeg": ("Winnipeg (وینیپگ، منیتوبا) — سرد؛ ارزان‌ترین شهر بزرگ غرب", "ارزان — CAD 1,400–1,700"),
    "Saskatoon": ("Saskatoon (ساسکاتون، ساسکاچوان) — شهر دانشگاهی کوچک", "ارزان — CAD 1,400–1,700"),
    "Edmonton": ("Edmonton (ادمونتون، آلبرتا) — پایتخت آلبرتا؛ بدون مالیات فروش استانی", "ارزان تا متوسط — CAD 1,500–1,800"),
    "Calgary": ("Calgary (کلگری، آلبرتا) — قطب تک آلبرتا؛ بدون مالیات فروش استانی", "متوسط — CAD 1,650–2,000"),
    "Victoria": ("Victoria (ویکتوریا، بریتیش کلمبیا) — معتدل، گران؛ ۹۰ دقیقه کشتی تا ونکوور", "گران — CAD 1,900–2,300"),
    "Ottawa": ("Ottawa (اتاوا، انتاریو) — پایتخت؛ دولت + Shopify/تک", "متوسط تا گران — CAD 1,800–2,200"),
    "Windsor": ("Windsor (ویندزور، انتاریو) — مرز دیترویت؛ خودرو", "ارزان تا متوسط — CAD 1,450–1,800"),
    "Toronto": ("Toronto (تورنتو، انتاریو) — بزرگ‌ترین بازار کار کانادا؛ گران", "خیلی گران — CAD 2,100–2,600"),
}

# ---- programmes ---------------------------------------------------------------
# country, university, city key (see CITIES), programme, field key, duration, fee text (local), (cur, annual amount low, high or None),
# entry requirement, IELTS, QS 2027, tier for GPA 15.77/20, note, source URL
P = []

def add(*a):
    P.append(a)

# ===== انگلستان (GBP) — فقط دانشگاه‌های Russell Group در انگلستان (به خواست شما، ۲۸ سپتامبر ۲۰۲۶؛ نسخهٔ ۳.۱۱) =====
# ۲۰ عضو انگلیسی گروه راسل: Birmingham، Bristol، Cambridge، Durham، Exeter، Imperial، KCL، Leeds، Liverpool، LSE، Manchester، Newcastle، Nottingham، Oxford، QMUL، Sheffield، Southampton، UCL، Warwick، York.
# Cardiff / Edinburgh / Glasgow / Queen's Belfast عضو گروه راسل‌اند ولی در انگلستان نیستند → حذف. Oxford/Cambridge/LSE: ارشد CS با معدل ۱۵.۷۷ عملاً بسته یا بدون برنامهٔ مناسب → نیامده‌اند.
# نکتهٔ مشترک همهٔ ردیف‌های انگلستان: هیچ‌کدام گام ۱ بودجه (شهریه + تمکن £10,827 خارج لندن / £14,130 لندن ≤ $40,000) را بدون بورس رد نمی‌کنند — جزئیات در شیت «تصمیم» بخش پ-۲.
add("انگلستان", "University of Exeter (Russell Group)", "Exeter", "MSc Advanced Computer Science", "SE", "۱ سال", "£30,100 (2027/28 رسمی)", ("GBP", 30100, None),
    "2:1 در CS/رشتهٔ مرتبط (ممکن است مصاحبهٔ ویدئویی بخواهند)؛ معادل ایرانی را رسمی نیافتم — معمولاً ۱۴–۱۵/۲۰ (چک شود)", "Profile B1 ≈ 6.5 (چک شود)", "≈ 160 (QS 2026: 161)", "Target", "ارزان‌ترین Russell Group انگلستان برای ۲۰۲۷؛ بورس Exeter Excellence £3k/£5k/£10k برای دارندگان پیشنهاد (درخواست جدا)؛ شهر کوچک، بازار IT محلی کوچک",
    "https://www.exeter.ac.uk/study/postgraduate/courses/computerscience/advancedcsmsc/")
add("انگلستان", "University of Liverpool (Russell Group)", "Liverpool", "MSc Advanced Computer Science", "SE", "۱ سال", "£34,000 (2026/27 رسمی؛ رقم 2027/28 هنوز اعلام نشده)", ("GBP", 34000, None),
    "2:2 در CS/رشتهٔ مرتبط — تنها Russell Group این فهرست که رسماً 2:2 می‌پذیرد → با ۱۵.۷۷ امن؛ متقاضیان ایران باید از «فرم درخواست جایگزین» (تحریم) استفاده کنند", "6.5 (هر بخش ≥ 5.5)", "≈ 165 (QS 2026)", "Safe/Target", "درخواست از ۵ اکتبر ۲۰۲۶ باز می‌شود؛ مهلت بین‌المللی ۲۳ اوت ۲۰۲۷؛ ودیعه؛ Liverpool شهر ارزانِ RG",
    "https://www.liverpool.ac.uk/courses/advanced-computer-science-msc")
add("انگلستان", "University of Liverpool (Russell Group)", "Liverpool", "MSc Data Science and Artificial Intelligence", "DS", "۱ سال", "≈ £34,000 (هم‌باند با Advanced CS همین دانشگاه 2026/27؛ چک شود)", ("GBP", 34000, None),
    "2:1 یا 2:2 قوی در CS/ریاضی/مهندسی (چک شود)", "6.5 (هر بخش ≥ 5.5)", "≈ 165 (QS 2026)", "Target", "همان دانشگاه، همان مهلت و فرم جایگزین ایران",
    "https://www.liverpool.ac.uk/courses/data-science-and-artificial-intelligence-msc")
add("انگلستان", "Newcastle University (Russell Group)", "Newcastle", "MSc Advanced Computer Science", "SE", "۱ سال", "≈ £31,700 (ورودی ۲۰۲۶ — رقم رسمی ۲۰۲۷ هنوز منتشر نشده؛ صفحهٔ رسمی از ایران بارگذاری نشد)", ("GBP", 31700, None),
    "2:1 در CS/رشتهٔ کامپیوتری، یا 2:2 با سابقهٔ کار مرتبط؛ معادل ایرانی را رسمی نیافتم (معمولاً ۱۴–۱۵/۲۰)", "6.5 (هر بخش ≥ 5.5)", "149", "Target", "ارزان‌ترین RG بعد از Exeter؛ ودیعهٔ £1,500؛ rolling؛ بورس VC International £8,000 خودکار (فهرست کشوری ۲۰۲۷ را چک کنید) و VC Excellence تا ۵۰٪ (درخواست تا ۸ ژوئن ۲۰۲۷)",
    "https://www.ncl.ac.uk/postgraduate/")
add("انگلستان", "Newcastle University (Russell Group)", "Newcastle", "MSc Cyber Security", "CY", "۱ سال", "≈ £31,700 (هم‌باند با Advanced CS، ورودی ۲۰۲۶؛ چک شود)", ("GBP", 31700, None),
    "2:1 در CS/کامپیوتر (2:2 + سابقهٔ مرتبط بررسی می‌شود)", "6.5 (هر بخش ≥ 5.5)", "149", "Target", "مدرک تأییدشدهٔ NCSC؛ همان بورس‌های Newcastle",
    "https://www.ncl.ac.uk/postgraduate/")
add("انگلستان", "Newcastle University (Russell Group)", "Newcastle", "MSc Cloud Computing", "CLOUD", "۱ سال", "≈ £31,700 (هم‌باند با Advanced CS، ورودی ۲۰۲۶؛ چک شود)", ("GBP", 31700, None),
    "2:1 در CS/کامپیوتر (2:2 + سابقهٔ مرتبط بررسی می‌شود)", "6.5 (هر بخش ≥ 5.5)", "149", "Target", "یکی از معدود ارشدهای خالص Cloud در Russell Group",
    "https://www.ncl.ac.uk/postgraduate/")
add("انگلستان", "Newcastle University (Russell Group)", "Newcastle", "MSc Computer Game Engineering", "GD", "۱ سال", "£32,300 (2026)", ("GBP", 32300, None),
    "2:2 در رشتهٔ کامپیوتری/ریاضی‌محور (طبق QS TopUniversities و IDP — صفحهٔ رسمی را چک کنید)", "6.5", "149", "Target/Reach", "معتبرترین ارشد مهندسی بازی انگلستان؛ ۷ ماه Unity/C# شما اینجا امتیاز است",
    "https://www.ncl.ac.uk/postgraduate/")
add("انگلستان", "University of York (Russell Group)", "York", "MSc Advanced Computer Science", "SE", "۱ سال", "£32,900 (2027/28 رسمی)", ("GBP", 32900, None),
    "2:2 با پیش‌زمینهٔ قوی — صفحهٔ رسمی ایرانِ York: 2:1 = ۱۵/۲۰، 2:2 = ۱۳/۲۰ → ۱۵.۷۷ هر دو را رد می‌کند", "6.5", "=158", "Target", "بورس بین‌المللی York برای ارشد CS عملاً فقط Chevening/تخفیف فارغ‌التحصیلان خودش",
    "https://www.york.ac.uk/study/postgraduate-taught/courses/msc-advanced-computer-science/")
add("انگلستان", "University of York (Russell Group)", "York", "MSc Human-Centred Interactive Technologies", "HCI", "۱ سال", "£32,900 (2027/28)", ("GBP", 32900, None),
    "2:2 (York برای ایران: ۱۳/۲۰)", "6.5", "=158", "Target", "بهترین برنامهٔ HCI انگلستان برای معدل شما؛ ولی بازار UX ضعیف",
    "https://www.york.ac.uk/study/postgraduate-taught/courses/msc-human-centred-interactive-technologies/")
add("انگلستان", "University of York (Russell Group)", "York", "MSc Cyber Security", "CY", "۱ سال", "≈ £32,900 (هم‌باند با Advanced CS 2027/28؛ چک شود)", ("GBP", 32900, None),
    "2:2 در CS/رشتهٔ مرتبط (چک شود)", "6.5", "=158", "Target", "مدرک تأییدشدهٔ NCSC",
    "https://www.york.ac.uk/study/postgraduate-taught/courses/msc-cyber-security/")
add("انگلستان", "University of Sheffield (Russell Group)", "Sheffield", "MSc Advanced Computer Science", "SE", "۱ سال", "£34,550 (2027/28 رسمی؛ شهریهٔ ثابت)", ("GBP", 34550, None),
    "2:1 در CS/مهندسی نرم‌افزار — صفحهٔ رسمی ایرانِ Sheffield: 2:1 = ۱۴/۲۰ دانشگاه دولتی (First ۱۷، 2:2 ۱۳) → ۱۵.۷۷ ✓؛ بدون توصیه‌نامه", "6.5 (هر بخش ≥ 6.0)", "82", "Target", "بورس International PG £7,000 سال ۲۰۲۷ فقط ۱۰ کشور (ایران نیست)؛ شهر ارزانِ RG",
    "https://www.sheffield.ac.uk/postgraduate/taught/courses/2027/advanced-computer-science-msc")
add("انگلستان", "University of Sheffield (Russell Group)", "Sheffield", "MSc Artificial Intelligence", "AI", "۱ سال", "≈ £34,550 (هم‌باند با Advanced CS 2027/28؛ چک شود)", ("GBP", 34550, None),
    "2:1 در CS/رشتهٔ مرتبط با برنامه‌نویسی (ایران: ۱۴/۲۰ دولتی) → ۱۵.۷۷ ✓", "6.5 (هر بخش ≥ 6.0)", "82", "Target/Reach", "رتبهٔ بالا؛ رقابتی‌تر از Advanced CS",
    "https://www.sheffield.ac.uk/postgraduate/taught/courses/2027/artificial-intelligence-msc")
add("انگلستان", "University of Sheffield (Russell Group)", "Sheffield", "MSc Cybersecurity and Artificial Intelligence", "CY", "۱ سال", "≈ £34,550 (هم‌باند با Advanced CS 2027/28؛ چک شود)", ("GBP", 34550, None),
    "2:1 در CS/رشتهٔ مرتبط (ایران: ۱۴/۲۰ دولتی) → ۱۵.۷۷ ✓", "6.5 (هر بخش ≥ 6.0)", "82", "Target", "ترکیب دو حوزهٔ کم‌عرضه؛ همان شهر ارزان",
    "https://www.sheffield.ac.uk/postgraduate/taught/courses/2027/cybersecurity-and-artificial-intelligence-msc")
add("انگلستان", "University of Leeds (Russell Group)", "Leeds", "MSc Advanced Computer Science (گرایش‌های AI / Cloud / Data Analytics)", "SE", "۱ سال", "£34,600 (ورودی ۲۰۲۷ رسمی)", ("GBP", 34600, None),
    "2:1 در CS/رشتهٔ مرتبط با برنامه‌نویسی؛ معادل ایرانی را رسمی نیافتم (معمولاً ۱۵/۲۰)", "6.5 (هر بخش ≥ 6.0)", "≈ 86 (QS 2026)", "Target/Reach", "مهلت بین‌المللی ۳۰ ژوئیه ۲۰۲۷؛ Leeds بازار IT متوسط‌به‌بالا (Sky، BJSS، NHS Digital)",
    "https://courses.leeds.ac.uk/")
add("انگلستان", "University of Leeds (Russell Group)", "Leeds", "MSc High-Performance Graphics and Games Engineering", "GD", "۱ سال", "≈ £34,600 (هم‌باند با Advanced CS ۲۰۲۷؛ چک شود)", ("GBP", 34600, None),
    "2:1 در CS با C++ قوی؛ ۷ ماه Unity/C# شما کمک می‌کند (معادل ایرانی: معمولاً ۱۵/۲۰)", "6.5 (هر بخش ≥ 6.0)", "≈ 86 (QS 2026)", "Target/Reach", "تنها ارشد گرافیک/موتور بازی در Russell Group؛ همان مهلت ۳۰ ژوئیه ۲۰۲۷",
    "https://courses.leeds.ac.uk/")
add("انگلستان", "University of Nottingham (Russell Group)", "Nottingham", "MSc Advanced Computer Science / Advanced CS (Artificial Intelligence)", "AI", "۱ سال", "£34,800 (ورودی ۲۰۲۷ رسمی)", ("GBP", 34800, None),
    "2:1 در CS یا STEM با محتوای محاسباتی؛ معادل ایرانی را رسمی نیافتم (معمولاً ۱۴–۱۵/۲۰)", "6.5 (هر بخش ≥ 6.0)", "≈ 97 (QS 2026)", "Target/Reach", "نسخهٔ دوسالهٔ MSc CS(AI) برای غیر-CS £23,200/سال — برای شما لازم نیست",
    "https://www.nottingham.ac.uk/pgstudy/course/taught/computer-science-artificial-intelligence-msc")
add("انگلستان", "University of Birmingham (Russell Group)", "Birmingham", "MSc Advanced Computer Science", "SE", "۱ سال", "≈ £34,740 (به نقل از QS TopUniversities — صفحهٔ رسمی از ایران باز نشد؛ چک شود)", ("GBP", 34740, None),
    "2:1 در رشتهٔ کامپیوتری (معادل ایرانی: معمولاً ۱۴–۱۵/۲۰؛ چک شود)", "6.5 (هر بخش ≥ 6.0)", "≈ 76 (QS 2026)", "Target/Reach", "دومین شهر انگلستان؛ بازار IT بزرگ‌تر از Sheffield/Liverpool؛ زندگی متوسط",
    "https://www.birmingham.ac.uk/postgraduate/courses/taught/computer-science")
add("انگلستان", "University of Birmingham (Russell Group)", "Birmingham", "MSc Cyber Security", "CY", "۱ سال", "≈ £34,740 (هم‌باند با Advanced CS؛ چک شود)", ("GBP", 34740, None),
    "2:1 در رشتهٔ کامپیوتری (چک شود)", "6.5 (هر بخش ≥ 6.0)", "≈ 76 (QS 2026)", "Target/Reach", "مدرک تأییدشدهٔ NCSC",
    "https://www.birmingham.ac.uk/postgraduate/courses/taught/computer-science")
add("انگلستان", "University of Southampton (Russell Group)", "Southampton", "MSc Artificial Intelligence", "AI", "۱ سال", "£36,800 (سپتامبر ۲۰۲۷ رسمی)", ("GBP", 36800, None),
    "2:1 در CS/مهندسی/ریاضی — صفحهٔ ایرانِ Southampton: ۱۷ / ۱۵ / ۱۳ از ۲۰ بسته به ردهٔ دانشگاه (سمنان احتمالاً ردهٔ ۱۵/۲۰) → ۱۵.۷۷ مرزی‑✓", "6.5 (هر بخش ≥ 6.0)", "≈ 87 (QS 2026)", "Target/Reach", "ودیعهٔ £2,000؛ Spärck AI Scholarship: ۱۱ بورس کامل + کمک‌هزینه برای همین رشته (بسیار رقابتی، بین‌المللی مجاز)",
    "https://www.southampton.ac.uk/courses/artificial-intelligence-masters-msc")
add("انگلستان", "University of Southampton (Russell Group)", "Southampton", "MSc Cyber Security", "CY", "۱ سال", "≈ £36,800 (هم‌باند با MSc AI سپتامبر ۲۰۲۷؛ چک شود)", ("GBP", 36800, None),
    "2:1 در CS/رشتهٔ مرتبط (ایران: ۱۷ / ۱۵ / ۱۳ بسته به ردهٔ دانشگاه)", "6.5 (هر بخش ≥ 6.0)", "≈ 87 (QS 2026)", "Target/Reach", "مدرک تأییدشدهٔ NCSC؛ مرکز آکادمیک امنیت سایبری",
    "https://www.southampton.ac.uk/courses/cyber-security-masters-msc")
add("انگلستان", "Queen Mary University of London (Russell Group)", "London-MileEnd", "MSc Advanced Computer Science", "SE", "۱ سال", "£36,950 (سپتامبر ۲۰۲۷ رسمی)", ("GBP", 36950, None),
    "2:1 — صفحهٔ رسمی ایرانِ QMUL: 2:1 = ۱۵–۱۶/۲۰ (2:2 = ۱۳.۵–۱۴، First = ۱۷.۵–۱۸.۵) → ۱۵.۷۷ ✓", "6.5 (هر بخش ≥ 6.0)", "≈ 110 (QS 2026)", "Target", "ارزان‌ترین RG لندن؛ ودیعهٔ £2,000؛ تمکن لندنی (£1,570 × ۹) و زندگی گران",
    "https://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/advanced-computer-science-msc/")
add("انگلستان", "Queen Mary University of London (Russell Group)", "London-MileEnd", "MSc Computer Games", "GD", "۱ سال", "≈ £36,950 (هم‌باند با Advanced CS سپتامبر ۲۰۲۷؛ چک شود)", ("GBP", 36950, None),
    "2:1 در CS/رشتهٔ مرتبط (ایران: ۱۵–۱۶/۲۰) → ۱۵.۷۷ ✓", "6.5 (هر بخش ≥ 6.0)", "≈ 110 (QS 2026)", "Target", "لندن = بزرگ‌ترین خوشهٔ استودیوهای بازی اروپا؛ ولی گران‌ترین زندگی",
    "https://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/computer-games-msc/")
add("انگلستان", "University of Manchester (Russell Group)", "Manchester", "MSc Advanced Computer Science", "SE", "۱ سال", "£39,400 (ورودی ۲۰۲۶ رسمی؛ رقم ۲۰۲۷ هنوز اعلام نشده)", ("GBP", 39400, None),
    "2:1 در CS — صفحهٔ رسمی ایرانِ Manchester: ارشد معمولاً ≥ ۱۴/۲۰ دانشگاه دولتی (۱۵ خصوصی)، ولی دپارتمان CS بالاتر از حداقل دانشگاه می‌خواهد و رتبهٔ کلاسی را می‌بیند → ۱۵.۷۷ مرزی", "6.5–7.0 (چک شود)", "35", "Target/Reach", "مهلت‌های مرحله‌ای (≈ نوامبر / ژانویه / فوریه / می)؛ ودیعهٔ £2,500؛ بدون هزینهٔ درخواست؛ Global Futures Scholarship شامل ایران نیست؛ دومین قطب فناوری انگلستان",
    "https://www.manchester.ac.uk/study/masters/courses/list/")
add("انگلستان", "Durham University (Russell Group)", "Durham", "MSc Advanced Computer Science (و MSc Data Science)", "SE", "۱ سال", "£34,500 (2026 entry)", ("GBP", 34500, None),
    "2:1 در CS — جدول رسمی Durham برای ایران: 1st ≥ ۱۷/۲۰، 2:1 = ۱۴–۱۶/۲۰، 2:2 = ۱۲–۱۳/۲۰ (دانشگاه باید در فهرست Ecctis باشد) → ۱۵.۷۷ ✓", "6.5 (هر بخش ≥ 6.0)", "=94", "Target", "QS 2027 ≈ 94 · High Fliers 2025: دهم · ارزان‌ترین شهرِ این فهرست؛ ۱۵ دقیقه تا نیوکاسل؛ خوابگاه ارشد تضمینی نیست",
    "https://www.durham.ac.uk/study/courses/advanced-computer-science-g5t609/")
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

# ===== سوئیس (CHF) =====
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
add("سوئیس", "University of Bern", "Bern", "Swiss Joint MSc Computer Science (Bern / Neuchâtel / Fribourg)", "SE", "۱.۵ سال (90 ECTS)", "CHF 2,609 در ترم برای خارجی‌ها از پاییز ۲۰۲۶ (پایه CHF 850 + اضافهٔ غیرسوئیسی‌ها CHF 1,700 + جانبی CHF 59) ≈ CHF 5,200/سال", ("CHF", 5218, None),
    "کارشناسی Computer Science یا معادل (بررسی موردی؛ حداکثر ۶۰ ECTS تکمیلی — دروس تکمیلی ممکن است آلمانی/فرانسه باشند)", "بدون آزمون (B2 توصیه — FAQ رسمی)", "=191", "Target", "⚠️ شهریهٔ خارجی‌ها از پاییز ۲۰۲۶ سه‌برابر شد (رسمی unibe.ch) → همان مدرک مشترک را از Neuchâtel (CHF 790/ترم) یا Fribourg (CHF 985/ترم) بگیرید؛ مهلت ۳۰ آوریل — ویزایی‌ها مهلت دیرهنگام ندارند",
    "https://www.philnat.unibe.ch/studies/study_programs/master_s_in_computer_science/index_eng.html")
add("سوئیس", "University of Neuchâtel", "Neuchatel", "Swiss Joint MSc Computer Science (ثبت‌نام در Neuchâtel)", "SE", "۱.۵ سال (90 ECTS)", "CHF 790 در ترم (خارجی؛ شامل همهٔ هزینه‌ها) = CHF 1,580/سال", ("CHF", 1580, None),
    "کارشناسی CS یا معادل (بررسی موردی؛ حداکثر ۶۰ ECTS تکمیلی)", "بدون آزمون (B2 توصیه — FAQ رسمی)", "—", "Target", "ارزان‌ترین شهریهٔ سوئیس؛ همان مدرک مشترک Bern/Fribourg (دروس در سه شهر، بلیت قطار جبران می‌شود)؛ مهلت ۳۰ آوریل (خارجی‌ها: تا ۳۱ مارس بفرستید)؛ هزینهٔ پرونده CHF 100 از شهریه کم می‌شود؛ شهر فرانسه‌زبان",
    "https://mcs.unibnf.ch/")
add("سوئیس", "University of Fribourg", "Fribourg", "Swiss Joint MSc Computer Science (ثبت‌نام در Fribourg)", "SE", "۱.۵ سال (90 ECTS)", "CHF 985 در ترم (خارجی؛ رسمی؛ شامل CHF 115 اضافهٔ خارجی‌ها) = CHF 1,970/سال", ("CHF", 1970, None),
    "کارشناسی CS یا معادل (بررسی موردی؛ حداکثر ۶۰ ECTS تکمیلی)", "بدون آزمون (B2 توصیه — FAQ رسمی)", "=670", "Target", "همان برنامهٔ مشترک Bern/Neuchâtel؛ شهر دوزبانه و ارزان‌تر؛ ⚠️ مهلت ویزایی‌ها ۱–۲۸ فوریه ۲۰۲۷ (رسمی unifr.ch)",
    "https://www.unifr.ch/inf/en/")
add("سوئیس", "University of Basel", "Basel", "MSc Computer Science", "SE", "۱.۵ سال (90 ECTS)", "CHF 850 در ترم (برای همه؛ بدون اضافهٔ خارجی‌ها — رسمی 2026/27) = CHF 1,700/سال", ("CHF", 1700, None),
    "کارشناسی CS یا معادل با نمرات خوب؛ بررسی فردی", "B2–C1 (چک شود)", "=150", "Target/Reach", "رتبهٔ ۱۵۰؛ 90 ECTS انگلیسی؛ هزینهٔ درخواست CHF 100؛ ⚠️ کانتون Basel تمکن CHF 24,000/سال می‌خواهد؛ مهلت ۳۰ آوریل (رسمی)",
    "https://dmi.unibas.ch/en/studies/computer-science/masters/")
add("سوئیس", "University of Zurich (UZH)", "Zuerich", "MSc Informatics (گرایش‌ها: Software Systems، Data Science، People-Oriented Computing…)", "SE", "۱.۵–۲ سال (90/120 ECTS)", "CHF 879 در ترم (خارجی؛ شامل CHF 100 اضافهٔ خارجی‌ها و CHF 59 جانبی) ≈ CHF 1,760/سال", ("CHF", 1760, None),
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
add("هلند", "University of Amsterdam (UvA)", "Amsterdam", "MSc Software Engineering (۱ ساله!)", "SE", "۱ سال", "€34,300 (2026/27 رسمی — ارشد یک‌سالهٔ دانشکدهٔ علوم برای غیر-EEA)", ("EUR", 34300, None),
    "کارشناسی CS با پیش‌زمینهٔ برنامه‌نویسی/نرم‌افزار؛ بررسی موردی", "6.5", "60", "Target/Reach", "تنها ارشد ۱ سالهٔ معتبر هلند؛ با وجود شهریهٔ بالاتر، کل هزینه‌اش (۱ سال زندگی) از دوساله‌ها کمتر است؛ Amsterdam = بهترین بازار انگلیسی‌زبان ولی بدترین مسکن (اتاق €900–1,300)؛ ⚠️ رقم قبلی ≈ €23,540 غلط بود",
    "https://www.uva.nl/en/programmes/masters/software-engineering/software-engineering.html")
add("هلند", "University of Amsterdam (UvA)", "Amsterdam", "MSc Artificial Intelligence", "AI", "۲ سال", "€26,000 (2026/27 رسمی — ارشد دوسالهٔ دانشکدهٔ علوم)", ("EUR", 26000, None),
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
add("سوئد", "KTH Royal Institute of Technology", "Stockholm", "MSc Machine Learning", "AI", "۲ سال", "≈ SEK 180,000–190,000 (کل دوره ≈ SEK 360–380k)", ("SEK", 180000, 190000),
    "کارشناسی CS/ریاضی قوی؛ بسیار رقابتی", "6.5", "82", "Reach", "Stockholm گران (اتاق SEK 7–10k)؛ رقم دقیق روی kth.se فقط در سامانهٔ اپلای نمایش داده می‌شود",
    "https://www.kth.se/en/studies/master/machine-learning")
add("سوئد", "KTH Royal Institute of Technology", "Stockholm", "MSc Cybersecurity", "CY", "۲ سال", "≈ SEK 180,000–190,000", ("SEK", 180000, 190000),
    "کارشناسی CS", "6.5", "82", "Reach", "",
    "https://www.kth.se/en/studies/master/cybersecurity")
add("سوئد", "KTH Royal Institute of Technology", "Stockholm-Kista", "MSc Software Engineering of Distributed Systems", "CLOUD", "۲ سال", "SEK 180,000–190,000", ("SEK", 180000, 190000),
    "کارشناسی CS", "6.5", "82", "Target/Reach", "Kista = قطب ICT سوئد (Ericsson)",
    "https://www.kth.se/en/studies/master/software-engineering-of-distributed-systems")
add("سوئد", "Chalmers University of Technology", "Gothenburg", "MSc Data Science and AI", "DS", "۲ سال", "≈ SEK 175,000 (2026/27؛ 2025/26: SEK 160,000)", ("SEK", 175000, None),
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

# ---- فنلاند (۷ کشور از نسخهٔ ۳.۱۰) — شهریه‌ها از صفحه‌های رسمی ۲۰۲۶/۲۷؛ درخواست مشترک ۷–۲۱ ژانویه ۲۰۲۷ (Tampere/Oulu/Turku/LUT)، Aalto ۷ دسامبر ۲۰۲۶ – ۵ ژانویه ۲۰۲۷، Helsinki ۵–۱۹ ژانویه ۲۰۲۷ ----
add("فنلاند", "Tampere University", "Tampere", "MSc Computing Sciences and Electrical Engineering — AI-native Software (Software, Web & Cloud)", "SE", "۲ سال", "€12,000 (رسمی 2026/27؛ Early-bird −€2,000 سال اول)", ("EUR", 12000, None),
    "کارشناسی مرتبط (CS/SE/IT) با برنامه‌نویسی و ریاضی", "6.5 (W 5.5)", "436", "Target", "بورس ۵۰٪ برای کل دوره هنگام پذیرش (گزینشی)؛ Nokia/Unity/Intel در شهر؛ خوابگاه TOAS €212–410؛ مهلت ۲۱ ژانویه ۲۰۲۷",
    "https://www.tuni.fi/en/tau/masters-programmes/ai-native-software-computing-sciences-and-electrical-engineering")
add("فنلاند", "Tampere University", "Tampere", "MSc Computing Sciences and Electrical Engineering — Data Science", "DS", "۲ سال", "€12,000", ("EUR", 12000, None),
    "کارشناسی مرتبط + ریاضی/آمار", "6.5 (W 5.5)", "436", "Target", "همان برنامهٔ CSEE، تخصص Data Science",
    "https://www.tuni.fi/en/tau/masters-programmes/data-science-computing-sciences-and-electrical-engineering")
add("فنلاند", "Tampere University", "Tampere", "MSc Computing Sciences and Electrical Engineering — Information Security", "CY", "۲ سال", "€12,000", ("EUR", 12000, None),
    "کارشناسی CS/IT/EE", "6.5 (W 5.5)", "436", "Target", "تخصص امنیت اطلاعات؛ Nokia/Insta/Nixu در تامپره",
    "https://www.tuni.fi/en/tau/masters-programmes/information-security-computing-sciences-and-electrical-engineering")
add("فنلاند", "Tampere University", "Tampere", "MSc Computing Sciences and Electrical Engineering — Human-Technology Interaction", "HCI", "۲ سال", "€12,000", ("EUR", 12000, None),
    "کارشناسی CS/IT یا مرتبط", "6.5 (W 5.5)", "436", "Target", "گروه HTI و Gamification تامپره؛ برای علاقه به UX/بازی",
    "https://www.tuni.fi/en/tau/masters-programmes/human-technology-interaction-computing-sciences-and-electrical-engineering")
add("فنلاند", "University of Oulu", "Oulu", "MSc (Tech) Computer Science and Engineering — Artificial Intelligence / Applied Computing", "AI", "۲ سال", "€10,000 (رسمی؛ ۳۰٪ معافیت سال دوم)", ("EUR", 10000, None),
    "کارشناسی CS/CE/EE؛ ۷۰ جای تحصیل", "6.5", "360", "Target", "ارزان‌ترین شهریهٔ فنلاند در فهرست؛ Nokia و خوشهٔ 6G در Oulu؛ خوابگاه PSOAS €250–380؛ مهلت ۲۱ ژانویه ۲۰۲۷",
    "https://www.oulu.fi/en/apply/masters-computer-science-and-engineering")
add("فنلاند", "University of Turku", "Turku", "MSc (Tech) Information and Communication Technology — Software Engineering", "SE", "۲ سال", "€12,000 (رسمی؛ Early-bird −€2,000؛ ۵۰٪ سال دوم با ۵۵ واحد)", ("EUR", 12000, None),
    "کارشناسی مرتبط (CS/SE/IT)؛ سهمیهٔ ۵۵ نفر برای کل ICT", "6.5", "398", "Target", "بورس سال دوم برای همهٔ واجدان شرایط (۵۵ واحد در سال اول) → کل شهریه می‌تواند €16,000 شود؛ خوابگاه TYS €250–400",
    "https://www.utu.fi/en/study-at-utu/masters-degree-programme-in-information-and-communication-technology-software-engineering")
add("فنلاند", "University of Turku", "Turku", "MSc (Tech) Information and Communication Technology — Cyber Security (EIT Digital)", "CY", "۲ سال", "€12,000", ("EUR", 12000, None),
    "کارشناسی CS/IT/EE", "6.5", "398", "Target", "عضو EIT Digital Master School (امکان مدرک دوگانه)",
    "https://www.utu.fi/en/study-at-utu/masters-degree-programme-in-information-and-communication-technology-cyber-security")
add("فنلاند", "LUT University", "Lappeenranta", "MSc (Tech) Software Engineering", "SE", "۲ سال", "€15,000 (رسمی 2026/27؛ بورس Early-bird/ادامهٔ تحصیل تا €5,000)", ("EUR", 15000, None),
    "کارشناسی مهندسی/CS با برنامه‌نویسی", "6.5", "390", "Target", "شهر کوچک و ارزان کنار مرز روسیه؛ گام ۱ فقط با بورس €5,000 رد می‌شود؛ خوابگاه LOAS €250–450",
    "https://www.lut.fi/en/studies/masters-programmes")
add("فنلاند", "Aalto University", "Espoo", "MSc (Tech) Computer Science", "SE", "۲ سال", "€17,000 (رسمی؛ گروه فناوری)", ("EUR", 17000, None),
    "کارشناسی CS/SE قوی؛ GRE اختیاری", "6.5 (W 5.5)", "126", "Reach", "بهترین برند فنی فنلاند؛ اکوسیستم استارتاپی Otaniemi؛ خوابگاه AYY/HOAS €300–700؛ مهلت ۵ ژانویه ۲۰۲۷",
    "https://www.aalto.fi/en/study-options/computer-science-master-of-science-technology")
add("فنلاند", "Aalto University", "Espoo", "MSc (Tech) Machine Learning, Data Science and Artificial Intelligence (Macadamia)", "AI", "۲ سال", "€17,000", ("EUR", 17000, None),
    "کارشناسی CS/ریاضی/EE با ریاضیات قوی؛ GRE (گروه ۲)", "6.5 (W 5.5)", "126", "Reach", "شناخته‌شده‌ترین ارشد ML فنلاند؛ رقابت بالا",
    "https://www.aalto.fi/en/study-options/machine-learning-data-science-and-artificial-intelligence-master-of-science-technology")
add("فنلاند", "Aalto University", "Espoo", "MSc (Tech) Security and Cloud Computing (SECCLO، Erasmus Mundus)", "CLOUD", "۲ سال", "€17,000 (مسیر Aalto؛ کنسرسیوم بورس Erasmus Mundus جدا دارد)", ("EUR", 17000, None),
    "کارشناسی CS/IT؛ ریاضی/شبکه", "6.5 (W 5.5)", "126", "Reach", "سال دوم در یکی از ۶ دانشگاه شریک (KTH، DTU، NTNU، …)",
    "https://www.aalto.fi/en/study-options/security-and-cloud-computing-secclo-master-of-science-technology")
add("فنلاند", "Aalto University", "Espoo", "MSc (Tech) Computer, Communication and Information Sciences — Game Design and Development", "GD", "۲ سال", "€17,000 (Studyinfo 2027)", ("EUR", 17000, None),
    "کارشناسی مرتبط + پورتفولیو؛ فقط ۸ جای تحصیل", "6.5 (W 5.5)", "126", "Reach", "هلسینکی = قطب بازی اروپا (Supercell، Rovio، Remedy، Housemarque، Unity)؛ سابقهٔ Unity شما مزیت است؛ ۸ نفر ⇒ Reach",
    "https://opintopolku.fi/konfo/en/toteutus/1.2.246.562.17.00000000000000008124")
add("فنلاند", "University of Helsinki", "Helsinki", "MSc Computer Science (Algorithms / Networks / Software)", "SE", "۲ سال", "€15,000 (رسمی؛ مهلت ۵–۱۹ ژانویه ۲۰۲۷)", ("EUR", 15000, None),
    "کارشناسی CS با ≥ ۶۰ ECTS CS", "6.5 (W 6.0)", "123", "Target/Reach", "بالاترین رتبهٔ فنلاند؛ درخواست جدا از سامانهٔ مشترک؛ خوابگاه HOAS €300–450",
    "https://www.helsinki.fi/en/degree-programmes/computer-science-masters-programme")
add("فنلاند", "University of Helsinki", "Helsinki", "MSc Data Science", "DS", "۲ سال", "€15,000", ("EUR", 15000, None),
    "کارشناسی CS/ریاضی/آمار؛ رقابتی", "6.5 (W 6.0)", "123", "Reach", "دانشکدهٔ علوم؛ ظرفیت محدود",
    "https://www.helsinki.fi/en/degree-programmes/data-science-masters-programme")

# ===== کانادا بدون کبک (CAD) — کشور هشتم (نسخهٔ ۳.۱۲، ۲۹ سپتامبر ۲۰۲۶) =====
# به خواست شما کبک (McGill، Concordia، Montréal) حذف شد: PR کبک فرانسه می‌خواهد. UBC/SFU نیامده‌اند: کف رسمی ایران ۱۶/۲۰ روی کل دوره (معدل کل شما ۱۵.۷۷).
# Waterloo (کف ۷۸٪ + شهریهٔ رسمی پیدا نشد)، Dalhousie/Ontario Tech/Regina (جدول شهریهٔ رسمی از ایران بارگذاری نشد) و Queen's/McMaster/Western (Reach، بدون رقم رسمی) عمداً نیامده‌اند.
# شهریه‌ها: رسمی 2026/27 مگر جایی که «≈» آمده. «پایان‌نامه‌ای» = استاد راهنما + معمولاً TA/RA؛ «درسی» = بدون فاندینگ.
add("کانادا", "Memorial University of Newfoundland (MUN)", "StJohns", "MSc Computer Science — thesis route", "SE", "۲ سال", "CAD 1,611 × ۶ ترم = CAD 9,666 برای کل دوره (Master's Payment Plan A، رسمی 2026/27) + ≈ CAD 1,300 هزینه‌های اجباری/سال", ("CAD", 4833, None),
    "کارشناسی ۴ ساله با «Second Class» (B ≈ ۷۵٪) — معادل ایرانی رسمی ندارد (معمولاً ۱۴–۱۵/۲۰)؛ برای مسیر پایان‌نامه‌ای استاد راهنما لازم است", "6.5 (هر بخش ≥ 6.0)", "≈ 800+ (QS 2026)", "Target", "ارزان‌ترین ارشد کل جدول (کل شهریه ≈ $6,800)؛ پرداخت در ۶ قسط؛ MCP (بیمهٔ استانی) رایگان با مجوز ≥ ۱۲ ماه؛ شهر کوچک و دور، بازار IT کوچک (Verafin/Nasdaq)؛ مهلت پاییز ≈ فوریه ۲۰۲۷ (چک شود)",
    "https://www.mun.ca/sgs/media/production/memorial/academic/school-of-graduate-studies/school-of-graduate-studies/media-library/MinimumExpense.pdf")
add("کانادا", "Memorial University of Newfoundland (MUN)", "StJohns", "MSc Computer Science — non-thesis (course) route", "SE", "۲ سال", "CAD 2,600 × ۶ ترم = CAD 15,600 برای کل دوره (رسمی 2026/27، تمام‌وقت) + ≈ CAD 1,300 هزینه‌های اجباری/سال", ("CAD", 7800, None),
    "همان کف B؛ بدون استاد راهنما → پذیرش آسان‌تر؛ بدون TA/RA تضمینی", "6.5 (هر بخش ≥ 6.0)", "≈ 800+ (QS 2026)", "Safe/Target", "ارزان‌ترین مسیر «درسی» ۸ کشور؛ همان مدرک MSc؛ PGWP ۳ ساله؛ خوابگاه Paton College CAD 5,255/ترم با غذا",
    "https://www.mun.ca/sgs/media/production/memorial/academic/school-of-graduate-studies/school-of-graduate-studies/media-library/MinimumExpense.pdf")
add("کانادا", "Memorial University of Newfoundland (MUN)", "StJohns", "Master of Artificial Intelligence (MAI، درسی)", "AI", "۱۶ ماه (۱.۳۳ سال)", "Payment Plan D: CAD 2,416.50 × ۴ + هزینهٔ ویژهٔ CAD 20,282 = CAD 29,948 برای کل دوره (رسمی 2026/27)", ("CAD", 22460, None),
    "کارشناسی CS/مهندسی با B؛ درسی (بدون استاد راهنما)", "6.5 (هر بخش ≥ 6.0)", "≈ 800+ (QS 2026)", "Target", "تنها ارشد AI کانادا که در بودجهٔ $40k جا می‌شود (شهریه ≈ $21.1k + تمکن $16.5k = $37.6k ✅)؛ ۱۶ ماه پیوسته؛ MASc Software Engineering همین دانشگاه هم همین قیمت است",
    "https://www.mun.ca/sgs/media/production/memorial/academic/school-of-graduate-studies/school-of-graduate-studies/media-library/MinimumExpense.pdf")
add("کانادا", "University of Manitoba", "Winnipeg", "MSc Computer Science (thesis یا course-based)", "SE", "۲ سال", "CAD 6,909.96 × ۲ ترم سال اول = CAD 13,820 + هزینهٔ ادامه CAD 675 × ۴ ترم = ≈ CAD 16,500 برای کل دوره (رسمی 2025/26؛ 2026/27 ≈ +۳–۴٪)", ("CAD", 8260, None),
    "کف رسمی ایران: ۱۵/۲۰ در دو سال آخر (شما ۱۶.۹۲ ✓) + کارشناسی ۴ ساله؛ پایان‌نامه‌ای: استاد راهنما", "6.5 (هر بخش ≥ 6.0)", "≈ 690 (QS 2026)", "Target", "تنها دانشگاه بزرگ کانادا با کف ایرانی رسمیِ «دو سال آخر» — با ۱۶.۹۲ واجد شرایطید؛ MPNP مسیر «Graduate Internship» (ارشد + کارآموزی Mitacs → PR بدون پیشنهاد کار)؛ بیمهٔ استانی برای دانشجوی بین‌المللی نیست (بیمهٔ دانشگاه ≈ CAD 700/سال)؛ مهلت ≈ ژانویه ۲۰۲۷ (چک شود)",
    "https://umanitoba.ca/registrar/tuition-fees/2025-2026-graduate-tuition-and-fees-archive")
add("کانادا", "University of Saskatchewan (USask)", "Saskatoon", "MSc Computer Science (thesis)", "SE", "۲ سال", "CAD 4,279 × ۳ ترم = CAD 12,837/سال (رسمی 2026/27، نرخ استاندارد پایان‌نامه‌ای) + ≈ CAD 1,100 هزینه‌های اجباری/سال", ("CAD", 12837, None),
    "کارشناسی ۴ ساله با ≥ ۷۰٪ (B) در دو سال آخر — معادل ایرانی رسمی نیافتم (≈ ۱۵/۲۰)؛ استاد راهنما لازم", "6.5 (هر بخش ≥ 6.0)", "≈ 350 (QS 2026)", "Target", "بیمهٔ استانی رایگان؛ خوابگاه Graduate House CAD 1,212–1,504؛ Seager Wheeler CAD 673/ماه؛ حداقل دستمزد CAD 15.70 (اکتبر ۲۰۲۶)؛ مهلت ≈ ژانویه–فوریه ۲۰۲۷ (چک شود)",
    "https://grad.usask.ca/funding/tuition.php")
add("کانادا", "University of Alberta (UAlberta)", "Edmonton", "MSc Computing Science — thesis-based", "SE", "۲ سال", "برنامه‌محور: CAD 10,518.72/سال برای ورودی ۲۰۲۶ (رسمی، ثابت‌شده) و ۵.۵٪ کاهش برای ورودی پاییز ۲۰۲۷ ≈ CAD 9,940/سال + ≈ CAD 1,800 هزینه‌های اجباری/سال", ("CAD", 9940, None),
    "GPA ≥ 3.0 روی ۶۰ واحد آخر (رسمی FGSR)؛ گروه CS عملاً ≈ 3.5 = ≈ ۱۷/۲۰ ایران (منبع ثانویه) → دو سال آخر شما ۱۶.۹۲ مرزی؛ استاد راهنما لازم", "6.5 (هر بخش ≥ 6.0؛ گروه CS ممکن است 7 بخواهد — چک شود)", "≈ 94 (QS 2026)", "Target/Reach", "بهترین برند بین گزینه‌های داخل بودجه (Amii، RL/ML)؛ «بیشتر دانشجویان پایان‌نامه‌ای با TA/RA تضمینی ۵ ترم» (FAQ رسمی)؛ AHCIP (بیمهٔ استانی) رایگان؛ بدون مالیات فروش استانی؛ مهلت ۱۵ دسامبر ۲۰۲۶ (فاندینگ) / ۱۵ ژانویه ۲۰۲۷",
    "https://www.ualberta.ca/en/graduate-studies/fees-funding/tuition-fees/instructional-fees-international.html")
add("کانادا", "University of Alberta (UAlberta)", "Edmonton", "MSc Computing Science — course-based", "SE", "۲ سال", "CAD 826.36 به ازای هر واحد (ورودی ۲۰۲۶) × ≈ ۳۰ واحد ≈ CAD 24,800؛ ورودی ۲۰۲۷ +۵.۵٪ ≈ CAD 26,150 برای کل دوره (≈ CAD 13,100/سال) + ≈ CAD 1,800 هزینه‌های اجباری/سال", ("CAD", 13077, None),
    "همان کف 3.0 روی ۶۰ واحد آخر؛ بدون استاد راهنما → پذیرش آسان‌تر از پایان‌نامه‌ای؛ بدون TA/RA", "6.5 (هر بخش ≥ 6.0؛ چک شود)", "≈ 94 (QS 2026)", "Target", "مسیر «درسی» یک دانشگاه Top-100 داخل بودجه (شهریه ≈ $18.4k + تمکن $16.5k = $35k ✅)؛ تعداد واحد دقیق را با گروه چک کنید؛ مهلت ۱۵ ژانویه ۲۰۲۷",
    "https://www.ualberta.ca/en/graduate-studies/fees-funding/tuition-fees/instructional-fees-international.html")
add("کانادا", "University of Calgary (UCalgary)", "Calgary", "MSc Computer Science — thesis-based", "SE", "۲ سال", "CAD 2,858.55 × ۳ ترم = CAD 8,575.65/سال (رسمی 2026/27) + ≈ CAD 1,000 هزینه‌های عمومی/سال؛ فاندینگ تضمینی ارشد پایان‌نامه‌ای بین‌المللی CAD 25,455/سال × ۲ سال (رسمی، ورودی‌های از ژانویه ۲۰۲۶)", ("CAD", 8576, None),
    "GPA ≥ 3.0 روی نیمهٔ دوم کارشناسی (رسمی G.A.1) — معادل ایرانی رسمی ندارد (۱۶.۹۲ دو سال آخر ≈ B+)؛ استاد راهنما لازم", "6.5 (هر بخش ≥ 6.0)", "≈ 180 (QS 2026)", "Target/Reach", "تنها گزینهٔ ۸ کشور با «حداقل فاندینگ تضمینی» بالاتر از شهریه + بخشی از زندگی (CAD 25,455 − شهریه ≈ CAD 16,900/سال ≈ CAD 1,400/ماه)؛ AAIP Accelerated Tech Pathway برای PR؛ AHCIP رایگان؛ مهلت ≈ اول تا اواسط ژانویه ۲۰۲۷ (چک شود)",
    "https://calendar.ucalgary.ca/pages/bdf3d650a14247e4912def1671b7ba09")
add("کانادا", "University of Victoria (UVic)", "Victoria", "MSc Computer Science (thesis)", "SE", "۲ سال", "≈ CAD 2,746 × ۳ قسط = ≈ CAD 8,240/سال (رقم 2025/26 در FAQ رسمی دانشکده؛ جدول 2026/27 چک شود) + ≈ CAD 1,200 هزینه‌های اجباری/سال + MSP CAD 75/ماه", ("CAD", 8238, None),
    "B+ (≈ ۷۷٪) در دو سال آخر — معادل ایرانی رسمی نیافتم (احتمالاً ۱۶/۲۰ روی دو سال آخر)؛ استاد راهنما لازم", "6.5 (هر بخش ≥ 6.0)", "≈ 350 (QS 2026)", "Target/Reach", "BC PNP «International Post-Graduate» (ارشد STEM در BC → PR بدون پیشنهاد کار)؛ شهر گران و بازار کوچک (ونکوور ۹۰ دقیقه)؛ حداقل دستمزد BC CAD 18.25؛ مهلت ≈ ۱۵ دسامبر ۲۰۲۶ برای بین‌المللی‌ها (چک شود)",
    "https://www.uvic.ca/graduate/programs/graduate-programs/assets/_common/tuition-fees-degree-intl-meng.php")
add("کانادا", "Carleton University", "Ottawa", "Master of Computer Science (MCS، thesis؛ گرایش Data Science, Analytics & AI هم هست)", "SE", "۲ سال", "≈ CAD 26,641/سال (2025/26، پایان‌نامه‌ای — منبع ثانویه)؛ رسمی پاییز ۲۰۲۶ برای مسیر غیرپایان‌نامه‌ای: CAD 9,668.99/ترم × ۳ = CAD 29,007/سال + ≈ CAD 2,500 هزینه‌های اجباری (UHIP، U-Pass)", ("CAD", 26641, 29007),
    "B+ (۷۷٪) در دو سال آخر؛ پایان‌نامه‌ای با استاد راهنما و معمولاً TA/RA ≈ CAD 18–24k/سال", "6.5 (هر بخش ≥ 6.0)", "≈ 560 (QS 2026)", "Target", "اتاوا: دولت فدرال + Shopify + دفاعی؛ OINP Masters Graduate برای PR؛ بدون فاندینگ خارج بودجه (شهریه ≈ $37.5k)؛ فقط با نامهٔ فاندینگ داخل بودجه؛ مهلت ≈ ۱ فوریه ۲۰۲۷ (چک شود)",
    "https://carleton.ca/studentaccounts/tuition-fees/grad-per-cred_f26w27_intl/")
add("کانادا", "University of Windsor", "Windsor", "Master of Applied Computing (MAC، درسی، با co-op اختیاری)", "SE", "۱۶ ماه (۱.۳۳ سال)", "≈ CAD 30,300–30,900/سال ≈ CAD 40–41k برای ۱۶ ماه (منابع ثانویه ۲۰۲۵–۲۶؛ صفحهٔ رسمی شهریه از دسترس خارج شده — با دانشگاه چک شود) + بیمه/کارگاه ≈ CAD 3,000", ("CAD", 30600, None),
    "کارشناسی ۴ ساله CS/مرتبط با ≥ ۷۰٪ (B) — مسیر کلاسیک ایرانی‌ها؛ درسی، بدون استاد راهنما", "7.0 (هر بخش ≥ 6.5) — چک شود", "≈ 650 (QS 2026)", "Safe", "امن‌ترین پذیرش کانادا برای معدل ۱۵.۷۷، ولی گام ۱ ❌ (≈ $28.7k شهریه + $16.5k تمکن = $45k)؛ co-op ۴–۸ ماه با حقوق؛ ۴۵ دقیقه تا دیترویت؛ OINP Masters Graduate",
    "https://www.uwindsor.ca/finance/fee-estimator")
add("کانادا", "University of Toronto", "Toronto", "MScAC — Master of Science in Applied Computing (۱۶ ماه، ۸ ماه کارآموزی با حقوق)", "AI", "۱۶ ماه (۱.۳۳ سال)", "کل شهریه و هزینه‌ها برای ۱۶ ماه: ≈ CAD 90,050 برای بین‌المللی‌ها (رسمی، ورودی سپتامبر ۲۰۲۶؛ شامل CAD 2,200 پیش‌برنامه)", ("CAD", 67540, None),
    "کف SGS برای ایران ۱۵/۲۰ ولی MScAC عملاً A− = ۱۷/۲۰ روی سال‌های آخر (سال آخر شما ۱۷.۰۳، دو سال آخر ۱۶.۹۲ → مرزی)؛ مصاحبه؛ رقابت شدید", "7.0 (W/S ≥ 6.5)", "≈ 29 (QS 2026)", "Reach", "بهترین برند و بازار (تورنتو)؛ کارآموزی ۸ ماهه ≈ CAD 40–55k حقوق دارد ولی بعد از پرداخت شهریه؛ گام ۱ ❌ با فاصلهٔ زیاد ($63.5k شهریه)؛ مهلت ≈ ۱ دسامبر ۲۰۲۶ (چک شود)",
    "https://mscac.utoronto.ca/apply/")
add("کانادا", "Memorial University of Newfoundland (MUN)", "StJohns", "MASc Software Engineering (درسی، ۱۶ ماه)", "SE", "۱۶ ماه (۱.۳۳ سال)", "Payment Plan D: CAD 2,416.50 × ۴ + هزینهٔ ویژهٔ CAD 20,282 = CAD 29,948 برای کل دوره (رسمی 2026/27)", ("CAD", 22460, None),
    "کارشناسی مهندسی/CS با B؛ درسی", "6.5 (هر بخش ≥ 6.0)", "≈ 800+ (QS 2026)", "Target", "همان ساختار و قیمت MAI؛ برای کسی که مهندسی نرم‌افزار می‌خواهد نه AI؛ داخل بودجه ($37.6k)",
    "https://www.mun.ca/sgs/media/production/memorial/academic/school-of-graduate-studies/school-of-graduate-studies/media-library/MinimumExpense.pdf")

PROGRAMS = P


def fee_usd(cur, lo, hi):
    """Annual tuition in USD, rounded to the nearest $100."""
    r = RATES[cur]
    def f(x):
        return int(round(x * r / 100.0)) * 100
    if hi is None:
        return f"${f(lo):,}"
    return f"${f(lo):,}–{f(hi):,}"
