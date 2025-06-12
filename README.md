# 🔐 secretThreadsBot

A Python Telegram bot for steganography—hiding a private message inside a public one.

## Features

- **Hide secret messages** within innocuous public messages using basic steganography in Python.
- **Telegram integration**: interact with the bot via Telegram.
- **Easy to extend**: plug in stronger algorithms, add bot commands, integrate with other services.

## Contents

```
.
├── LICENSE
├── README.md
├── bot.py        # Bot logic & Telegram handler
└── main.py       # Startup & configuration
```

## 🔧 Prerequisites

- Python 3.7+
- `python-telegram-bot` (check version compatibility)
- Telegram Bot API token

## 🚀 Setup

1. **Clone the repo**  
   ```bash
   git clone https://github.com/bhargavsai-lingampalli/secretThreadsBot.git
   cd secretThreadsBot
   ```

2. **Create a virtual environment & install dependencies**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # On Windows use `venv\Scripts\activate`
   pip install python-telegram-bot
   ```

3. **Set your Token & run**  
   ```bash
   export TELEGRAM_TOKEN="YOUR_TOKEN_HERE"        # On Windows: set TELEGRAM_TOKEN=...
   python main.py
   ```

## 🤖 Usage

Once running:

- **/start** – welcome and basic instruction.
- **/encode `<public>` | `<secret>`**  
  Hide `<secret>` within `<public>`.  
  Example:  
  ```
  /encode Hello world | MySecret
  ```

- **/decode `<public>`**  
  Extract the hidden message from `<public>`.
- You can launch to your own Telegram group, share the bot, and test steganography live.

## 🧩 Bot Logic Overview

- **`bot.py`** – handles Telegram commands, text parsing, performs hide/reveal operations.
- **`main.py`** – loads `TELEGRAM_TOKEN`, initializes, and starts the bot.
- Hiding technique: e.g., using zero-width characters or simple substring mapping (customizable).

## 🛠️ Customization

- Replace the encoding logic in `bot.py` with more robust methods (e.g., zero-width spaces, bit manipulation, image/audio stego).
- Add more commands: error handling, help docs, usage logs.
- Dockerize or deploy on services like Heroku, AWS Lambda, Azure, or run in GitHub Codespaces.

## 💡 Contribution

Feel free to:

- Improve encoding/decoding algorithms
- Add tests, CI pipelines
- Enhance UX (Markdown support, file stego, bot commands, etc.)

Pull requests are welcome! ☃️

## 📝 License

MIT © Bhargav Sai Lingampalli

---

### ✅ Quick Start in Codespace

1. Open the repo in GitHub Codespaces.
2. In the terminal:
    ```bash
    pip install python-telegram-bot
    export TELEGRAM_TOKEN=<your_token>
    python main.py
    ```
3. Chat with your bot in Telegram and try:

   ```
   /encode Hello world | SecretMsg
   ```