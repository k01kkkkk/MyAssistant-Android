[app]

title = MyAssistant
package.name = myassistant
package.domain = org.myassistant

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,kivy==2.3.0,pyjnius,websocket-client,cython==0.29.36

android.permissions = INTERNET,VIBRATE,FOREGROUND_SERVICE,WAKE_LOCK
android.archs = armeabi-v7a,arm64-v8a
android.minapi = 21
android.maxapi = 34
android.ndk_path = /home/runner/android-sdk/ndk/23.1.7779620
android.foreground_service = true

orientation = portrait
fullscreen = 0

log_level = 2
warn_on_root = 1
p4a.branch = master

# Путь к SDK будет установлен автоматически в CI
