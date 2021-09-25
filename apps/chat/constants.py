from django.core.validators import RegexValidator

# ---------- #
CONVERSATION_STATUS = (('started', 'Started'), ('in-progress', 'In Progress'), ('resolved', 'Resolved'))
CHAT_STATUS = (('new', 'New'), ('sent', 'Sent'))
SCHEDULE_STATUS = (('created', 'Created'), ('in-progress', 'In Progress'), ('finish', 'Finish'))


# ---------- #
CHAT_MESSAGE_REGEX_PATTERN = r"[^\w\s{}$%_\/~@.#$%^&()!?-]"

ERROR_CHAT_LENGTH_MESSAGE = "Chat message can not be more than 300 characters."
ERROR_CHAT_PATTERN_MESSAGE = "Chat message contains invalid characters."