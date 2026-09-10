import requests
import json

token = "8274980094:AAFOCAHI_9c1JykEFqkh2ftDoDPNKYaOU4A"
url = f"https://api.telegram.org/bot{token}/getWebhookInfo"

response = requests.get(url)
print("Telegram Webhook Info:")
print(json.dumps(response.json(), indent=2))
