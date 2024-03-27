import os
import time

import requests


def read_event(envelope):
    if envelope.get("secret") == os.getenv("PUBSUB_SECRET"):
        return envelope.get("type"), envelope.get("body")
    return None, None


def send_event(type, body, id=None, url="https://pubsub.jpnt.tech/ingress"):
    if not id:
        id = round(time.time() * 1000)
    requests.post(
        url,
        json={
            "secret": os.getenv("PUBSUB_SECRET"),
            "type": type,
            "body": body,
            "id": id,
        },
    )
    return id
