[app]

title = MyAssistant
package.name = myassistant
package.domain = org.myassistant

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,kivy,pyjnius,websocket-client

android.permissions = INTERNET,VIBRATE,FOREGROUND_SERVICE,WAKE_LOCK

# ✅ Устаревший android.arch заменён:
android.archs = armeabi-v7a

# ✅ Можно удалить — GitHub Actions сам ставит SDK/NDK:
# android.api = 33
# android.sdk = 33

android.minapi = 21
android.foreground_service = true

entrypoint = main.py

# Необязательные параметры (можно оставить по умолчанию)
# icon.filename = %(source.dir)s/icon.png
p4a.branch = master
log_level = 2
warn_on_root = 1
