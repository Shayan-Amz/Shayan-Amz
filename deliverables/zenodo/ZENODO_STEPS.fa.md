# گرفتن DOI از Zenodo برای ریپوهای گیت‌هاب — راهنمای قدم‌به‌قدم

> ✅ **انجام شد (۲۰۲۶-۱۰-۲۶):** Floating-Point-ALU v1.0.0 → Concept DOI `10.5281/zenodo.23677513`. پچ `0002-add-zenodo-doi.patch` بج و شناسه‌ها را به ریپو اضافه می‌کند.

> هدف: یک DOI دائمی (مثل `10.5281/zenodo.1234567`) برای **Floating-Point-ALU** (و در صورت تمایل OpenGL-Dream-Village و پایان‌نامه)
> تا در رزومه بخش «Technical Reports & Preprints» معتبر و قابل‌استناد باشد. بدون داوری ژورنال، رایگان، حدود ۲۰ دقیقه.

## چرا Floating-Point-ALU اولویت اول است؟

| معیار | FP-ALU | OpenGL-Dream-Village | Real-Estate (پایان‌نامه) |
|---|---|---|---|
| لایسنس | MIT ✅ | MIT ✅ | Proprietary ⚠ (رکورد Zenodo باید restricted باشد یا لایسنس عوض شود) |
| هندسه/کد شخص ثالث | ندارد | هندسه صحنه از krishnodey (attributed) — باید در متادیتا ذکر شود | ندارد |
| نتیجهٔ عددی قابل‌ادعا | ۳۲٬۰۲۶٬۹۹۲ تست، ۰ خطا، ۴ کامپایلر | ۰ پیکسل اختلاف، ۴ صحنه، ۳ سیستم‌عامل | هنوز عدد F1/WER اندازه‌گیری نشده (اول بنچمارک را اجرا کنید) |
| گزارش فنی آماده | `deliverables/technical-report-fp32/` ✅ | — | — |

## مرحلهٔ ۰ — پیش‌نیازها (۵ دقیقه)

1. **ORCID بگیرید** (رایگان): https://orcid.org/register → شناسهٔ `0000-000X-XXXX-XXXX` را در `CITATION.cff` و `.zenodo.json` (`"orcid": "..."` داخل creators) اضافه کنید. برای اپلای کانادا مفید است.
2. در Zenodo با **GitHub login** ثبت‌نام کنید: https://zenodo.org/signup → «Sign up with GitHub». این‌طوری اتصال ریپوها خودکار می‌شود.

## مرحلهٔ ۱ — فایل‌های متادیتا را به ریپو اضافه کنید

برای هر ریپو، دو فایل از همین پوشه را در **ریشهٔ ریپو** بگذارید:

```bash
cd Floating-Point-ALU
cp /path/to/deliverables/zenodo/Floating-Point-ALU/CITATION.cff .
cp /path/to/deliverables/zenodo/Floating-Point-ALU/.zenodo.json .
git add CITATION.cff .zenodo.json
git commit -m "Add citation metadata (CFF + Zenodo)"
git push
```

* `CITATION.cff` → گیت‌هاب دکمهٔ **«Cite this repository»** را در سایدبار نشان می‌دهد و Zenodo هم از آن می‌خواند.
* `.zenodo.json` → عنوان/توضیح/کلیدواژه/لایسنس رکورد Zenodo را تعیین می‌کند (در غیر این صورت فقط از توضیح ریپو استفاده می‌کند).
* فایل‌ها اعتبارسنجی شده‌اند (`cffconvert --validate` → valid, schema 1.2.0).

## مرحلهٔ ۲ — اتصال GitHub ↔ Zenodo (یک‌بار)

1. https://zenodo.org/account/settings/github/ را باز کنید.
2. اگر لیست ریپوها خالی است، «Sync now» بزنید.
3. کلید (toggle) کنار `Shayan-Amz/Floating-Point-ALU` را **ON** کنید.
   ⚠ **این باید قبل از ساختن Release انجام شود.** ریلیزهایی که قبل از ON کردن ساخته شوند DOI نمی‌گیرند (باید ریلیز جدید بسازید).

## مرحلهٔ ۳ — ساختن اولین Release

از سایت گیت‌هاب (Releases → Draft a new release) یا با CLI:

```bash
gh release create v1.0.0 --repo Shayan-Amz/Floating-Point-ALU \
  --title "v1.0.0 — bit-exact binary32 ALU, 32M differential checks" \
  --notes "First archived release. 32,026,992 differential checks vs host FPU, 0 failures (GCC/Clang/AppleClang/MSVC). See docs/technical-report.pdf."
```

* نسخهٔ `v1.0.0` با `version: 1.0.0` در `CITATION.cff` یکی باشد.
* اگر می‌خواهید PDF گزارش فنی هم داخل آرشیو Zenodo باشد، قبل از ریلیز آن را در ریپو commit کنید (مثلاً `docs/technical-report.pdf`).

## مرحلهٔ ۴ — گرفتن DOI و بج (۲–۵ دقیقه بعد از ریلیز)

1. به https://zenodo.org/account/settings/github/ برگردید؛ جلوی ریپو یک بج DOI ظاهر می‌شود. روی آن کلیک کنید.
2. دو DOI می‌بینید:
   * **Concept DOI** (همهٔ نسخه‌ها) ← این را در رزومه و `CITATION.cff` بگذارید.
   * **Version DOI** (فقط v1.0.0).
3. بج را به README اضافه کنید (شمارهٔ `XXXXXXX` را عوض کنید):

```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
```

4. خط `# doi:` را در `CITATION.cff` باز کنید و DOI را بنویسید؛ `related_identifiers` در `.zenodo.json` هم می‌تواند DOI گزارش را داشته باشد. (این تغییر برای ریلیز بعدی اعمال می‌شود؛ متادیتای رکورد فعلی را می‌توانید مستقیم در Zenodo → Edit هم اصلاح کنید.)

## مرحلهٔ ۵ — (اختیاری) آپلود گزارش فنی به‌عنوان رکورد جداگانه

اگر می‌خواهید گزارش FP32 یک DOI **مستقل از کد** داشته باشد (برای بخش Preprints بهتر است):

1. https://zenodo.org/uploads/new
2. Resource type: **Publication → Technical note** (یا Preprint)
3. فایل: `technical-report-fp32/report.pdf`
4. Title / Authors (با ORCID) / Description = چکیدهٔ گزارش / License: CC-BY-4.0
5. Related works: «is supplemented by» → DOI کدِ مرحلهٔ ۴.
6. Publish → DOI جدید. همین را می‌توانید در ResearchGate هم به‌صورت «Preprint» اضافه کنید (ResearchGate خودش DOI می‌دهد ولی DOI Zenodo معتبرتر است؛ یکی را انتخاب کنید و دیگری را فقط لینک بدهید تا DOI تکراری نسازید).

## قالب استناد برای رزومه (بعد از گرفتن DOI)

```
Amouzadeh, S. (2026). Floating-Point-ALU: A bit-exact C++17 software model of an IEEE 754 binary32 ALU
    (Version 1.0.0) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.XXXXXXX

Amouzadeh, S. (2026). Bit-exact software modelling of IEEE 754 binary32 arithmetic with 32-million-case
    differential verification [Technical report]. Zenodo. https://doi.org/10.5281/zenodo.YYYYYYY
```

## نکته دربارهٔ Real-Estate / پایان‌نامه

* `.zenodo.json` آن با `access_right: restricted` و `license: other-closed` آماده شده چون LICENSE ریپو proprietary است. رکورد restricted هم DOI و صفحهٔ متادیتا دارد (برای رزومه کافی است) ولی فایل‌ها عمومی نیستند.
* اگر می‌خواهید open باشد: LICENSE را به MIT/Apache-2.0 تغییر دهید و در `.zenodo.json` بگذارید `"access_right": "open", "license": "MIT"`.
* بهتر است **اول** بنچمارک متنی (`deliverables/thesis-evaluation/`) را اجرا و نتایج را commit کنید، بعد ریلیز بزنید تا آرشیو Zenodo شامل اعداد F1 باشد.

## چیزهایی که من (ایجنت) نمی‌توانم از داخل سندباکس انجام دهم

* باز کردن zenodo.org یا orcid.org (دسترسی شبکه فقط به GitHub/PyPI/npm).
* بنابراین مراحل ۰، ۲، ۴ و ۵ را شما انجام می‌دهید. مراحل ۱ و ۳ را می‌توانم با `gh` برایتان انجام دهم — **فقط بعد از اینکه مرحلهٔ ۲ را تأیید کردید**، چون ریلیزِ قبل از اتصال DOI نمی‌گیرد.
