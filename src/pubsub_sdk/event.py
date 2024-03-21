import os

import requests


def read_event(envelope):
    if envelope.get("secret") == os.getenv("PUBSUB_SECRET"):
        return envelope.get("type"), envelope.get("body")


def send_event(type, body):
    requests.post(
        "https://pubsub.jpnt.tech/ingress",
        json={
            "secret": os.getenv("PUBSUB_SECRET"),
            "type": type,
            "body": body,
        },
    )
