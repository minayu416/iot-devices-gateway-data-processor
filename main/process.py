import hexdump

from log import logger
from constant import Constant
from main.module.mqtt_subscribe import MQTTSubscriber


# TODO thread or async, queue. (Msg Object)
class MsgProcessor(object):

    def decode(self):
        pass

    def transfer(self):
        pass

    def process(self):
        pass

    def save(self):
        pass

    def work(self):
        pass


msg_processor = MsgProcessor()


def dump_hex(bs: bytes):
    """Convert bytes to hex
    Args:
        bs (bytes):
    Returns:
        TODO string:
    """
    return ':'.join('{:02X}'.format(b) for b in bs)


class MainManager(object):

    # singleton design pattern

    __instance = None

    qos = 0

    # TODO register multiple topics.
    topics = [Constant.DATA_TOPIC, Constant.COMMAND_TOPIC]

    def __new__(cls):
        if not MainManager.__instance:
            MainManager.__instance = object.__new__(cls)
        return MainManager.__instance

    def on_connect(self, client, userdata, flags, rc):
        # subscribe when connected.
        qos = self.qos
        # TODO Implement receive multiple topics.
        topic = self.topics
        client.subscribe(topic, qos=qos)

    def on_message(self, client, userdata, msg):
        msg_topic = msg.topic
        try:
            msg_payload = msg.payload.decode('utf-8')
        except UnicodeDecodeError:
            msg_payload = f'binary:{dump_hex(msg.payload)}'

        # Using log to record.
        logger().info(f"Received topic: {msg_topic}")
        logger().info(f"Received Msg: {msg_payload}")

        # TODO msg_processor
        # TODO open new MsgProcessor Object.

    def start(self):
        # TODO MQTT subscribe
        # TODO change params
        mqtt_subscriber = MQTTSubscriber("subscriber", None, None, "127.0.0.1", 6638, True)
        mqtt_subscriber.subscribe(self.on_connect, self.on_message)

        # listen at on_message
        mqtt_subscriber.connect()
