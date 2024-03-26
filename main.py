from credentials import api_hash, api_id, bot_token
import logging
from pyrogram import Client, filters

app=Client(api_hash=api_hash, api_id=api_id, bot_token=bot_token)

@app.on_message(filters.command('start'))
async def welcome(client, message):
  chat_id=message.chat.id
  client.send_message(chat_id=chat_id, text="hi")
