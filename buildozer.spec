[app]
title = إدارة المشتريات
package.name = purchasesapp
package.domain = org.purchases
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,flask,kivy,sqlite3,werkzeug
orientation = portrait
fullscreen = 0
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, CAMERA
android.api = 31
android.minapi = 21

[buildozer]
log_level = 2
warn_on_root = 1
bin_dir = /sdcard/Download
