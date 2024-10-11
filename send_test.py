import json

import paho.mqtt.client as mqtt

# Configurações do RabbitMQ para MQTT
BROKER = "localhost"
PORT = 1883
TOPIC = "json_schemas"
MQTT_USER = "usuario"
MQTT_PASS = "senha"


# Callback para quando a mensagem for enviada com sucesso
def on_publish(client, userdata, mid):
    print(f" [x] Message {mid} published successfully!")


# Função para enviar a mensagem JSON via MQTT
def send_message(message):
    # Criando o cliente MQTT
    client = mqtt.Client(client_id="mqtt_sender_test", protocol=mqtt.MQTTv311)

    # Definindo as credenciais do RabbitMQ para MQTT
    client.username_pw_set(MQTT_USER, MQTT_PASS)

    # Callback para confirmar a publicação
    client.on_publish = on_publish

    # Conectando ao broker MQTT (RabbitMQ)
    client.connect(BROKER, PORT, 60)

    # Publicando a mensagem
    message = json.dumps(message)
    result = client.publish(TOPIC, message)

    # Verifique o status da publicação
    if result.rc == mqtt.MQTT_ERR_SUCCESS:
        print(f" [x] Sent '{message}' to topic {TOPIC}")
    else:
        print(f" [!] Failed to send message. Error code: {result.rc}")

    # Aguarde para garantir que a mensagem seja publicada
    client.loop_start()
    client.disconnect()


if __name__ == "__main__":
    message = {
        "schema": 1,
        "mac": "8C:AA:85:A3:E2:E0",
        "product": "ICU820",
        "message": "This is a test",
    }

    send_message(message)
