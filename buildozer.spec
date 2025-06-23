[app]

title = MyAssistant
package.name = myassistant
package.domain = org.myassistant

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,kivy==2.3.0,pyjnius,websocket-client,cython

android.permissions = INTERNET,VIBRATE,FOREGROUND_SERVICE,WAKE_LOCK

android.arch = armeabi-v7a

android.minapi = 21
android.maxapi = 34
android.sdk = 34
android.ndk = 23b
android.foreground_service = true

entrypoint = main.py

p4a.branch = master
log_level = 2
warn_on_root = 1

# Удалено явное указание sdk_path, так как в Actions он будет в другом месте
