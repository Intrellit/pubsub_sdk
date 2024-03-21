import os


def read_event(envelope):
    if envelope.get("secret") == os.getenv("PUBSUB_SECRET"):
        return envelope.get("type"), envelope.get("body")
