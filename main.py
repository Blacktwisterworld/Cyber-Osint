import os
import requests
import json
from flask import Flask, request
import telebot

# Bot Configuration (Hardcoded as requested)
BOT_TOKEN = "8274980094:AAFOCAHI_9c1JykEFqkh2ftDoDPNKYaOU4A"
ADMIN_CHAT_ID = "7236183825"

# Get environment variables (If not set, we'll try to get it from the request later)
WEBHOOK_URL = os.environ.get('RENDER_EXTERNAL_URL')


# Define your 5 API URLs and their respective query parameters
API_CONFIGS = {
    'tg': {
        'url': os.environ.get('API_TG_URL', 'https://tg2num-botadminshere.vercel.app/'),
        'param_name': 'id',
        'desc': 'Telegram ID lookup'
    },
    'ff': {
        'url': os.environ.get('API_FF_URL', 'https://ff-info-ro45.vercel.app/api'),
        'param_name': 'uid',
        'extra_params': {'key': 'Anurag'}, # Keeping the API key hardcoded based on user URL
        'desc': 'Free Fire Player Info'
    },
    'ifsc': {
        'url': os.environ.get('API_IFSC_URL', 'https://ifsc-info-api-eta.vercel.app/ifsc'),
        'param_name': 'ifsc',
        'desc': 'Bank IFSC Code Lookup'
    },
    'insta': {
        'url': os.environ.get('API_INSTA_URL', 'https://instagram-info-api-orpin.vercel.app/profile'),
        'param_name': 'username',
        'desc': 'Instagram Profile Info'
    },
    'vehicle': {
        'url': os.environ.get('API_VEHICLE_URL', 'https://vehicle-full-info.vercel.app/'),
        'param_name': 'vehicle_number',
        'desc': 'Vehicle Number Plate Lookup'
    }
}

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

# Security check function
def is_admin(message):
    return str(message.chat.id) == ADMIN_CHAT_ID

# Basic /start command handler
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if is_admin(message):
        admin_text = (
            f"☠️🔥 *SYSTEM OVERRIDE: ACCESS GRANTED* 🔥☠️\n\n"
            f"😈 Welcome to the dark side, Master! 🌌 The entire digital network bows to your absolute command. 🕹️💥\n\n"
            f"💻 *Terminal connected.* 🔐 *Encryption: RSA-4096.*\n"
            f"🕸️ *Shadow routing established...* 🚀 *Bypassing global firewalls...* ✅ *Done.*\n\n"
            f"🛡️🔪 *Security Status:* Maximum (Offensive Cyber-Protocols Armed) 💣\n"
            f"📡👻 *Connection:* Undetectable 🕶️\n"
            f"👑🆔 *Master ID Recognized:* `{message.chat.id}` 🎯\n\n"
            f"⚡⚙️ *SYSTEM CAPABILITIES & DIRECTIVES:* 🛠️\n"
            f"🌐 Your 5 Vercel backend APIs are fully synchronized 🔄 and awaiting input. ⌨️\n\n"
            f"📝 *Target Commands:* 💡\n"
            f"👉 `/tg <id>` - Telegram Lookup\n"
            f"👉 `/ff <uid>` - Free Fire Info\n"
            f"👉 `/ifsc <code>` - Bank IFSC Details\n"
            f"👉 `/insta <username>` - Instagram Info\n"
            f"👉 `/vehicle <number>` - Vehicle Info\n\n"
            f"🩸🐺 *Remember: We do not just find data in the shadows, we hunt it down and bend it to your will.* ⛓️ *The internet is our playground, and you make the rules.* 🌍👹\n\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"👨‍💻🧠 *Mastermind / Core Developer:* Cyber Insight 💎\n"
            f"👑🔥 *Absolute Creator & Overlord:* Monu (Devid) 🚀🏆\n"
            f"━━━━━━━━━━━━━━━━━━━━\n\n"
            f"⏳ >_ Awaiting your next command, Monu... ⌨️💭"
        )
        bot.reply_to(message, admin_text, parse_mode='Markdown')
    else:
        scary_text = (
            f"🛑🚨 *CRITICAL WARNING: UNAUTHORIZED ACCESS DETECTED* 🚨🛑\n\n"
            f"👁️💀 Who are you? You have just stepped into a highly restricted zone 🚧 and triggered a Level 9 Security Breach! ☢️💣\n\n"
            f"🌐⛓️ This entity belongs strictly to the shadowy network of *Cyber Insight*. 🕶️🌌\n\n"
            f"👁️‍🗨️🔍 *I am watching you.* Your Telegram ID (`{message.chat.id}`) has been recorded 📝 and locked 🔒 in our database. "
            f"👣 Your digital footprint is currently being traced. 📡🛰️\n\n"
            f"⚖️⚔️ This system is governed by the absolute creator, *Monu (Devid)*. 👑🔥 "
            f"He is not someone you want to mess with. 🚫👹 Trespassers are dealt with severely. ☠️🩸\n\n"
            f"⚠️🔥 *LEAVE IMMEDIATELY BEFORE DEFENSIVE PROTOCOLS ARE ENGAGED AGAINST YOUR DEVICE.* 🔥⚠️"
        )
        bot.reply_to(message, scary_text, parse_mode='Markdown')

# Helper function to format JSON beautifully
def format_json_response(data):
    if isinstance(data, dict) or isinstance(data, list):
        formatted = json.dumps(data, indent=2, ensure_ascii=False)
        return f"```json\n{formatted}\n```"
    return str(data)

# Generic handler for the specific API commands
@bot.message_handler(commands=['tg', 'ff', 'ifsc', 'insta', 'vehicle'])
def handle_api_request(message):
    if not is_admin(message):
        bot.reply_to(message, "You are not authorized to use this command.")
        return

    # Extract command (e.g., 'tg' from '/tg 5339638465')
    command_name = message.text.split()[0].replace('/', '').lower()
    config = API_CONFIGS.get(command_name)

    if not config:
        return

    # Extract the target parameter
    command_parts = message.text.split(maxsplit=1)
    query_text = command_parts[1] if len(command_parts) > 1 else ""
    
    if not query_text:
        bot.reply_to(message, f"⚠️ Please provide an input for `{command_name}`. Example: `/{command_name} <target>`", parse_mode='Markdown')
        return
        
    loading_msg = bot.reply_to(message, f"⏳ Hunting data from {config['desc']}...")
    
    try:
        # Build query parameters dynamically based on the specific API requirement
        params = {config['param_name']: query_text}
        
        # Add any extra params if they exist (like the 'key=Anurag' for FF API)
        if 'extra_params' in config:
            params.update(config['extra_params'])
            
        response = requests.get(config['url'], params=params, timeout=15)
        
        if response.status_code == 200:
            try:
                data = response.json()
                result_text = format_json_response(data)
                bot.edit_message_text(f"✅ *Target Extracted ({config['desc']}):*\n\n{result_text}", 
                                      chat_id=message.chat.id, 
                                      message_id=loading_msg.message_id,
                                      parse_mode='Markdown')
            except ValueError:
                bot.edit_message_text(f"✅ *Raw Data Extracted ({config['desc']}):*\n\n`{response.text}`", 
                                      chat_id=message.chat.id, 
                                      message_id=loading_msg.message_id,
                                      parse_mode='Markdown')
        else:
            bot.edit_message_text(f"❌ *API Error:* Status Code `{response.status_code}`\n\nResponse: {response.text}",
                                  chat_id=message.chat.id, 
                                  message_id=loading_msg.message_id,
                                  parse_mode='Markdown')
            
    except Exception as e:
        bot.edit_message_text(f"⚠️ *Connection Failure:* `{str(e)}`",
                              chat_id=message.chat.id, 
                              message_id=loading_msg.message_id,
                              parse_mode='Markdown')

@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def getMessage():
    try:
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return "!", 200
    except Exception as e:
        print(f"Error processing update: {e}")
        return "Error", 500

@app.route('/')
def index():
    return "Bot is running online and secure. ☠️", 200

# Endpoint to manually set the webhook ONE TIME
@app.route('/setup_webhook')
def setup_webhook():
    # Try to get the URL from the request if the environment variable isn't set
    base_url = WEBHOOK_URL
    if not base_url:
        # e.g., https://cyber-osint-jsy2.onrender.com
        base_url = request.url_root.rstrip('/')
        
    if not base_url or 'localhost' in base_url or '127.0.0.1' in base_url:
        return "Cannot determine valid external URL for webhook.", 400
    
    bot.remove_webhook()
    webhook_target = f"{base_url}/{BOT_TOKEN}"
    success = bot.set_webhook(url=webhook_target)
    
    if success:
        return f"Bot is ready for use", 200
    else:
        return "Failed to set Webhook.", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
