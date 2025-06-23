[app]

title = MyAssistant
package.name = myassistant
package.domain = org.myassistant
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3,kivy,pyjnius,websocket-client

android.permissions = INTERNET,VIBRATE,FOREGROUND_SERVICE,WAKE_LOCK

# Укажи минимальную версию SDK (например 21)
android.minapi = 21

# Включи foreground service (если нужно)
android.foreground_service = true

# Используем SDL2 (стандарт)
android.arch = armeabi-v7a

# Если нужно, добавь icon (опционально)
# icon.filename = %(source.dir)s/data/icon.png
