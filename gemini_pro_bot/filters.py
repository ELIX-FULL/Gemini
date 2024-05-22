import os
from telegram import Update
from telegram.ext.filters import UpdateFilter, COMMAND, TEXT, PHOTO
from dotenv import load_dotenv

load_dotenv()

_AUTHORIZED_USERS = [
    i.strip() for i in os.getenv("AUTHORIZED_USERS", "").split(",") if i.strip()
]


class AuthorizedUserFilter(UpdateFilter):
    def filter(self, update: Update):
        if not _AUTHORIZED_USERS:
            return True
        if update.message:  # Check if message exists before accessing attributes
            return (
                update.message.from_user.username in _AUTHORIZED_USERS
                or str(update.message.from_user.id) in _AUTHORIZED_USERS
            )
        return False  # Update doesn't contain a message, so not authorized


AuthFilter = AuthorizedUserFilter()
MessageFilter = AuthFilter & ~COMMAND & TEXT
PhotoFilter = AuthFilter & ~COMMAND & PHOTO
