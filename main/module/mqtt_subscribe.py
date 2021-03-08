# reference from https://github.com/minayu416/chest

import paho.mqtt.client as mqtt
import time


# TODO change print function into log()


class MQTTSubscriber(object):
    """MQTT Subscriber, open a subscribe connection and listening to receive data.
    Notes:
        please customize on_connect, on_message by ownself, you can find them refered to down (MQTTFunctionSample).

    """

    def __init__(self, client_id, user, password, mqtt_server, mqtt_port, clean_session=None):
        self.client_id = client_id
        self.client = None
        self.user = user
        self.password = password
        self.mqtt_server = mqtt_server
        self.mqtt_port = mqtt_port
        # Config File: {0: True, 1: False}
        self.clean_session = clean_session

    def subscribe(self, on_connect, on_message):
        """Setting Mqtt Config and Connecting to MQTT.
        Params:
            Please customize your own mqtt function by yourself. You can refer them from MQTTFunctionSample class at
            the bottom.
            on_connect(function):
            on_message(function):
        """
        client_id = self.client_id  # If broker asks client ID.
        self.client = mqtt.Client(client_id=client_id, clean_session=self.clean_session)
        # If broker asks user/password.
        user = self.user
        password = self.password
        self.client.username_pw_set(user, password)

        self.client.on_connect = on_connect
        self.client.on_message = on_message

        self.connect()

    def connect(self):
        try:
            self.client.connect(self.mqtt_server, self.mqtt_port)
            # Using log to record.
            # logger.info("connect succeed")
            # logger.info("Looping...")
            print("connect succeed")
            print("Looping...")
            self.client.loop_forever()

        except KeyboardInterrupt:
            self.client.disconnect()
            print("MQTT disconnect")
            # logger.info("MQTT disconnect")

        except Exception as e:
            # logger.exception(f"MQTT connection problem: {str(e)}")
            print(f"MQTT connection problem: {str(e)}")
            time.sleep(3)
            self.connect()
