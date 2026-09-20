import requests

# உங்கள் Bot Token மற்றும் Chat ID-ஐ இங்கே மாற்றவும்
BOT_TOKEN = "8393676021:AAFHKCuRB_88gED02wiyPJieaXRTc_3Ei8s"
CHAT_ID = "8903813463"

def send_telegram_message(message: str):
    """Telegram-க்கு உடனடியாக alert மெசேஜ் அனுப்பும் function"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload, timeout=10)
        return response.status_code == 200
    except Exception as e:
        print(f"Error sending alert: {e}")
        return False

# Test alert அனுப்பி சரிபார்க்க
if __name__ == "__main__":
    test_msg = "🚀 *RoutinePilot Connected!* \nஉங்க போனுக்கு இனிமே daily routine & 10 English words alerts வரும்!"
    if send_telegram_message(test_msg):
        print("Success! Check your Telegram app for the alert.")
    else:
        print("Failed! Check your BOT_TOKEN and CHAT_ID.")