# receive_json_mqtt.py
import json

import paho.mqtt.client as mqtt

# Configurações do RabbitMQ para MQTT
BROKER = "localhost"
PORT = 1883
TOPIC = "json_schemas"  # Garanta que o tópico esteja correto
MQTT_USER = "usuario"
MQTT_PASS = "senha"


# Callback para quando uma mensagem for recebida
def on_message(client, userdata, message):
    payload = message.payload.decode()
    print(f" [x] Received {payload}")

    # Convertendo o payload de volta para JSON
    json_message = json.loads(payload)
    print(f"Processando a mensagem: {json_message}")


# Função para receber a mensagem JSON via MQTT
def receive_json_message():
    # Criando o cliente MQTT
    client = mqtt.Client(client_id="mqtt_receiver", protocol=mqtt.MQTTv5)

    # Definindo as credenciais do RabbitMQ para MQTT
    client.username_pw_set(MQTT_USER, MQTT_PASS)

    # Definindo o callback para quando uma mensagem for recebida
    client.on_message = on_message

    # Conectando ao broker MQTT (RabbitMQ)
    client.connect(BROKER, PORT, 60)

    # Inscrevendo-se no tópico
    client.subscribe(TOPIC)

    print(f" [*] Subscribed to topic {TOPIC}. Waiting for messages...")

    # Mantendo a conexão ativa para escutar mensagens
    client.loop_forever()


if __name__ == "__main__":
    receive_json_message()
