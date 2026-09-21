import threading
import time
from app import app
from kivy.app import App
from kivy.uix.webbrowser import WebBrowser

def run_flask():
    app.run(host='127.0.0.1', port=5000, debug=False)

class PurchasesApp(App):
    def build(self):
        # تشغيل خادم flask في الخلفية
        threading.Thread(target=run_flask, daemon=True).start()
        time.sleep(1.5)
        # فتح واجهة الويب داخل تطبيق أندرويد
        return WebBrowser(url="http://127.0.0.1:5000")

if __name__ == '__main__':
    PurchasesApp().run()
