import redis
from aioflask import request, jsonify

from app import app
from app.logic_db import init_new_dialogue, stop_dialogue, stop_list_dialogue
from app.utilities import get_config

redis_db = redis.from_url(get_config()["redis_connect"])


@app.route('/')
@app.route('/ping')
async def ping():
    return "pong"


@app.route('/message', methods=['GET', 'POST'])
async def handler_message():
    if request.content_type == 'application/json':
        user_id = request.json['user_id']
        text = request.json['text']
    else:
        user_id = request.args.get('user_id', '1')
        text = request.args.get('text', 'Hello')

    data = ['user', text]
    redis_db.rpush(user_id, *data)     # запись нового сообщения от пользователя в redis

    conversation, nlp = await init_new_dialogue(user_id)
    result = nlp([conversation], do_sample=False, max_length=1000)
    text_to_user = list(result.iter_texts())[-1][1]

    data = ['bot', text_to_user]
    redis_db.rpush(user_id, *data)      # запись ответного сообщения пользователю в redis

    return jsonify({
        'text': text_to_user
    })


@app.route('/reset', methods=['GET', 'POST'])
@app.route('/stop', methods=['GET', 'POST'])
async def stop():
    if request.content_type == 'application/json':
        return await stop_dialogue(request.json['user_id'])
    return await stop_dialogue(request.args.get('user_id', '1'))


@app.route('/stop_list', methods=['GET', 'POST'])
async def stop_list():
    if request.content_type == 'application/json':
        return await stop_list_dialogue(request.json['user_ids'])
    return await stop_list_dialogue(request.args.get('user_ids', []))
