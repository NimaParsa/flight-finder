import requests


class NotificationManager:
    def __init__(self):
        self.bot_chatID = '100932112'
        self.bot_token = '5848505489:AAHtDajrAityfgpJVgPvJrfyCw1A3CGTBYA'

    def telegram_bot_sendtext(self, price, city_name, iata, date):
        telegram_params = {
            "chat_id": self.bot_chatID,
            "parse_mode": "Markdown",
            "text": f"Low Price Alert!!!\n\n"
                    f"Price:{price}"
                    f"\nArrival City Name:{city_name}"
                    f"\nArrival Airport IATA Code:{iata}"
                    f"\nDate:{date}"
        }
        send_text = 'https://api.telegram.org/bot' + self.bot_token + '/sendMessage?'
        response1 = requests.get(send_text, params=telegram_params)
        return response1.json()
