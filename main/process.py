from log import logger

from config import config
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


class MainExecutor(object):

    # Singleton design pattern

    __instance = None

    # permit multiple topics format: [("my/topic", 0), ("another/topic", 2)]
    # [(topic1, qos1), (topic2, qos2)]
    topics = [(Constant.DATA_TOPIC, 0), (Constant.COMMAND_TOPIC, 0)]

    def __new__(cls):
        if not MainExecutor.__instance:
            MainExecutor.__instance = object.__new__(cls)
        return MainExecutor.__instance

    def on_connect(self, client, userdata, flags, rc):
        # subscribe when connected.
        topic = self.topics
        client.subscribe(topic)

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

    def work(self):
        mqtt_subscriber = MQTTSubscriber(config.mqtt.get("subscriber"), None, None,
                                         config.mqtt.get("host"), config.mqtt.get("port"), True)
        mqtt_subscriber.subscribe(self.on_connect, self.on_message)

        # listen at on_message
        mqtt_subscriber.connect()
