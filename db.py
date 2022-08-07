import pickledb
import config


class DB:
    def __init__(self):
        self.users_db = pickledb.load(config.USERS_DB_PATH, True)

    def get_users(self, chat_id):
        users = self.users_db.get(str(chat_id))
        if users:
            return users
        else:
            return []

    def add_user(self, chat_id, user_id):
        if not self.users_db.exists(str(chat_id)):
            self.users_db.lcreate(str(chat_id))

        if not self.users_db.lexists(str(chat_id), user_id):
            self.users_db.ladd(str(chat_id), user_id)
            config.logger.debug("User " + str(user_id) + " added to chat: " + str(chat_id))

    def rem_user(self, chat_id, user_id):
        self.users_db.lremvalue(str(chat_id), user_id)
        config.logger.debug("User " + str(user_id) + " removed from chat: " + str(chat_id))
