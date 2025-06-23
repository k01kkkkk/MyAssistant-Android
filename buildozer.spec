[app]

# Название приложения
title = MyAssistant
package.name = myassistant
package.domain = org.myassistant

# Где лежит твой main.py
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Версия
version = 0.1
requirements = python3,kivy,pyjnius,websocket-client

# Разрешения Android
android.permissions = INTERNET,VIBRATE,FOREGROUND_SERVICE,WAKE_LOCK

# Минимальный API Android (например Android 5.0 = 21)
android.minapi = 21

# Архитектура (поддержка большинства устройств)
android.arch = armeabi-v7a

# Включение фонового режима
android.foreground_service = true

# Удаление всех файлов, кроме указанных
copy_to_assets = 0

# Язык и строка запуска
entrypoint = main.py

# (Опционально) можно указать иконку:
# icon.filename = %(source.dir)s/icon.png

# Компрессия Python-кода
android.include_exts = py

# Оптимизация
android.allow_backup = 1
android.hardwareAccelerated = true

# Используется SDL2 (стандартно)
android.api = 33
android.sdk = 33
android.ndk = 25b
android.ndk_path = 
android.sdk_path = 

# (Опционально) убрать эти если не используешь
# android.logcat_filters = *:S python:D

# Без изменения
p4a.branch = master
log_level = 2
warn_on_root = 1
