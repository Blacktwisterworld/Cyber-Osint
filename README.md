# Cyber OSINT Telegram Bot

A Telegram-based OSINT utility bot for authorized information lookup and
research.

## Features

-   Telegram bot interface
-   Admin-controlled access
-   Multiple lookup commands
-   JSON/text API response handling
-   Automatic handling of large responses
-   Webhook support
-   Flask-based web application

## Commands

  Command      Purpose
  ------------ ----------------------------
  `/start`     Start the bot
  `/help`      Show available commands
  `/tg`        Telegram-related lookup
  `/ff`        Free Fire UID lookup
  `/ifsc`      IFSC information lookup
  `/insta`     Instagram profile lookup
  `/vehicle`   Vehicle information lookup

Use each command according to the prompts provided by the bot.

## Project Structure

``` text
Cyber-Osint/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements

-   Python 3
-   Telegram bot account
-   Access to the APIs used by the bot
-   Required Python packages listed in `requirements.txt`

## Configuration

Keep sensitive credentials outside the source code whenever possible.

Recommended environment variables include:

-   `BOT_TOKEN`
-   `ADMIN_CHAT_ID`
-   `RENDER_EXTERNAL_URL`
-   API-specific configuration values used by the application

Do not publish bot tokens, API keys, or other private credentials in a
public repository.

## Usage

Install dependencies:

``` bash
pip install -r requirements.txt
```

Run the application:

``` bash
python main.py
```

For production, use a WSGI server such as Gunicorn.


## 👤 About the Creator

### Monu (Devid) — Creator & Developer | Cyber Insight

**Monu (Devid)** is the creator and developer behind this project, with a strong interest in **cybersecurity, OSINT, ethical research, automation, and security-focused development**.

His work focuses on building practical tools that bring together **technology, information gathering, automation, and developer-friendly workflows**. The goal is to turn complex technical ideas into useful projects that can be explored, improved, and applied for legitimate research and security purposes.

As a developer, Monu (Devid) is interested in understanding how digital systems, APIs, online platforms, and security workflows work together. Through projects such as this Cyber OSINT Telegram Bot, he explores ways to make information-research workflows faster and easier to use while keeping responsible and authorized use in mind.

### 🧠 Cyber Insight

**Cyber Insight** represents the development and research mindset behind the project:

- 🔎 **OSINT & Digital Research**
- 🛡️ **Cybersecurity & Ethical Security**
- 🤖 **Automation & Telegram Bots**
- 💻 **Python & API Development**
- 🧩 **Developer Tools & Projects**
- 📚 **Learning, Experimentation & Research**

> **Creator:** Monu (Devid)  
> **Role:** Developer & Creator  
> **Focus:** Cyber Insight • OSINT • Cybersecurity • Development • Automation

This project is part of Monu (Devid)'s ongoing journey of learning, building, and experimenting with cybersecurity and developer technologies.

### ⚡ Creator's Vision

> **“Learn the system. Understand the data. Build the tool. Use knowledge responsibly.”**

The aim is not simply to create software, but to keep learning how modern digital systems work and build tools that are useful for **authorized research, education, and cybersecurity awareness**.

## Security

This project should only be used for lawful and authorized
OSINT/research purposes.

Do not use the bot to access, collect, expose, or distribute private
information without authorization. Respect applicable laws, platform
policies, and the privacy of individuals.

## Disclaimer

This project is provided for educational, research, and authorized
security/OSINT purposes. The developer is not responsible for misuse of
the software or information obtained through third-party services.

## License

Add an appropriate license before distributing this project publicly.
