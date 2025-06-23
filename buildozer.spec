[app]

title = MyAssistant
package.name = myassistant
package.domain = org.myassistant

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,kivy,pyjnius,websocket-client,cython

android.permissions = INTERNET,VIBRATE,FOREGROUND_SERVICE,WAKE_LOCK

android.archs = armeabi-v7a

android.minapi = 21
android.foreground_service = true

entrypoint = main.py

android.sdk_path = ~/.buildozer/android/platform/android-sdk

# icon.filename = %(source.dir)s/icon.png
p4a.branch = master
log_level = 2
warn_on_root = 1
