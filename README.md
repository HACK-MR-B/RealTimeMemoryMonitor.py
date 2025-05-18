# RealTimeMemoryMonitor.py


# 🧠 RealTimeMemoryMonitor.py

## 📄 الوصف (Description in Arabic)

سكربت بايثون يقوم بمراقبة استخدام الذاكرة (RAM) في الوقت الحقيقي على جهاز المستخدم.  
يعرض السكربت معلومات الذاكرة بشكل لحظي ويقوم بما يلي:

- ✅ عرض حجم الذاكرة الكلي، المستخدم، والمتاح.
- ⚠️ تنبيه المستخدم إذا تجاوز استخدام الذاكرة نسبة 80%.
- 📝 تسجيل جميع القراءات في ملف سجل `memory_log.txt` مع الوقت والتاريخ.
- 🔁 تحديث المعلومات كل ثانية بشكل تلقائي.

---

## 🇺🇸 Description (English)

A Python script for **real-time RAM monitoring**.  
This script continuously displays system memory usage and performs the following:

- ✅ Shows total, used, and available memory.
- ⚠️ Warns the user when memory usage exceeds 80%.
- 📝 Logs every reading to a file named `memory_log.txt` with a timestamp.
- 🔁 Refreshes data every second.

---

## 📦 المتطلبات (Requirements)

Install the required Python package using:

```bash
pip install psutil

python3 RealTimeMemoryMonitor.py
