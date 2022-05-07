from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
from transformers import Conversation, ConversationalPipeline
from typing import Tuple, Any
import redis

from app.utilities import get_config, list_segmentation

blenderbot = {
    '90m': 'facebook/blenderbot-90M',
    '400m': 'facebook/blenderbot-400M-distill',
    '1b': 'facebook/blenderbot-1B-distill',
    '3b': 'facebook/blenderbot-3B'
}
mname = blenderbot.get('400m')
model = BlenderbotForConditionalGeneration.from_pretrained(mname)
tokenizer = BlenderbotTokenizer.from_pretrained(mname)

redis_db = redis.from_url(get_config().get("redis_connect"))


async def init_new_dialogue(user_id: str) -> Tuple[Any, Any]:
    from_memory = await list_segmentation(redis_db.lrange(user_id, 0, -1))

    conversation = Conversation()
    for index, message in enumerate(from_memory):
        if message[0] == 'bot':
            conversation.append_response(response=message[1])
        else:
            conversation.add_user_input(text=message[1])
            if not index+1 == len(from_memory):
                conversation.mark_processed()

    return conversation, ConversationalPipeline(model=model, tokenizer=tokenizer)


async def stop_dialogue(user_id: str):
    if redis_db.unlink(user_id):
        return 'ok'


async def stop_list_dialogue(user_ids: list):
    if redis_db.unlink(*user_ids):
        return 'ok'

