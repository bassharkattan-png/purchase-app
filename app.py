import os
from flask import Flask, render_template, request, redirect, url_for

# تحديد المسار الثابت الذي أخبرتني عنه لتخزين البيانات والجداول
TARGET_DIR = "/sdcard/مشاريع تيرمكس/برنامج جداول"
os.makedirs(TARGET_DIR, exist_ok=True)

# إعداد تطبيق Flask ليعمل مع مجلد المشروع
app = Flask(__name__, 
            template_folder=TARGET_DIR, 
            static_folder=TARGET_DIR)

@app.route('/')
def index():
    # تأكد أن صفحة الواجهة الرئيسية لديك اسمها index.html داخل نفس المجلد
    return render_template('index.html')

if __name__ == '__main__':
    print("جاري تشغيل السيرفر محلياً...")
    # تشغيل السيرفر على المنفذ الافتراضي
    app.run(host='0.0.0.0', port=5000, debug=True)
