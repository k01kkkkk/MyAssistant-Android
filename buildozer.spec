[app]

title = MyAssistant
package.name = myassistant
package.domain = org.myassistant

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,kivy,pyjnius,websocket-client

android.permissions = INTERNET,VIBRATE,FOREGROUND_SERVICE,WAKE_LOCK
android.minapi = 21
android.foreground_service = true
