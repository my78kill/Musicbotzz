QUEUE = {}

def add(chat_id, song):
    QUEUE.setdefault(chat_id, []).append(song)

def get(chat_id):
    return QUEUE.get(chat_id, [])

def pop(chat_id):
    if chat_id in QUEUE and QUEUE[chat_id]:
        return QUEUE[chat_id].pop(0)