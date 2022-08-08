# MentionBot

The bot mentions all users in a group when somebody writes '@all' message.

All users should write something to chat first, because the bot has to remember the user and save user's Telegram ID.

Group privacy mode must be disabled for the bot.

## Configuration
Create `user_config.py` file and fill it. For example:
```
DEBUG = False
BOT_TG_TOKEN = "Token for the bot"
USERS_DB_PATH = "./users.db"
```
