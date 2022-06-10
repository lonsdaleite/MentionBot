import db

bot_db = db.DB()

for chat_id in bot_db.users_db.getall():
    print(chat_id)
    for user_id in bot_db.get_users(chat_id):
        print(user_id)
