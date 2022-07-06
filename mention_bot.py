import traceback
import aiogram
from aiogram import Bot, Dispatcher, executor, types, filters
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from datetime import datetime, timedelta
import re
import config
import db

bot = Bot(token=config.BOT_TG_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
bot_db = db.DB()

async def handle_start(message: types.Message, state: FSMContext):
    config.logger.debug(message)
    bot_db.add_user(message.chat.id, message.from_user.id)
    reply_text = "Just send @all to mention everyone"
    await message.reply(reply_text)

async def handle_all(message: types.Message, state: FSMContext):
    config.logger.debug(message)
    bot_db.add_user(message.chat.id, message.from_user.id)

    if re.match(r'.*([^\w]|^)@all([^\w]|$).*', message.text):
        users = bot_db.get_users(message.chat.id)
        mention_text = ""
        for user_id in users:
            mention_text += "[⁠](tg://user?id=" + str(user_id) + ")"

        message_text = "@all" + mention_text
        await bot.send_message(message.chat.id, parse_mode = types.ParseMode.MARKDOWN_V2, text = message_text)
        config.logger.debug(message_text)

async def handle_add_user(message: types.Message, state: FSMContext):
    bot_db.add_user(message.chat.id, message.from_user.id)

def register_handlers_main(dp: Dispatcher):
    dp.register_message_handler(handle_start, commands=['start'])
    dp.register_message_handler(handle_all, filters.Text(contains='@all', ignore_case=False))
    dp.register_message_handler(handle_add_user)

def main():
    register_handlers_main(dp)
    try:
        executor.start_polling(dp, skip_updates=True)
    except:
        traceback.print_exc()
        config.logger.error("Bot crashed")
    finally:
        config.logger.info("Bot stopped")

if __name__ == "__main__":
    main()
