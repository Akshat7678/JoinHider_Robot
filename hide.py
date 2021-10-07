import os
from pyrogram import Client, filters
from pyrogram.types import Message, User

bot = Client(
    "BotNameHere",
     bot_token = os.environ["BOT_TOKEN"],
     api_id = int(os.environ["API_ID"]),
     api_hash = os.environ["API_HASH"]
)

@bot.on_message(filters.new_chat_members)
async def welcome(bot,message):
	try:		
                await message.delete()	
        except:		
                return
	
@bot.on_message(filters.left_chat_member)
async def goodbye(bot,message):
	try:		
                await message.delete()	
        except:		
                return
	
bot.run()
