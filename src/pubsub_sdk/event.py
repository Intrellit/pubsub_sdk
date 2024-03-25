import os

import requests


def read_event(envelope):
    if envelope.get("secret") == os.getenv("PUBSUB_SECRET"):
        return envelope.get("type"), envelope.get("body")
    return None, None


def send_event(type, body, url="https://pubsub.jpnt.tech/ingress"):
    requests.post(
        url,
        json={
            "secret": os.getenv("PUBSUB_SECRET"),
            "type": type,
            "body": body,
        },
    )
