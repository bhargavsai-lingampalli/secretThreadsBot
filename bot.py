from pyrogram import Client, filters
from main import encrypt, decrypt

app = Client("invisibieText_bot")
user_input = {}


@app.on_message(filters.command("start") & filters.private)
async def start_command(app, message):
    start_message = f'''
**Hello, [{message.chat.first_name}](tg://user?id={message.chat.id})!!!
Welcome to Invisible Text Bot a prototype bot in development stage.**
    
i can hide a secret message inside a public message.

**use /help for more details**
'''
    await app.send_message(message.chat.id, start_message)


@app.on_message(filters.command('help') & filters.private)
async def help_command(app, message):
    help_message = """    
**what is secret message**?
__A message(text) which is not visible, but present inside a text which can be later retrived using me.__

**what is public message**?
__A message(text) which is visible to read, A coverup message.__
    
use /encrypt command to hide a message
use /decrypt command to retrive the hidden message
    
"""
    await app.send_message(message.chat.id, help_message)


@app.on_message(filters.command('encrypt') & filters.private)
async def encrypt_command(app, message):
    user_input[message.chat.id] = {'step': 1}
    await app.send_message(message.chat.id, 'Enter public message ')


@app.on_message(filters.command('decrypt') & filters.private)
async def decrypt_command(app, message):
    await app.send_message(message.chat.id, 'send the message to decrypt')


@app.on_message(filters.text & filters.private)
async def handle_input(app, message):
    chat_id = message.chat.id
    if chat_id in user_input and user_input[chat_id]["step"] == 1:
        user_input["public_text"] = message.text
        user_input[chat_id]["step"] = 2
        await app.send_message(message.chat.id, 'enter private text')
    elif chat_id in user_input and user_input[chat_id]["step"] == 2:
        user_input["private_text"] = message.text
        public, private = user_input["public_text"], user_input["private_text"]
        result = encrypt(private, public)

        await app.send_message(message.chat.id, f"**Click on below text to copy\n**\n`{result}`")

        del user_input[chat_id]

    else:
        encrypted_message = message.text
        result = decrypt(encrypted_message)
        if result != '':
            await app.send_message(chat_id=message.chat.id, text=f"**the secret text is**\n\n`{result}`",
                                   reply_to_message_id=message.id)
        else:
            await app.send_message(chat_id=message.chat.id,
                                   text=f"**There is No Secret Message in given text.\n\nUse /encrypt to create a secret message**",
                                   reply_to_message_id=message.id)


app.run()
