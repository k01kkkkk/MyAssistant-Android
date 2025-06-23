from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from jnius import autoclass
import websocket
import threading
import time

PythonActivity = autoclass('org.kivy.android.PythonActivity')
Context = autoclass('android.content.Context')
Vibrator = PythonActivity.mActivity.getSystemService(Context.VIBRATOR_SERVICE)

def vibrate(ms=1000):
    try:
        Vibrator.vibrate(ms)
        print("✅ Vibrate done")
    except Exception as e:
        print("❌ Vibrate error:", e)

def speak(text):
    try:
        Intent = autoclass('android.content.Intent')
        TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
        Locale = autoclass('java.util.Locale')

        tts = TextToSpeech(PythonActivity.mActivity, None)
        tts.setLanguage(Locale.ENGLISH)
        tts.speak(text, TextToSpeech.QUEUE_FLUSH, None, "utteranceId")
        print("🔊 Speak:", text)
    except Exception as e:
        print("❌ TTS error:", e)

def ws_client():
    def on_message(ws, msg):
        print("📩 Message:", msg)
        if msg == "vibrate":
            vibrate(1000)
        elif msg.startswith("sound:"):
            text = msg.replace("sound:", "").strip()
            if text:
                speak(text)

    def on_error(ws, error):
        print("⚠️ WebSocket error:", error)

    def on_close(ws, code, reason):
        print("🔌 Connection closed, reconnecting in 5s...")
        time.sleep(5)
        threading.Thread(target=ws_client, daemon=True).start()

    def on_open(ws):
        print("✅ Connected to WebSocket")
        def ping():
            while ws.keep_running:
                try:
                    ws.send("ping")
                    time.sleep(10)
                except:
                    break
        threading.Thread(target=ping, daemon=True).start()

    ws = websocket.WebSocketApp(
        "wss://7cd0-2a03-f680-fe05-25b8-a5c0-866d-5dc8-4745.ngrok-free.app",
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.run_forever()

class MyApp(App):
    def build(self):
        Clock.schedule_once(lambda dt: threading.Thread(target=ws_client, daemon=True).start(), 1)
        return Label(text="🤖 MyAssistant running...")

MyApp().run()
