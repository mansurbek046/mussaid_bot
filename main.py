from credentials import api_hash, api_id, bot_token
import logging
from pyrogram import Client, filters
from urllib.parse import urlparse, parse_qs
from instagram import instagram

app=Client('mussaid_bot', api_hash=api_hash, api_id=api_id, bot_token=bot_token)

@app.on_message(filters.command('start'))
async def welcome(client, message):
  chat_id=message.chat.id
  await client.send_message(chat_id=chat_id, text="Welcome! Send me media link of Instagram, X and Tiktok or Telegram Story to download...")

@app.on_message()
async def handler(client, message):
  chat_id=message.chat.id
  networks=[
    "www.instagram.com",
    "instagram.com",
    "x.com",
    "www.x.com",
    "mobile.twitter.com",
    "tiktok.com",
    "www.tiktok.com",
    "t.me",
    "telegram.me"
  ]
  if message.text:
    urls=message.text.split()
    # await message.delete()
    count=len(urls)
    for url in urls:
      parsed_url=urlparse(url)
      
      if parsed_url.netloc in networks:
        count=-1
        if "instagram" in str(parsed_url.netloc):
          print(parsed_url, url)
          answer=await instagram(url)
          await client.send_message(chat_id=chat_id, text=filename)
  
    if count==len(urls):
      await client.send_message(chat_id=chat_id, text="Please, Send me link from Instagram, X, TikTok or Telegram Story...")
  
  await client.send_message(chat_id=chat_id, text="message")

if __name__=="__main__":
  app.run()