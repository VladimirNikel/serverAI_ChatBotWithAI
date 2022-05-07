import os


def get_config():
    config = {
        "db_messages": os.getenv("DB_MESSAGES", ""),
        "redis_connect": os.getenv("REDIS_CONNECT", "")
    }
    return config


async def list_segmentation(input_list) -> list:
    delimiter = [b'bot', b'user']
    output_list = [[]]
    for item in input_list:
        output_list[-1].append(item.decode("utf-8"))
        if item not in delimiter:
            output_list.append([])
    output_list.pop()
    return output_list
