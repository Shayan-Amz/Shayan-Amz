# -*- coding: utf-8 -*-
"""
Builds Table_final.xlsx — the clean, corrected comparison table (6 countries, M.Sc. Computer Science).
All figures verified against official/primary sources on 2026-09-27 (see sheet "منابع").
Incorporates the valid points of both audits (mine + Review.docx).
"""
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side
from openpyxl.utils import get_column_letter
from catalogue_data import PROGRAMS, FIELDS, FIELD_ROWS, CITIES, fee_usd

FX = "نرخ تبدیل ۲۷ سپتامبر ۲۰۲۶: €1 = $1.14 · £1 = $1.325 · $1 ≈ SEK 9.9 · $1 ≈ DKK 6.55"

HEAD = ["ردیف", "معیار", "آلمان 🇩🇪", "هلند 🇳🇱", "سوئد 🇸🇪", "دانمارک 🇩🇰", "ایرلند 🇮🇪", "انگلستان (England) 🇬🇧", "منبع اصلی"]

ROWS = [
 ["۱", "برنامه‌های هدف واقع‌بینانه (Safe / Target / Reach) — با معدل ≈ ۱۵.۷ از ۲۰ و IELTS ≈ 7",
  "Stuttgart (اشتوتگارت) – MSc Computer Science (انگلیسی، بدون NC، IELTS 7) → Target\nFAU (Erlangen/Nürnberg) – MSc Artificial Intelligence (انگلیسی، B2؛ ⚠️ از تابستان ۲۰۲۷ شهریهٔ €4,000/ترم برای غیر-EU) → Target\nTU Darmstadt (دارمشتات) – MSc Computer Science (انگلیسی، IELTS 7) → Target/Reach\nTU Dresden (درسدن) – MSc Computer Science (انگلیسی، IELTS 7، ارزیابی استعداد) → Reach\nSafe: RPTU Kaiserslautern، Passau، Saarland (Saarbrücken)، TU Chemnitz، OVGU Magdeburg",
  "Twente (Enschede) – MSc Computer Science (حداقل رسمی برای مدرک ایرانی: ۱۵/۲۰) → Target\nRadboud (Nijmegen) – MSc Computing Science → Target\n(هر دو روی واحدهای ریاضی/الگوریتم/CS نظری در ریزنمرات حساس‌اند)",
  "Linköping (لینشوپینگ) – MSc Computer Science (گزینش بر اساس گروه معدل) → Target\nBTH – MSc Software Engineering 120 واحدی، Karlskrona (≥ ۹۰ واحد CS/SE در کارشناسی) → Safe/Target\nHalmstad (هالمستاد) – MSc Information Technology 120 واحدی → Safe\n⚠️ برنامه ۶۰ واحدی BTH از راه دور/نیمه‌وقت است و برای ویزا کاربرد ندارد",
  "AAU (Aalborg) – MSc Computer Science (IT) (انگلیسی؛ نه برنامه Computer Science دانمارکی‌زبان) → Target\nSDU (Odense) – MSc Computer Science → Target\n(AAU رسماً حداقل ۱۵۰ ECTS دروس مرتبط با CS می‌خواهد و از ۲۰۲۷ سابقهٔ کار را هم در رتبه‌بندی حساب می‌کند؛ SDU هم واحدهای CS ریزنمرات را ارزیابی می‌کند)",
  "TU Dublin (Dublin) – MSc Computing (Advanced Software Development) → Safe\nMaynooth (۲۵ km از Dublin) – MSc (CS) Software Engineering، ۱ ساله → Safe/Target\nUL (Limerick) – MSc Software Engineering → Target\n(شرط 2.2 honours ≈ معدل شما OK)",
  "Teesside (Middlesbrough) – MSc Computer Science (2:2، IELTS 6.0) → Safe\nNorthumbria (Newcastle) – MSc Advanced Computer Science (2:2 در رشته کامپیوتری) → Safe\nEssex (Colchester) – MSc Advanced Computer Science (2:2؛ Computer Engineering پذیرفته می‌شود) → Safe/Target\nBrunel (London) – MSc AI / Data Science (2:2) → Safe/Target\nLeicester (لستر) – MSc Advanced Computer Science (2:1؛ سابقه کار مرتبط جبران می‌کند) → Target\nYork (یورک) – MSc Advanced Computer Science (2:2 با پیش‌زمینه قوی، IELTS 6.5) → Reach\nفقط انگلستان — Strathclyde (اسکاتلند) و Swansea (ولز) حذف شدند",
  "سایت برنامه‌ها؛ utwente.nl (Iran 15/20)؛ bth.se؛ «۷۵٪ قبولی» جدول اول حذف شد — چنین آماری وجود ندارد.\n➜ فهرست کامل ≈۱۰۰ برنامه در ۸ حوزه (AI، امنیت، داده، نرم‌افزار، ابری، نهفته/رباتیک، HCI، بازی) با شهریه و شرط ورود: شیت «برنامه‌ها»؛ مقایسهٔ بازار کار حوزه‌ها: شیت «حوزه‌ها و بازار کار»"],

 ["۲", "رتبه QS World University Rankings 2027 (ژوئن ۲۰۲۶)",
  "TU Dresden 185 · FAU 218 · TU Darmstadt 250 · Stuttgart 318",
  "Twente =223 · Radboud =283",
  "Linköping 308 · BTH و Halmstad در QS رتبه ندارند",
  "SDU =283 · Aalborg =329",
  "UL 388 · Maynooth 721–730 · TU Dublin 791–800",
  "Newcastle 149 · York =158 · Leicester =314 · Brunel 353 · Essex =438 · Northumbria =528 · Teesside در فهرست اصلی QS نیست (THE 601–800)",
  "topuniversities.com (QS WUR 2027)؛ utwente.nl/rankings"],

 ["۳", "طول دوره ارشد",
  "۲ سال (120 ECTS)", "۲ سال (120 ECTS)",
  "۲ سال (120 ECTS) — گزینه یک‌ساله حضوری معتبر ندارد",
  "۲ سال (120 ECTS)", "۱ سال (90 ECTS، ۱۲ ماه)", "۱ سال (۱۲ ماه)",
  "سایت برنامه‌ها"],

 ["۴", "شهریه سالانه رسمی، بدون بورس (سال تحصیلی 2026/27، ارز محلی)",
  "€0 + سهم ترمی €150–400 (≈ €300–800 در سال)\nStuttgart: €1,500 در ترم = €3,000 در سال (بادن-وورتمبرگ)\n⚠️ FAU: از ترم تابستان ۲۰۲۷ برای ورودی‌های جدید غیر-EU €4,000 در ترم (AI/CS) = €8,000 در سال (BayHIG §13)؛ Passau فعلاً بدون شهریه",
  "Twente: €21,700\nRadboud: €19,714 (2026/27، رسمی)",
  "Linköping: SEK 166,000\nHalmstad: ≈ SEK 151,000\nBTH: SEK 140,000 (70,000 در ترم)",
  "AAU: ≈ €14,910 (2025/26: 7,455 در ترم؛ نرخ ۲۰۲۶ هنوز روی سایت AAU نیست)\nSDU: €17,300 (نرخ رسمی برای ورودی سپتامبر ۲۰۲۶ به بعد — رقم قدیمی €13,900 دیگر معتبر نیست)",
  "TU Dublin: ≈ €15,000–15,500\nMaynooth: €18,000 (2025/26) → ≈ €18,500\nUL: €20,800",
  "Teesside: £17,000\nNorthumbria: £21,500\nLeicester: £24,250\nEssex: £24,675\nBrunel: £24,795\nYork: £32,900 (Newcastle ≈ £31,700)\nکف قیمت انگلستان: Chester £15,500 (بدون رتبه). بورس‌ها (مثلاً Brunel تا £6,000) جدا حساب شوند، تضمینی نیستند",
  "utwente.nl؛ liu.se؛ bth.se؛ sdu.dk؛ studyindenmark.dk؛ ul.ie؛ maynoothuniversity.ie؛ brunel.ac.uk؛ tees.ac.uk؛ northumbria.ac.uk؛ le.ac.uk؛ essex.ac.uk؛ york.ac.uk"],

 ["۵", "شهریه سالانه به دلار",
  "$350–900 (Stuttgart ≈ $3,400؛ FAU از ۲۰۲۷ ≈ $9,300)", "$22,500–24,700", "$14,100–16,800",
  "$17,000–19,700", "$17,100–23,700", "$22,500–43,600 (Teesside $22,500 · Northumbria $28,500 · Leicester/Essex/Brunel ≈ $32,100–32,900 · York $43,600)",
  FX],

 ["۶", "هزینه زندگی ماهانه واقعی دانشجو (و حداقل قانونی ویزا ۲۰۲۶)",
  "€950–1,250 (Dresden/Erlangen ارزان‌تر؛ Stuttgart/Darmstadt گران‌تر)\nحداقل حساب مسدود: €992/ماه",
  "€1,100–1,500 در Enschede/Nijmegen\nحداقل IND: €1,130.77/ماه",
  "SEK 10,700–13,000 (≈ €950–1,150)\nحداقل Migrationsverket: SEK 10,656/ماه",
  "DKK 8,000–10,000 (≈ €1,070–1,340) در Aalborg/Odense\nحداقل SIRI: DKK 7,426/ماه",
  "Dublin: €1,400–1,800 (اتاق €800–1,200)\nLimerick/Maynooth: €1,100–1,400\nحداقل رسمی ISD: €10,000 برای یک سال",
  "شمال انگلستان (Middlesbrough/Newcastle): £950–1,250\nLeicester/Colchester/York: £1,000–1,350\nLondon (Brunel): £1,400–1,800\nحداقل ویزا: £1,171 / £1,529 در ماه (× ۹)؛ از ۳۰ نوامبر ۲۰۲۶: £1,203 / £1,570",
  "make-it-in-germany.com؛ ind.nl؛ migrationsverket.se؛ nyidanmark.dk؛ irishimmigration.ie؛ gov.uk (HC 584)"],

 ["۷", "هزینه سال اول = شهریه + ۱۲ ماه زندگی (دلار)",
  "$13,000–18,000 (Stuttgart تا $20,500؛ FAU از ۲۰۲۷ تا ≈ $26,000)",
  "$37,500–45,000",
  "$27,000–32,500",
  "$31,500–38,000",
  "$32,000–48,000 (خارج از Dublin: $32,000–40,000)",
  "$38,000–65,000 (Teesside $38–42k · Northumbria $44–48k · Leicester/Essex $48–54k · Brunel/London $55–61k · York $60–65k)",
  "محاسبه از ردیف‌های ۴ و ۶؛ بدون بلیت، ویزا، بیمه، ودیعه (۱۰–۱۵٪ اضافه کنید)"],

 ["۸", "هزینه کل تا فارغ‌التحصیلی (شهریه × سال‌ها + زندگی) — مهم‌ترین عدد مالی",
  "$27,000–36,000 (۲ سال؛ Stuttgart تا $41,000؛ FAU از ۲۰۲۷ تا ≈ $53,000) — ارزان‌ترین",
  "$75,000–90,000 (۲ سال) — گران‌ترین",
  "$54,000–65,000 (۲ سال)",
  "$63,000–76,000 (۲ سال)",
  "$32,000–48,000 (۱ سال)",
  "$38,000–65,000 (۱ سال)",
  "محاسبه؛ جدول اول فقط سال اول را مقایسه کرده بود"],

 ["۹", "سازگاری با بودجه $32,000 در سال",
  "✅ کاملاً (حتی Stuttgart)",
  "❌ کسری $5,500–13,000 در هر سال",
  "✅ (Linköping دقیقاً مرزی)",
  "⚠️ مرزی؛ AAU تقریباً در بودجه، SDU کسری تا ≈ $6,000 در سال",
  "⚠️ خارج از Dublin یا با شهریه TU Dublin ✓؛ Dublin کسری",
  "❌ کسری $6,000–33,000 (کمترین: Teesside ≈ $6–10k؛ Northumbria ≈ $12–16k)",
  "محاسبه از ردیف ۷"],

 ["۱۰", "مسکن در بدو ورود",
  "خوابگاه Studierendenwerk با لیست انتظار؛ Stuttgart و Darmstadt سخت، Dresden و Erlangen آسان‌تر. بلافاصله بعد از پذیرش ثبت‌نام کنید.",
  "کمبود شدید ملی؛ ولی Twente (کمپوس) و Radboud/SSH& اتاق رزروشده برای بین‌المللی‌ها دارند — مهلت را از دست ندهید.",
  "تضمین سراسری نیست: Linköping به شهریه‌پردازها یک پیشنهاد اتاق برای سال اول می‌دهد؛ Halmstad تضمین ندارد؛ BTH تأیید نشد.",
  "دفتر اسکان بین‌المللی AAU/SDU؛ Aalborg و Odense نسبتاً در دسترس.",
  "Dublin بحرانی و بسیار گران؛ UL دهکده‌های خوابگاهی کمپوس؛ Maynooth خوابگاه کمپوس (قرعه‌کشی).",
  "معمولاً تضمین خوابگاه سال اول برای بین‌المللی‌ها اگر تا مهلت درخواست دهید.",
  "سایت دانشگاه‌ها؛ hh.se (Find Accommodation)؛ liu.se"],

 ["۱۱", "سقف قانونی کار دانشجویی",
  "۱۴۰ روز کامل یا ۲۸۰ نیم‌روز در سال (Werkstudent تا ۲۰ ساعت/هفته در ترم)",
  "۱۶ ساعت/هفته (کارفرما TWV می‌گیرد) یا تمام‌وقت در ژوئن–اوت",
  "از ۱۱ ژوئن ۲۰۲۶: حداکثر ۱۵ ساعت/هفته در ترم؛ ژوئن–اوت بدون سقف. تخلف = لغو اقامت. + حداقل پیشرفت تحصیلی ۳۷.۵ واحد سال اول / ۴۵ واحد بعد",
  "۹۰ ساعت/ماه (سپتامبر–مه) + تمام‌وقت ژوئن–اوت",
  "۲۰ ساعت/هفته؛ ۴۰ ساعت/هفته در ژوئن–سپتامبر و ۱۵ دسامبر–۱۵ ژانویه",
  "۲۰ ساعت/هفته در ترم؛ تمام‌وقت در تعطیلات",
  "make-it-in-germany.com؛ ind.nl؛ migrationsverket.se (خبر ۲۵ مه ۲۰۲۶)؛ nyidanmark.dk؛ irishimmigration.ie؛ gov.uk"],

 ["۱۲", "درآمد واقع‌بینانه کار حین تحصیل (ناخالص، ماهانه)",
  "€1,000–1,600 (Werkstudent فنی €15–20/ساعت؛ برای رشته شما فراوان)",
  "تا ≈ €1,000 (۱۶ ساعت × €14.71)؛ یافتن کارفرمای TWV‌گیر سخت",
  "€300–800 (سقف ۱۵ ساعت؛ کار برای غیرسوئدی‌زبان کمیاب)",
  "DKK 8,000–12,000 (€1,070–1,600) اگر کار پیدا شود؛ اکثر کارهای خدماتی دانمارکی می‌خواهند",
  "تا ≈ €1,200 (۲۰ ساعت × €14.15)",
  "تا ≈ £1,100 (۲۰ ساعت × £12.71)",
  "حداقل دستمزدهای ۲۰۲۶؛ برآورد. درآمد دانشجویی را در تأمین مالی ویزا حساب نکنید."],

 ["۱۳", "زبان محیط کار فنی (IT)",
  "انگلیسی در استارتاپ‌ها/شرکت‌های بزرگ (Berlin، Munich، Hamburg) کافی؛ اکثر آگهی‌های IT آلمانی B2 می‌خواهند → بدون آلمانی حدود نیمی از بازار بسته است.",
  "انگلیسی در tech رایج و کافی؛ نه ۱۰۰٪.",
  "انگلیسی در tech رایج (Stockholm، Göteborg)؛ بازار ۲۰۲۴–۲۶ ضعیف (بیکاری ≈ ۹٪).",
  "انگلیسی برای بخشی از نقش‌های IT در Copenhagen/Aarhus کافی؛ برای اکثر نقش‌ها دانمارکی B1–B2 ترجیح دارد؛ در Aalborg/Odense سخت‌تر.",
  "۱۰۰٪ انگلیسی؛ دفاتر اروپایی Google، Meta، Microsoft، Amazon، Stripe…",
  "۱۰۰٪ انگلیسی؛ بازار جونیور ۲۰۲۵–۲۶ بسیار رقابتی.",
  "workindenmark.dk؛ آگهی‌های StepStone/LinkedIn؛ ارزیابی"],

 ["۱۴", "زبان برای امور اداری و زندگی روزمره",
  "قانوناً برای تحصیل لازم نیست؛ عملاً A2–B1 (اداره اتباع، اجاره، بیمه، مالیات).",
  "انگلیسی کافی؛ نامه‌های رسمی هلندی.",
  "انگلیسی کافی.",
  "انگلیسی روزمره کافی؛ سامانه‌ها و نامه‌ها دانمارکی.",
  "انگلیسی.", "انگلیسی.",
  "تجربه عمومی؛ ارزیابی"],

 ["۱۵", "مجوز اقامت پس از تحصیل برای جست‌وجوی کار",
  "۱۸ ماه (§20 AufenthG) — هر کاری مجاز",
  "۱۲ ماه (zoekjaar) — تا ۳ سال بعد از مدرک قابل درخواست؛ €254",
  "۱۲ ماه — با اثبات تمکن SEK 10,656/ماه برای کل دوره",
  "۳ سال، خودکار همراه مجوز تحصیلی برای ارشد state-approved (AAU/SDU) — تا گرفتن «مجوز کار نامحدود» فقط ۹۰ ساعت/ماه",
  "۲۴ ماه Stamp 1G (۱۲ + ۱۲) — کار تمام‌وقت بدون مجوز",
  "۱۸ ماه Graduate visa برای درخواست‌های از ۱ ژانویه ۲۰۲۷ — £937 + IHS £1,035/سال",
  "make-it-in-germany.com؛ ind.nl؛ migrationsverket.se؛ nyidanmark.dk؛ irishimmigration.ie؛ gov.uk (Statement of Changes ۱۴ اکتبر ۲۰۲۵)"],

 ["۱۶", "حداقل حقوق برای ویزای کار (سطوح ۲۰۲۶)",
  "بلوکارت: €50,700 عمومی / €45,934.20 برای IT و تازه‌فارغ‌التحصیلان (تا ۳ سال بعد از مدرک)\nمجوز کار §18b برای فارغ‌التحصیلان آلمان: بدون کف ثابت",
  "HSM کاهش‌یافته برای فارغ‌التحصیلان هلند (تا ۳ سال): €3,122/ماه بدون حق تعطیلات ≈ €40,500/سال\nزیر ۳۰ سال عادی: €4,357/ماه",
  "SEK 34,470/ماه (۹۰٪ میانه؛ از ۱۶ ژوئن ۲۰۲۶)\nفارغ‌التحصیلان سوئد که از داخل درخواست دهند: ۷۵٪ = SEK 28,725/ماه\nهر ژوئن به‌روز می‌شود",
  "Positive List (مشاغل IT): کف ثابت ندارد (حقوق مطابق استاندارد دانمارکی)\nPay Limit: DKK 552,000 · Supplementary: DKK 446,000",
  "CSEP: €40,904 (از ۱ مارس ۲۰۲۶؛ پلکانی تا ۲۰۳۰)\nتخفیف تا ۱۲ ماه بعد از مدرک: €36,848\nGEP: €36,605",
  "Skilled Worker: بالاترینِ £41,700 و نرخ شغل؛ نرخ SOC 2134 (توسعه‌دهنده) = £54,700\nتازه‌کار (حداکثر ۴ سال): ۷۰٪ = £38,290\n+ انگلیسی B2 (از ۸ ژانویه ۲۰۲۶)",
  "make-it-in-germany.com؛ ind.nl؛ migrationsverket.se؛ nyidanmark.dk؛ enterprise.gov.ie (DETE)؛ gov.uk Appendix Skilled Occupations"],

 ["۱۷", "حقوق ورودی جونیور توسعه‌دهنده (ناخالص سالانه، ۲۰۲۶)",
  "€48,000–55,000 (با ارشد ≈ €55k)",
  "€40,000–50,000 (Amsterdam بالاتر)",
  "SEK 420,000–540,000 (35–45 هزار در ماه)",
  "DKK 500,000–540,000 (IDA 2026: تازه‌فارغ‌التحصیل ≈ DKK 43,800/ماه با بازنشستگی)",
  "€35,000–45,000 (میانه Dublin ≈ €38k؛ Big Tech €50k+)",
  "£28,000–35,000 خارج لندن (Manchester/Leeds/Newcastle)؛ London £32,000–45,000 — اغلب زیر کف اسپانسری £38,290",
  "StepStone؛ Glassdoor؛ IDA؛ Reed — برآورد بازار، نه آمار رسمی"],

 ["۱۸", "خالص ماهانه تقریبی (بعد از مالیات)",
  "€2,700–3,000", "€2,700–3,100 (بدون قاعده ۳۰٪)", "€2,500–2,900 (SEK 29–33 هزار)",
  "€3,300–3,700 (DKK 25–27.5 هزار)", "€2,600–3,000", "£2,000–2,500",
  "ماشین‌حساب‌های مالیاتی ۲۰۲۶ (کلاس مالیاتی مجرد)"],

 ["۱۹", "پس‌انداز ماهانه تخمینی جونیور (خالص − هزینه زندگی یک نفر شاغل)",
  "€1,000–1,500", "€700–1,200", "€900–1,400", "€1,100–1,600",
  "Dublin €400–1,000 · Limerick €800–1,300", "£400–900",
  "برآورد؛ هزینه زندگی شاغل: DE €1,400–1,700 · NL €1,700–2,100 · SE €1,300–1,600 · DK €1,900–2,300 · IE €1,800–2,300 · UK £1,300–1,700"],

 ["۲۰", "اقامت دائم (PR) — زمان و شرط اصلی",
  "۲ سال کار برای فارغ‌التحصیل آلمان با B1 (§18c)؛ بلوکارت: ۲۱ ماه با B1 / ۲۷ ماه با A1",
  "۵ سال اقامت قانونی (سال‌های تحصیل نصف حساب می‌شود) + inburgering",
  "۴ سال مجوز کار در ۷ سال اخیر + خودکفایی (تحصیل حساب نمی‌شود)",
  "۸ سال (یا ۴ سال با هر ۴ شرط تکمیلی) + ۳.۵ سال کار تمام‌وقت در ۴ سال اخیر",
  "۲ سال CSEP → Stamp 4 (کار آزاد؛ PR نیست)؛ اقامت بلندمدت: ۵ سال قابل‌احتساب (Stamp 2 دانشجویی حساب نمی‌شود)",
  "فعلاً ۵ سال Skilled Worker (Graduate visa حساب نمی‌شود)؛ طرح Earned Settlement با پایه ۱۰ سال در دستور کار دولت (تا سپتامبر ۲۰۲۶ قانون نشده)",
  "make-it-in-germany.com؛ ind.nl؛ migrationsverket.se؛ nyidanmark.dk؛ irishimmigration.ie؛ gov.uk / Home Affairs Committee"],

 ["۲۱", "آزمون زبان محلی برای PR",
  "B1 آلمانی (A1 فقط با بلوکارت ۲۷ ماهه)",
  "A2 فعلی → B1 (تصمیم کابینه، فوریه ۲۰۲۶)",
  "هیچ (برای PR)",
  "Prøve i Dansk 2 (≈ B1) برای مسیر ۸ ساله؛ PD3 (≈ B2) برای مسیر ۴ ساله",
  "هیچ",
  "انگلیسی B2 از ۲۶ مارس ۲۰۲۷ + آزمون Life in the UK (زبان سوم نیست)",
  "BAMF؛ ind.nl؛ migrationsverket.se؛ nyidanmark.dk؛ irishimmigration.ie؛ gov.uk (HC 1691)"],

 ["۲۲", "شهروندی (جدا از PR)",
  "۵ سال + B1 + آزمون تابعیت (تحصیل حساب می‌شود)",
  "۵ سال + inburgering (A2 → B1)",
  "از ۶ ژوئن ۲۰۲۶: ۸ سال + آزمون مدنی + آزمون زبان (از اکتبر ۲۰۲۷) + کف درآمد",
  "۹ سال + PD3 + آزمون تابعیت + اشتغال ۳.۵ سال از ۴ سال",
  "۵ سال قابل‌احتساب (بدون آزمون زبان)",
  "ILR + ۱۲ ماه؛ B1/B2 + Life in the UK",
  "قوانین تابعیت ۲۰۲۶؛ migrationsverket.se؛ nyidanmark.dk؛ irishimmigration.ie"],

 ["۲۳", "فرایند ویزا برای پاسپورت ایرانی — وضعیت سپتامبر ۲۰۲۶ (بسیار متغیر)",
  "سفارت تهران در «حالت اضطراری»؛ بخش ویزا به روی مراجعان عادی بسته. TLScontact از ۱۵ ژوئیه ۲۰۲۶ لیست انتظار دانشجویی باز کرده ولی وقت نمی‌دهد. صدور ویزا: ۴۶هزار (۲۰۲۴) → ۲۳هزار (۲۰۲۵) → ≈ ۱٬۳۰۰ اوایل ۲۰۲۶. ارجاع موردی به ایروان/استانبول. حتی در شرایط عادی لیست انتظار ۶–۱۸ ماه.",
  "دانشگاه درخواست را در IND ثبت می‌کند (TEV) ✓؛ ولی سفارت هلند موقتاً به باکو منتقل شده و MVV در ایران صادر نمی‌شود.",
  "درخواست آنلاین در Migrationsverket؛ بررسی دیجیتال پاسپورت؛ سفارت تهران فعلاً بیومتریک/کارت اقامت نمی‌گیرد (ژوئیه ۲۰۲۶).",
  "«در حال حاضر امکان درخواست از ایران وجود ندارد» (سفارت دانمارک، ۲۰۲۶) — باید از SIRI بخواهید پرونده به نمایندگی دیگری در منطقه برود؛ بیومتریک ظرف ۱۴ روز.",
  "AVATS آنلاین ✓؛ کنسول افتخاری تهران فعلاً درخواست ویزا نمی‌پذیرد — محل تحویل مدارک را هنگام اقدام بررسی کنید.",
  "درخواست آنلاین gov.uk + بیومتریک در VAC؛ VFS تهران در ۲۰۲۶ متناوباً بسته/باز شده؛ می‌توان از VAC کشور ثالث اقدام کرد. «قانون ۲۸ روز» مربوط به تمکن مالی است، نه VFS.",
  "visas-de.tlscontact.com؛ netherlandsworldwide.nl؛ swedenabroad.se؛ iran.um.dk؛ ireland.ie/tehran؛ gov.uk — برنامه B: اقدام از ترکیه/ارمنستان/امارات"],

 ["۲۴", "نمره انگلیسی برنامه‌های هدف",
  "TU Darmstadt، TU Dresden، Stuttgart: C1 / IELTS 7.0 (Dresden: هر بخش ≥ B2)\nFAU (AI): B2 / IELTS 6.5",
  "IELTS 6.5 (هر بخش ≥ 6.0)",
  "IELTS 6.5 (هر بخش ≥ 5.5)",
  "IELTS 6.5",
  "IELTS 6.5 (هر بخش ≥ 6.0)",
  "IELTS 6.0–6.5",
  "سایت برنامه‌ها — IELTS معمولاً ۲ سال اعتبار دارد؛ زمان امتحان را با اقدام ۲۰۲۸ هماهنگ کنید"],

 ["۲۵", "تمکن مالی ویزا (۲۰۲۶) و نکته تحریمی",
  "حساب مسدود €11,904 (€992 × ۱۲). Fintiba ساکنان ایران را نمی‌پذیرد؛ Expatrio/Coracle را هنگام اقدام بررسی کنید. انتقال پول فقط از مسیر کشور ثالث/صرافی (۳–۶٪ هزینه).",
  "€13,569 (€1,130.77 × ۱۲) + شهریه؛ معمولاً به حساب دانشگاه واریز می‌شود.",
  "SEK 10,656 × ماه‌های مجوز (سال اول ≈ SEK 128,000) + قسط اول شهریه.",
  "پرداخت شهریه ترم اول به‌عنوان تمکن پذیرفته می‌شود (در غیر این‌صورت DKK 7,426/ماه).",
  "€10,000 + شهریه سال اول (حداقل €6,000 پرداخت‌شده)؛ ۶ ماه گردش حساب.",
  "شهریه + £1,171 × ۹ = £10,539 خارج لندن / £13,761 لندن؛ از ۳۰ نوامبر ۲۰۲۶: £10,827 / £14,130؛ ۲۸ روز متوالی در حساب؛ + ویزای دانشجویی £524 + IHS با نرخ دانشجویی £776/سال (برای ۱۶ ماه اقامت ≈ £1,164).",
  "make-it-in-germany.com؛ ind.nl؛ migrationsverket.se؛ nyidanmark.dk؛ irishimmigration.ie؛ gov.uk (HC 584). افتتاح حساب بانکی برای ایرانی‌ها در همه‌جا کندتر است (آلمان و هلند بیشترین گزارش مشکل)."],

 ["۲۶", "بازار کار برای جونیورِ فقط‌انگلیسی‌زبان (ارزیابی، ۱–۵ ستاره)",
  "⭐⭐⭐ تقاضا و حقوق بالا؛ بدون آلمانی نیمی از بازار بسته",
  "⭐⭐⭐⭐ انگلیسی‌دوست‌ترین بازار قاره؛ کف HSM فارغ‌التحصیل دست‌یافتنی",
  "⭐⭐ بازار ۲۰۲۴–۲۶ ضعیف؛ شبکه محلی مهم",
  "⭐⭐ بدون دانمارکی محدود؛ خارج از Copenhagen سخت",
  "⭐⭐⭐⭐ هاب فناوری اروپا؛ ۲ سال Stamp 1G؛ رقابت جونیور زیاد ولی در باز",
  "⭐⭐ بازار جونیور اشباع؛ اسپانسری £38,290+ برای جونیور نادر؛ بعد از ۱۸ ماه باید ویزای کار داشت",
  "ارزیابی بر اساس ردیف‌های ۱۳، ۱۵، ۱۶، ۱۷"],

 ["۲۷", "جهت‌گیری سیاست‌های مهاجرتی ۲۰۲۵–۲۶ (ریسک تغییر تا ۲۰۲۸)",
  "متوسط: قوانین کار پایدار؛ تابعیت ۳ ساله حذف شد",
  "متوسط: B1 برای PR/تابعیت؛ WIB فقط کارشناسی انگلیسی را هدف گرفته (ارشد امن)",
  "بالا: شهروندی ۸ سال، کف حقوق ۹۰٪ میانه، سقف کار ۱۵ ساعت، تبدیل اقامت تحصیلی به کاری فقط بعد از ≥ ۲ ترم",
  "متوسط–بالا: سخت‌گیرانه ولی پایدار",
  "پایین–متوسط: افزایش پلکانی کف حقوق تا ۲۰۳۰",
  "بسیار بالا: Graduate visa ۱۸ ماه، B2، طرح PR ۱۰ ساله، عوارض £925/دانشجو/سال از اوت ۲۰۲۸ فقط برای دانشگاه‌های انگلستان — یعنی همهٔ گزینه‌های شما (ورودی ۲۰۲۸)؛ احتمالاً به شهریه اضافه می‌شود",
  "قوانین و لوایح ۲۰۲۵–۲۶"],

 ["۲۸", "امتیاز برای ۳ معیار شما (هر کدام از ۱۰): هزینه کل / زندگی و کار فقط با انگلیسی / بازار کار و حقوق",
  "10 / 4 / 8 = ۲۲",
  "2 / 8 / 8 = ۱۸",
  "6 / 8 / 5 = ۱۹",
  "4 / 6 / 6 = ۱۶",
  "7 / 10 / 8 = ۲۵",
  "5 / 10 / 4 = ۱۹",
  "وزن برابر. اگر «انگلیسی» وزن بیشتری دارد → ایرلند با فاصله؛ اگر «هزینه» وزن بیشتری دارد و B1 آلمانی را می‌پذیرید → آلمان. انگلستان با گزینه‌های ارزان شمال (Teesside/Northumbria) از ۱۷ به ۱۹ رسید (هم‌امتیاز سوئد) ولی هنوز از بودجهٔ سالانه $32k بیرون است."],
]

SUMMARY = [
 ["رتبه‌بندی هزینه کل تا فارغ‌التحصیلی", "آلمان $27–36k  <  ایرلند $32–48k  <  انگلستان $38–65k  <  سوئد $54–65k  <  دانمارک $63–76k  <  هلند $75–90k"],
 ["فقط با انگلیسی (تحصیل + کار + اداری + اقامت)", "ایرلند و انگلستان کامل؛ هلند و سوئد برای زندگی/کار خوب ولی برای اقامت دائم/تابعیت زبان می‌خواهند (هلند B1 در راه، سوئد آزمون تابعیت)؛ دانمارک و آلمان بدون زبان محلی هم بازار کار و هم PR محدود."],
 ["بازار کار و حقوق جونیور", "حقوق ناخالص: دانمارک > آلمان > هلند ≈ سوئد > ایرلند > انگلستان. دسترسی برای جونیورِ فقط‌انگلیسی: ایرلند ≈ هلند > آلمان > سوئد ≈ دانمارک ≈ انگلستان."],
 ["نتیجه با وزن برابر برای ۳ معیار", "ایرلند ۲۵ › آلمان ۲۲ › سوئد ۱۹ = انگلستان ۱۹ › هلند ۱۸ › دانمارک ۱۶.  پیشنهاد: اپلای هم‌زمان به ۲–۳ برنامه ایرلند (UL، Maynooth، TU Dublin) + ۲ برنامه آلمان (Stuttgart + یک گزینه Safe مثل Passau/Saarland؛ FAU فقط اگر شهریهٔ جدید €8,000/سال را می‌پذیرید)؛ تصمیم نهایی با پذیرش/بورس و وضعیت سفارت‌ها در ۲۰۲۸."],
 ["ریسک شماره یک", "دسترسی به سفارت‌ها از داخل ایران (ردیف ۲۳): در سپتامبر ۲۰۲۶ هیچ‌کدام از ۶ کشور خدمات عادی ویزای دانشجویی در تهران ندارند. از الان هزینه «برنامه B» (اقدام از ترکیه/ارمنستان/امارات) را در بودجه ببینید."],
 ["برنامه زمانی ورودی سپتامبر ۲۰۲۸", "تا بهار ۲۰۲۷: IELTS 7.0 (هر بخش ≥ 6.5) · تابستان ۲۰۲۷: ریزنمرات رسمی + تأییدیه‌ها + VPD uni-assist · پاییز ۲۰۲۷ تا زمستان ۲۰۲۸: اپلای (ایرلند rolling از اکتبر؛ سوئد ۱۵ ژانویه؛ هلند تا ۱ می؛ آلمان ۱۵ ژانویه–۱۵ ژوئیه؛ انگلستان rolling) · بهار ۲۰۲۸: شهریه/تمکن → خوابگاه → ویزا یا برنامه B."],
 ["تغییرات اصلی نسبت به جدول اول", "• هزینه کل دوره اضافه شد (هلند از «نیاز به تأمین سال دوم» به گران‌ترین گزینه تبدیل شد)\n• فقط انگلستان (به خواست شما): Strathclyde و Swansea حذف شدند؛ گزینه‌ها Teesside £17,000 · Northumbria £21,500 · Leicester £24,250 · Essex £24,675 · Brunel £24,795 · York £32,900؛ Graduate visa ۱۸ ماه؛ کف اسپانسری £54,700 / £38,290؛ طرح PR ۱۰ ساله؛ عوارض £925 از ۲۰۲۸ شامل همهٔ گزینه‌ها\n• کف حقوق ۲۰۲۶ همه کشورها به‌روز شد (آلمان €50,700/€45,934؛ هلند €3,122/ماه؛ سوئد SEK 34,470؛ ایرلند €40,904)\n• ایرلند: ۲ سال CSEP = Stamp 4 نه PR؛ تمکن €10,000\n• سوئد: کار دانشجویی ۱۵ ساعت/هفته (ژوئن ۲۰۲۶)؛ شهروندی ۸ سال؛ «BTH یک‌ساله» حذف شد؛ خوابگاه فقط LiU\n• QS 2027؛ شهریه‌های واقعی 2026/27؛ «۷۵٪ قبولی» حذف شد\n• «۱۰۰٪ انگلیسی» برای هلند/سوئد/دانمارک تعدیل شد؛ دانمارک PD2/PD3 تفکیک شد\n• ردیف ویزا برای وضعیت ۲۰۲۶ بازنویسی شد؛ ردیف‌های IELTS، تمکن مالی، پس‌انداز، شهروندی و امتیاز اضافه شد"],
 ["چرا «انگلستان» و نه «بریتانیا»", "به خواست شما فقط دانشگاه‌های انگلستان مقایسه شده‌اند. قوانین ویزا، کار و اقامت در کل بریتانیا یکسان است؛ سه تفاوت عملی: (۱) ارزان‌ترین گزینه‌های انگلستان (Teesside £17,000، Northumbria £21,500) از Swansea/Strathclyde ارزان‌ترند → کل دوره از $48–71k به $38–65k رسید؛ (۲) عوارض £925 به ازای هر دانشجو از اوت ۲۰۲۸ فقط دانشگاه‌های انگلستان را می‌گیرد — یعنی همهٔ گزینه‌های شما؛ (۳) بازار کار فناوری بریتانیا عملاً در انگلستان است (London، Manchester، Cambridge، Bristol، Leeds) — حذف اسکاتلند/ولز به فرصت شغلی لطمه نمی‌زند. برای شهریهٔ کمتر باید رتبهٔ پایین‌تر را بپذیرید: Teesside/Chester بدون رتبه QS، Northumbria ≈ ۵۲۸، Essex ≈ ۴۳۸؛ York (۱۵۸) و Newcastle (۱۴۹) تقریباً دوبرابر گران‌ترند."],
 ["نکته پروفایل", "معدل (۱۵.۷۷ طبق جدول اول؛ ۱۵.۷۰ طبق نقد دوم — تفاوتی در نتیجه ندارد) برای همه برنامه‌های بالا بالاتر از حداقل است. مهم‌تر از معدل، تطابق ریزنمرات با پیش‌نیازها (ریاضی، الگوریتم، CS نظری) و SOP با تکیه بر ۲ سال سابقه کار + بازی‌سازی + پروژه‌های گیت‌هاب است."],
 ["اعداد را چگونه بخوانم", "همه مبالغ سطح 2026/27 هستند؛ برای ۲۰۲۸ سالانه ۳–۵٪ (شهریه ۵–۱۰٪) اضافه کنید. " + FX],
]

SOURCES = [
 ("آلمان – EU Blue Card 2026 (€50,700 / €45,934.20)", "https://www.make-it-in-germany.com/en/visa-residence/types/eu-blue-card"),
 ("آلمان – Sperrkonto €992/ماه (2026)", "https://www.make-it-in-germany.com/en/study-training/study/financing"),
 ("آلمان – Niederlassungserlaubnis §18c (فارغ‌التحصیلان، ۲ سال، B1)", "https://www.make-it-in-germany.com/en/visa-residence/living-permanently/permanent-residence"),
 ("آلمان – Stuttgart MSc Computer Science (انگلیسی، IELTS 7، €1,500/ترم)", "https://www.uni-stuttgart.de/en/study/study-programs/Computer-Science-M.Sc./"),
 ("آلمان – FAU MSc Artificial Intelligence (انگلیسی، B2)", "https://www.ai.study.fau.eu/prospective-students/living-studying-in-germany/language-proficiency/"),
 ("آلمان – TU Darmstadt MSc Computer Science", "https://www.informatik.tu-darmstadt.de/studium_fb20/im_studium/studiengaenge_liste/computer_science_msc.en.jsp"),
 ("آلمان – TU Dresden MSc Computer Science admission", "https://tu-dresden.de/ing/informatik/studium/studienangebot/master-studiengaenge/m-sc-computer-science/admission?set_language=en"),
 ("آلمان – TLScontact Tehran (لیست انتظار دانشجویی)", "https://visas-de.tlscontact.com/en-us/country/ir/vac/irTHR2de"),
 ("آلمان – وضعیت سفارت تهران (Iran International، اوت ۲۰۲۶)", "https://www.iranintl.com/en/202608115899"),
 ("آلمان – Fintiba: ساکنان ایران پذیرفته نمی‌شوند", "https://www.simplegermany.com/best-blocked-account-germany/"),
 ("آلمان – حقوق توسعه‌دهنده (StepStone)", "https://www.stepstone.de/gehalt/Software-Entwickler-in.html"),
 ("هلند – IND مبالغ ۲۰۲۶ (HSM €3,122 / €4,357؛ دانشجو €1,130.77)", "https://ind.nl/en/required-amounts-income-requirements"),
 ("هلند – Twente شهریه 2026/27 €21,700", "https://www.utwente.nl/en/education/master/programmes/computer-science/finance/"),
 ("هلند – Twente حداقل معدل برای مدرک ایرانی (۱۵/۲۰)", "https://www.utwente.nl/en/education/master/programmes/european-studies/admission/international/"),
 ("هلند – Twente QS 2027 = 223", "https://www.utwente.nl/en/about-us/impact-ambitions/rankings/"),
 ("هلند – Radboud شهریهٔ رسمی 2026/27 غیر-EEA €19,714 (Data Science and AI؛ دانشکدهٔ علوم)", "https://www.ru.nl/en/education/masters/data-science-and-ai/tuition"),
 ("هلند – MVV در ایران (سفارت در باکو)", "https://www.netherlandsworldwide.nl/visa-the-netherlands/mvv-long-stay/apply-iran"),
 ("هلند – B1 برای PR/تابعیت (تصمیم کابینه ۲۰۲۶)", "https://thedutchdaily.nl/dutch-citizenship-b1-language-requirement-confirmed-2026/"),
 ("سوئد – قوانین جدید اقامت تحصیلی از ۱۱ ژوئن ۲۰۲۶ (۱۵ ساعت/هفته)", "https://www.migrationsverket.se/nyheter/news-archive/2026-05-25-new-rules-for-residence-permits-for-studies-in-higher-education.html"),
 ("سوئد – قوانین جدید مجوز کار از ۱ ژوئن ۲۰۲۶ (SEK 34,470)", "https://www.migrationsverket.se/nyheter/news-archive/2026-04-17-new-rules-for-work-permits-from-1-june-2026.html"),
 ("سوئد – گروه‌های معاف (فارغ‌التحصیلان ۷۵٪)", "https://eiglaw.com/sweden-publishes-exempt-occupations-for-new-salary-rule/"),
 ("سوئد – مجوز ۱۲ ماهه جست‌وجوی کار و تمکن SEK 10,656", "https://www.migrationsverket.se/en/you-want-to-extend/study/look-for-work-after-completing-your-studies-in-sweden.html"),
 ("سوئد – Linköping MSc CS شهریه SEK 332,000 (کل)", "https://liu.se/en/education/program/6mics"),
 ("سوئد – BTH MSc Software Engineering 120 credits (SEK 70,000/ترم)", "https://www.bth.se/english/education/programmes/masters-programme-in-software-engineering-120-credits"),
 ("سوئد – BTH برنامه ۶۰ واحدی (از راه دور، نیمه‌وقت، ۲ سال سابقه)", "https://www.bth.se/english/education/programmes/masters-programme-in-software-engineering-60-credits"),
 ("سوئد – Halmstad MSc Information Technology شهریه", "https://www.mastersportal.com/studies/22787/information-technology.html"),
 ("سوئد – Halmstad مسکن (بدون تضمین)", "https://www.hh.se/english/education/student-life/find-accommodation.html"),
 ("سوئد – شهروندی ۸ ساله از ژوئن ۲۰۲۶", "https://www.imidaily.com/europe/sweden-passes-law-curtailing-naturalization-8-year-wait-income-floor/"),
 ("سوئد – اطلاعیه مهاجرتی سفارت تهران", "https://www.swedenabroad.se/globalassets/ambassader/iran-teheran/documents/migration-issues/new-folder/english-versin.pdf"),
 ("دانمارک – Pay Limit Scheme 2026", "https://www.nyidanmark.dk/pl-PL/You-want-to-apply/Work/Pay-limit-scheme"),
 ("دانمارک – برنامه‌های آموزش عالی: ۹۰ ساعت/ماه، ۶ ماه یا ۳ سال جست‌وجوی کار", "https://www.nyidanmark.dk/en-GB/You-want-to-apply/Study/Higher-Education"),
 ("دانمارک – مجوز ۳ ساله جست‌وجوی کار", "https://www.nyidanmark.dk/de-DE/You-want-to-apply/Study/Study---job-seeking/Study---3-years-job-seeking"),
 ("دانمارک – اقامت دائم", "https://www.nyidanmark.dk/de-DE/You-want-to-apply/Permanent-residence-permit/Permanent-residence"),
 ("دانمارک – تمکن DKK 7,426 (2026)", "https://nyidanmark.dk/en-GB/Words-and-concepts/SIRI/Self-support---SIRI"),
 ("دانمارک – AAU Computer Science (IT) شهریه €7,455/ترم", "https://studyindenmark.dk/portal/aalborg-university-aau/aalborg/computer-science-it-msc"),
 ("دانمارک – SDU شهریهٔ رسمی از ورودی ۲۰۲۶: Science/Engineering €17,300 در سال", "https://www.sdu.dk/en/uddannelse/fees_and_funding/tuition"),
 ("دانمارک – SDU MSc Computer Science (ظرفیت محدود، €17,300)", "https://www.sdu.dk/en/uddannelse/kandidat/datalogi/adgangskrav"),
 ("دانمارک – سفارت تهران (درخواست از ایران ممکن نیست)", "https://iran.um.dk/en"),
 ("دانمارک – IDA حقوق شروع ۲۰۲۶", "https://studerende.ida.dk/snart-nyuddannet/loen/softwareingenioer-loen-saa-meget-kommer-du-til-at-tjene/"),
 ("ایرلند – کف حقوق مجوز کار از ۱ مارس ۲۰۲۶ (€40,904 / €36,848 / €36,605)", "https://kodlyons.ie/critical-skills-employment-permit-changes/"),
 ("ایرلند – نقشه راه DETE تا ۲۰۳۰", "https://www.visahq.com/news/2025-12-12/ie/ireland-sets-phased-salary-threshold-hikes-for-all-work-permit-categories-first-rise-due-1-march-2026/"),
 ("ایرلند – ISD تمکن دانشجویی €10,000", "https://www.irishimmigration.ie/coming-to-study-in-ireland/what-are-my-study-options/a-fee-paying-private-primary-or-secondary-school/information-on-student-finances/"),
 ("ایرلند – UL MSc Software Engineering €20,800", "https://www.ul.ie/study/postgraduate/software-engineering-msc"),
 ("ایرلند – Maynooth فهرست شهریه 2025/26", "https://www.maynoothuniversity.ie/sites/default/files/assets/document/2025.26%20Postgraduate%20EU%20&%20International%20Fees%20List%20(24.02.25)%20V.4%20CHR.pdf"),
 ("ایرلند – سفارت/کنسول افتخاری تهران", "https://www.ireland.ie/en/tehran/"),
 ("ایرلند – QS 2027 دانشگاه‌های ایرلند", "https://www.thejournal.ie/irish-universities-qs-world-university-rankings-2027-7073948-Jun2026/"),
 ("بریتانیا – Graduate visa ۱۸ ماه (از ژانویه ۲۰۲۷)", "https://students.leeds.ac.uk/visa-information-after-studies/doc/graduate-visas"),
 ("بریتانیا – HC 584 (۳ سپتامبر ۲۰۲۶): تمکن £1,570 / £1,203 از ۳۰ نوامبر ۲۰۲۶", "https://www.gov.uk/government/publications/statement-of-changes-to-the-immigration-rules-hc-584-3-september-2026"),
 ("بریتانیا – Skilled Worker نرخ شغل SOC 2134 £54,700", "https://withrowan.co.uk/guides/skilled-worker-software-engineers"),
 ("بریتانیا – Earned Settlement (وضعیت سپتامبر ۲۰۲۶)", "https://www.ukimmigration.law/earned-settlement-ilr-uk-plans/"),
 ("انگلستان – Teesside MSc Computer Science 2026-27: £17,000، 2:2، IELTS 6.0", "https://www.tees.ac.uk/postgraduate_courses/computing_&_cyber_security/msc_computer_science.cfm"),
 ("انگلستان – Northumbria MSc Advanced Computer Science 2026/27: £21,500، 2:2", "https://www.northumbria.ac.uk/study-at-northumbria/courses/msc-advanced-computer-science-dtfava6/"),
 ("انگلستان – Leicester MSc Advanced Computer Science سپتامبر ۲۰۲۶: £24,250، 2:1", "https://le.ac.uk/courses/advanced-computer-science-msc/2026"),
 ("انگلستان – Essex MSc Advanced Computer Science 2026: £24,675، 2:2 (شامل Computer Engineering)", "https://www.essex.ac.uk/courses/pg00435/1/msc-advanced-computer-science"),
 ("انگلستان – York MSc Advanced Computer Science 2026/27: £32,900، 2:2، IELTS 6.5", "https://www.york.ac.uk/study/postgraduate-taught/courses/msc-advanced-computer-science/"),
 ("انگلستان – Chester MSc Advanced Computer Science 2026/27: £15,500 (کف قیمت انگلستان)", "https://www.chester.ac.uk/study/course-search/advanced-computer-science-msc/"),
 ("بریتانیا – Brunel MSc AI 2026/27 £24,795", "https://www.brunel.ac.uk/study/courses/artificial-intelligence-msc"),
 ("بریتانیا – عوارض £925 به ازای هر دانشجوی بین‌المللی (انگلستان، از 2028-29)", "https://www.researchprofessionalnews.com/rr-news-uk-politics-2025-11-international-levy-to-be-flat-fee-of-925-per-student/"),
 ("بریتانیا – وضعیت VAC تهران", "https://livingintehran.com/2026/02/03/tehran-diplomatic-update-recent-embassy-reopenings-current-status-feb-2026/"),
 ("QS WUR 2027 – TU Dresden", "https://tu-dresden.de/tu-dresden/newsportal/news/qs-ranking-2027-tud-gehoert-erneut-zu-den-zehn-besten-universitaeten-deutschlands-und-baut-internationalen-erfolg-weiter-aus"),
 ("QS WUR 2027 – Stuttgart", "https://www.uni-stuttgart.de/en/university/news/all/QS-World-University-Rankings-2027-The-University-of-Stuttgart-is-recognized-for-its-strong-research-performance-and-commitment-to-sustainability/"),
 ("QS WUR 2027 – Newcastle 149", "https://www.ncl.ac.uk/press/articles/latest/2026/06/qs2027/"),
 ("QS WUR 2027 – York =158", "https://www.york.ac.uk/about/rankings/"),
 ("QS WUR 2027 – Leicester =314", "https://www.topuniversities.com/universities/university-leicester"),
 ("QS WUR 2027 – Essex =438", "https://www.topuniversities.com/universities/essex-university"),
 ("QS WUR 2027 – Northumbria =528", "https://www.topuniversities.com/universities/northumbria-university-newcastle"),
 ("QS WUR 2027 – Brunel", "https://students.brunel.ac.uk/campus-news/brunel-climbs-global-qs-rankings-after-strong-year-for-research-and-graduate-outcomes"),
 ("QS WUR 2027 – سایر", "https://www.topuniversities.com/world-university-rankings"),
 ("حداقل دستمزد ۲۰۲۶ هلند (€14.71)", "https://arlettipartners.com/new-increase-in-the-dutch-minimum-hourly-wage-from-january-1st-2026/"),
 ("نرخ ارز (xe.com، ۲۷ سپتامبر ۲۰۲۶)", "https://www.xe.com/"),
 # ---- شیت «حوزه‌ها و بازار کار»
 ("بازار کار – LinkedIn/WEF ژانویه ۲۰۲۶: ۱.۳ میلیون شغل جدید AI؛ AI Engineer سریع‌ترین‌رشد", "https://www.weforum.org/stories/jobs-and-the-future-of-work/ai-has-already-added-1-3-million-new-jobs-according-to-linkedin-data/"),
 ("بازار کار – Bitkom 2025: ۱۰۹ هزار جای خالی IT در آلمان، ۷.۷ ماه زمان پرکردن", "https://www.bitkom.org/Bitkom/Publikationen/Der-Arbeitsmarkt-fuer-IT-Fachkraefte"),
 ("بازار کار – ISC2 Cybersecurity Workforce Study 2024/2025 (حذف عدد کمبود؛ کمبود بودجه دلیل اول؛ ۳۱٪ تیم‌ها بدون جونیور)", "https://www.isc2.org/research"),
 ("بازار کار – اخراج‌های صنعت بازی ۲۰۲۲–۲۰۲۶ (≈۴۵ هزار؛ افت حقوق Unity)", "https://en.wikipedia.org/wiki/2022%E2%80%932026_video_game_industry_layoffs"),
 ("بازار کار – آگهی‌های UX/UXR (Indeed تا Q4 2025)", "https://www.thevoiceofuser.com/everyone-knows-the-uxr-hiring-market-is-bad-how-bad-is-it-though/"),
 ("بازار کار – اشباع جونیور علم داده ۲۰۲۶", "https://research.com/advice/are-too-many-students-choosing-data-science-oversaturation-competition-hiring-reality"),
 # ---- شیت «برنامه‌ها» (منابع تکمیلی؛ لینک هر برنامه در خود شیت است)
 ("ایرلند – UL MSc AI & ML: €20,800", "https://www.ul.ie/study/postgraduate/artificial-intelligence-and-machine-learning-msc"),
 ("ایرلند – TU Dublin MSc Applied Cyber Security: €14,500، 2:2", "https://www.tudublin.ie/study/postgraduate/courses/applied-cyber-security/"),
 ("ایرلند – TU Dublin MSc CS (Data Science): €21,750، 2:2 + ۲ سال سابقه", "https://www.tudublin.ie/study/postgraduate/courses/computing-data-science/"),
 ("ایرلند – DCU MSc Computing majors: €25,000، 2:1، بورس €5,000", "https://www.dcu.ie/courses/postgraduate/school-computing/msc-computing-major-options"),
 ("ایرلند – Galway MSc CS (AI) €28,000 / SDD €18,440، 2026/27", "http://cs.universityofgalway.ie/science-engineering/postgraduateprogrammes/taught-postgraduate-courses/software-design-development.html"),
 ("آلمان – Saarland MSc Cybersecurity (C1، بدون شهریه)", "https://www.uni-saarland.de/en/study/programmes/master/cybersecurity.html"),
 ("آلمان – Passau MSc AI Engineering (B2، معدل ≤ 2.7، A1 آلمانی سال اول)", "https://www.uni-passau.de/en/msc-ai-eng"),
 ("آلمان – Cologne Game Lab MA Game Development & Research (€2,500/ترم غیر-EU)", "https://colognegamelab.de/study-programs/post-graduate-programs/game-development-research-ma/faqs/"),
 ("آلمان – Siegen MSc HCI (DAAD)", "https://www2.daad.de/deutschland/studienangebote/international-programmes/en/detail/4686/"),
 ("آلمان – H-BRS MSc Autonomous Systems (B2+)", "https://www.h-brs.de/en/inf/admission-application-master-autonomous-systems"),
 ("آلمان – RWTH MSc Software Systems Engineering", "https://sc.informatik.rwth-aachen.de/en/studium/master/sse/"),
 ("آلمان – Tübingen MSc Machine Learning (IELTS 7، €1,500/ترم)", "https://uni-tuebingen.de/fakultaeten/mathematisch-naturwissenschaftliche-fakultaet/fachbereiche/informatik/studium/studierende/lehre-studienorganisation/studiengaenge/machine-learning/admission-and-application/"),
 ("آلمان – TUM Informatics: €6,000 در ترم برای غیر-EU", "https://www.tum.de/en/studies/degree-programs/detail/informatics-master-of-science-msc"),
 ("آلمان – FAU Autonomy Technologies (B2، IELTS 6.0)", "https://www.fau.eu/degree-program/autonomy-technologies-m-sc/"),
 ("هلند – Twente Embedded Systems 2026/27: €21,700", "https://www.utwente.nl/en/education/master/programmes/embedded-systems/finance/"),
 ("هلند – Leiden CS 2026/27: €22,500", "https://www.universiteitleiden.nl/en/education/study-programmes/master/computer-science/artificial-intelligence/admission-and-application/tuition-fees"),
 ("هلند – Groningen AI 2026/27: €24,900", "https://www.rug.nl/masters/artificial-intelligence/?lang=en"),
 ("هلند – Utrecht Game & Media Technology 2026/27: €25,306", "https://www.uu.nl/en/masters/game-and-media-technology"),
 ("هلند – QS 2027 فهرست دانشگاه‌های هلند", "https://dub.uu.nl/en/news/dutch-universities-fall-global-qs-rankings"),
 ("سوئد – Gothenburg Game Design & Technology: SEK 290,000 کل", "https://www.gu.se/en/study-gothenburg/game-design-technology-masters-programme-n2gdt"),
 ("سوئد – KTH Machine Learning: ≈ SEK 180,000–190,000 (کل دوره 360k طبق راهنمای ۲۰۲۶؛ kth.se رقم را فقط در سامانه نشان می‌دهد)", "https://www.kth.se/en/studies/master/machine-learning"),
 ("سوئد – Umeå AI: SEK 152,300", "https://www.umu.se/en/education/master/masters-programme-in-artificial-intelligence/"),
 ("سوئد – QS 2027 فهرست دانشگاه‌های سوئد", "https://www.study.eu/best-universities/sweden"),
 ("دانمارک – ITU شهریهٔ رسمی ورودی ۲۰۲۶: €8,250 در ترم = €16,500 در سال (رقم قدیمی €6,700 منسوخ)", "https://en.itu.dk/Programmes/MSc-Programmes/Applying-to-a-MSc-programme/Non-EU-EOES"),
 ("دانمارک – AAU Cyber Security / Medialogy €7,455 در ترم", "https://studyindenmark.dk/portal/aalborg-university-aau/copenhagen/cyber-security-msc-in-engineering"),
 ("دانمارک – DTU €15,000 (Human-Centered AI / Autonomous Systems)", "https://www.dtu.dk/english/education/graduate/msc-programmes/autonomous-systems/prerequisites"),
 ("دانمارک – Aarhus CS €17,300", "https://masters.au.dk/computerscience"),
 ("دانمارک – QS 2027 فهرست دانشگاه‌های دانمارک", "https://leapscholar.com/blog/top-universities-in-denmark/"),
 ("انگلستان – Goldsmiths MSc Computer Games Programming £22,000", "https://www.gold.ac.uk/pg/msc-computer-games-programming/"),
 ("انگلستان – Royal Holloway MSc Information & Cyber Security £25,500", "https://www.royalholloway.ac.uk/studying-here/postgraduate/information-security/information-and-cyber-security/"),
 ("انگلستان – Kent MSc Cyber Security (NCSC)", "https://www.kent.ac.uk/courses/postgraduate/1225/cyber-security"),
 ("انگلستان – MMU MSc Cyber Security £21,000", "https://www.mmu.ac.uk/study/postgraduate/course/msc-cyber-security"),
 ("انگلستان – York MSc Human-Centred Interactive Technologies £32,900", "https://www.york.ac.uk/study/postgraduate-taught/courses/msc-human-centred-interactive-technologies/"),
 ("انگلستان – Lancaster MSc Cyber Security £30,000", "https://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/cyber-security-msc/2026/"),
 ("انگلستان – NTU QS 2027 =639", "https://collegedunia.com/uk/university/862-nottingham-trent-university-nottingham/ranking"),
 ("آلمان – FAU: شهریهٔ غیر-EU از ترم تابستان ۲۰۲۷ (AI/CS €4,000، Autonomy Tech €2,000 در ترم؛ BayHIG §13)", "https://www.fau.eu/studying/international-students/application-and-enrollment-for-international-applicants/tuition-fees-for-students-from-non-eu-states/"),
 ("آلمان – Passau: «فعلاً» بدون شهریه برای غیر-EU (اعلام رسمی)", "https://www.uni-passau.de/en/study/news/news/no-tuition-fees-for-international-students-at-the-university-of-passau"),
 ("دانمارک – Aarhus نرخ رسمی 2026/27: Computer Science / Data Science / Computer Engineering €17,300", "https://masters.au.dk/tuitionfees/current-tuition-fee-rates"),
 ("دانمارک – AAU Computer Science (IT): شرط رسمی ≥ ۱۵۰ ECTS دروس CS؛ معیار رتبه‌بندی ۲۰۲۷ شامل سابقهٔ کار", "https://www.en.aau.dk/education/master/computer-science-it"),
 ("سوئد – Chalmers شهریهٔ استاندارد 2026/27 ≈ SEK 175,000 (collegedunia به نقل از صفحهٔ شهریهٔ Chalmers)", "https://collegedunia.com/sweden/university/769-chalmers-university-of-technology-gothenburg/programs?stream_id=48&degree_type=Master"),
 ("انگلستان – Surrey MSc Cyber Security ورودی ۲۰۲۷: £25,900 (فوریه) / £26,900 (سپتامبر)", "https://www.surrey.ac.uk/postgraduate/cyber-security-msc"),
 ("انگلستان – Newcastle MSc Computer Game Engineering £32,300، شرط 2:2 (QS TopUniversities)", "https://www.topuniversities.com/universities/newcastle-university/postgrad/msc-computer-game-engineering"),
 ("هلند – TU/e شهریهٔ رسمی 2026/27 €21,700 (2027/28: €22,400)", "https://www.tue.nl/en/education/become-a-tue-student/tuition-fees"),
]

# ---------------------------------------------------------------- styling
thin = Side(style="thin", color="BBBBBB")
border = Border(left=thin, right=thin, top=thin, bottom=thin)
hdr_fill = PatternFill("solid", fgColor="1F4E78")
hdr_font = Font(bold=True, color="FFFFFF", size=11)
crit_fill = PatternFill("solid", fgColor="EAF1FB")
src_font = Font(size=9, color="555555")
wrap_rtl = Alignment(wrap_text=True, vertical="top", horizontal="right", readingOrder=2)
wrap_ctr = Alignment(wrap_text=True, vertical="top", horizontal="center", readingOrder=2)


def style_sheet(ws, widths, header_row=1, freeze_col=3):
    ws.sheet_view.rightToLeft = True
    ws.freeze_panes = ws.cell(row=header_row + 1, column=freeze_col)
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w
    for cell in ws[header_row]:
        cell.fill = hdr_fill
        cell.font = hdr_font
        cell.alignment = wrap_ctr
        cell.border = border
    for row in ws.iter_rows(min_row=header_row + 1, max_row=ws.max_row):
        for cell in row:
            cell.alignment = wrap_rtl
            cell.border = border


wb = Workbook()

# ---- Sheet 1: the table
ws = wb.active
ws.title = "جدول نهایی ۲۰۲۶"
ws.append(HEAD)
for r in ROWS:
    ws.append(r)
style_sheet(ws, [6, 30, 46, 42, 46, 42, 42, 46, 34])
ws.row_dimensions[1].height = 34
for row in ws.iter_rows(min_row=2, max_row=ws.max_row):
    row[0].alignment = wrap_ctr
    row[1].fill = crit_fill
    row[1].font = Font(bold=True)
    row[8].font = src_font
n = ws.max_row + 2
ws.cell(row=n, column=2, value="تاریخ راستی‌آزمایی: ۲۷ سپتامبر ۲۰۲۶ (۵ مهر ۱۴۰۵). " + FX).font = Font(bold=True)
ws.cell(row=n + 1, column=2, value="همه ارقام سطح 2026/27 و از منابع رسمی (شیت «منابع»)؛ برای ورودی ۲۰۲۸ سالانه ۳–۵٪ (شهریه ۵–۱۰٪) اضافه کنید. ردیف‌های ۱۳، ۱۴، ۱۷–۱۹، ۲۶ برآورد/ارزیابی هستند و در ستون منبع مشخص شده‌اند.")
ws.cell(row=n + 2, column=2, value="جدول اولیه (Table.xlsx) برای مقایسه دست‌نخورده مانده است.")
ws.cell(row=n + 3, column=2, value="شیت «برنامه‌ها»: ≈۱۰۰ برنامهٔ انگلیسی‌زبان در ۸ حوزهٔ کامپیوتری (نه فقط CS) برای هر ۶ کشور؛ شیت «حوزه‌ها و بازار کار»: کدام حوزه برای شما بازار و پذیرش بهتری دارد.").font = Font(bold=True)

# ---- Sheet 1b: programme catalogue (all fields, all 6 countries)
ws4 = wb.create_sheet("برنامه‌ها")
HEAD4 = ["#", "کشور", "دانشگاه", "شهر", "هزینهٔ زندگی شهر (تقریبی، ماهانه با اجاره)", "برنامه", "حوزه", "مدت",
         "شهریهٔ سالانه 2026/27 (ارز محلی)", "≈ شهریهٔ سالانه به دلار", "شرط ورود", "IELTS", "QS 2027",
         "Safe / Target / Reach (معدل ۱۵.۷۷)", "بازار کار حوزه (۱–۵) و نکته", "نکتهٔ برنامه", "منبع (صفحهٔ رسمی)"]
ws4.append(HEAD4)
tier_fill = {"Safe": PatternFill("solid", fgColor="E2F0D9"), "Safe/Target": PatternFill("solid", fgColor="EAF5E1"),
             "Target": PatternFill("solid", fgColor="FFF2CC"), "Target/Reach": PatternFill("solid", fgColor="FCE4D6"),
             "Reach": PatternFill("solid", fgColor="F8CBAD")}
for i, (country, uni, city_key, prog, fkey, dur, fee_txt, fee_num, entry, ielts, qs, tier, note, url) in enumerate(PROGRAMS, start=1):
    flabel, fscore, fnote = FIELDS[fkey]
    city_name, city_cost = CITIES[city_key]
    ws4.append([i, country, uni, city_name, city_cost, prog, flabel, dur, fee_txt, fee_usd(*fee_num), entry, ielts, qs, tier,
                f"{fscore}/5 — {fnote}", note, url])
style_sheet(ws4, [5, 10, 28, 30, 22, 40, 22, 9, 30, 14, 34, 12, 12, 16, 44, 40, 40], freeze_col=5)
ws4.row_dimensions[1].height = 48
ws4.auto_filter.ref = f"A1:Q{ws4.max_row}"
for row in ws4.iter_rows(min_row=2, max_row=ws4.max_row):
    row[0].alignment = wrap_ctr
    row[1].alignment = wrap_ctr
    row[13].alignment = wrap_ctr
    row[13].fill = tier_fill.get(row[13].value, PatternFill())
    row[13].font = Font(bold=True)
    row[16].hyperlink = row[16].value
    row[16].font = Font(size=9, color="0563C1", underline="single")
    row[16].alignment = Alignment(wrap_text=True, vertical="top", horizontal="left")
n4 = ws4.max_row + 2
notes4 = [
    "راهنما: هر ردیف یک برنامهٔ انگلیسی‌زبان است. Safe/Target/Reach نسبت به معدل ۱۵.۷۷/۲۰ (≈ 2:2 بریتانیا / ≈ 2.3 آلمانی / ≈ ۷۹٪) و IELTS ≈ 7 سنجیده شده و پیش‌بینی پذیرش نیست. «≈» یعنی رقم از منبع ثانویه یا سال قبل است — قبل از اقدام صفحهٔ رسمی را چک کنید.",
    "شهریهٔ دلاری با نرخ " + FX + " و گرد شده به $100. برای ورودی ۲۰۲۸ شهریه‌ها را ۵–۱۰٪ در سال بالاتر فرض کنید. آلمان: عدد فقط سهم ترم (Semesterbeitrag) است که بلیت حمل‌ونقل را هم شامل می‌شود.",
    "امتیاز بازار کار (۱–۵) ارزیابی من بر پایهٔ منابع شیت «حوزه‌ها و بازار کار» است، نه آمار رسمی؛ برای هر برنامه فقط حوزه را نشان می‌دهد، نه کیفیت آن دانشگاه.",
    "ستون «هزینهٔ زندگی شهر» برآورد تقریبی هزینهٔ ماهانهٔ دانشجو با اجارهٔ اتاق در همان شهر است (سازگار با ردیف ۶ جدول اصلی)؛ برچسب‌ها: ارزان / متوسط / گران / خیلی گران. برای مقایسهٔ کشورها همچنان ردیف‌های ۶–۸ جدول اصلی معیار است.",
    "بازبینی صحت اعداد (۲۷ سپتامبر ۲۰۲۶): ≈۷۰٪ شهریه‌ها مستقیماً از صفحهٔ رسمی 2026/27 است؛ ردیف‌های «≈» از منبع ثانویه یا سال قبل‌اند. اصلاح‌های این بازبینی: FAU از تابستان ۲۰۲۷ شهریه می‌گیرد (AI/CS €4,000/ترم)؛ ITU €16,500 (نه €13,400)؛ Radboud €19,714 رسمی؛ Chalmers ≈ SEK 175k (نه 160k)؛ KTH ≈ 180–190k؛ AAU شرط ≥ ۱۵۰ ECTS؛ Surrey Cyber ورودی ۲۰۲۷؛ Newcastle Games 2:2؛ Sheffield AI ≈ £32.9–34.3k. رتبه‌بندی Safe/Target/Reach، امتیاز بازار و ردهٔ هزینهٔ شهر ارزیابی‌اند، نه دادهٔ رسمی.",
    "حذف‌شده‌ها: Essex MSc Computer Games (برای 2025/26 و 2026/27 تعلیق شده)، Hull AI & Data Science (سه رقم متناقض شهریه)، UCD/TCD (2:1 و ≈ €30k → Reach، بررسی نشد)، KU Copenhagen (شهریه تأیید نشد)، NCI/DBS ایرلند (کالج خصوصی، اعتبار کمتر).",
]
for k, t in enumerate(notes4):
    c = ws4.cell(row=n4 + k, column=2, value=t)
    c.alignment = wrap_rtl
    ws4.merge_cells(start_row=n4 + k, start_column=2, end_row=n4 + k, end_column=17)
    ws4.row_dimensions[n4 + k].height = 34

# ---- Sheet 1c: fields & job market
ws5 = wb.create_sheet("حوزه‌ها و بازار کار")
ws5.append(["حوزه", "تقاضای بازار ۲۰۲۶ (۱–۵)", "حقوق شروع نسبت به CS عمومی", "سازگاری با «فقط انگلیسی»",
            "تناسب با پروفایل شایان (Computer Eng، معدل ۱۵.۷۷، ۲ سال IT + ۷ ماه Unity/C#)", "ریسک‌ها / واقعیت بازار", "منابع"])
for r in FIELD_ROWS:
    ws5.append(r)
style_sheet(ws5, [26, 18, 40, 34, 56, 56, 40], freeze_col=2)
ws5.row_dimensions[1].height = 40
for row in ws5.iter_rows(min_row=2, max_row=ws5.max_row):
    row[0].fill = crit_fill
    row[0].font = Font(bold=True)
    row[1].alignment = wrap_ctr
    row[6].font = src_font
n5 = ws5.max_row + 2
c = ws5.cell(row=n5, column=1, value="جمع‌بندی برای شما: (۱) هوش مصنوعی/ML و (۲) مهندسی نرم‌افزار بهترین ترکیب «بازار + پذیرش‌پذیری + انگلیسی» را دارند؛ (۳) امنیت سایبری اگر حاضر به گرفتن گواهی و کارآموزی باشید؛ ابری/DevOps به‌عنوان گرایش داخل CS/SE. علم داده فقط با تمرکز Data Engineering. نهفته/رباتیک قوی است ولی با شرط «فقط انگلیسی» شما نمی‌خواند (کارفرمایان صنعتی آلمان/سوئد). HCI/UX و بازی‌سازی با معیار «حقوق شروع بالا» شما در تضادند — سابقهٔ Unity را به‌عنوان پورتفولیو کنار یک ارشد Software/AI نگه دارید.")
c.alignment = wrap_rtl
c.font = Font(bold=True)
ws5.merge_cells(start_row=n5, start_column=1, end_row=n5, end_column=7)
ws5.row_dimensions[n5].height = 70

# ---- Sheet 2: summary
ws2 = wb.create_sheet("جمع‌بندی")
ws2.append(["موضوع", "جمع‌بندی"])
for r in SUMMARY:
    ws2.append(r)
style_sheet(ws2, [34, 130], freeze_col=2)

# ---- Sheet 3: sources
ws3 = wb.create_sheet("منابع")
ws3.append(["موضوع", "لینک (بازدید ۲۷ سپتامبر ۲۰۲۶)"])
for t, u in SOURCES:
    ws3.append([t, u])
style_sheet(ws3, [60, 110], freeze_col=2)
for row in ws3.iter_rows(min_row=2, max_row=ws3.max_row):
    row[1].hyperlink = row[1].value
    row[1].font = Font(color="0563C1", underline="single")
    row[1].alignment = Alignment(wrap_text=True, vertical="top", horizontal="left")

wb.save("Table_final.xlsx")
print("saved Table_final.xlsx")
