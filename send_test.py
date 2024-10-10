import json
import paho.mqtt.client as mqtt

# Configurações de conexão
broker = "localhost"
port = 1883
topic = "configuracao/dispositivos/id_001"  # Tópico dedicado para configurações
username = "mqtt_user"
password = "mqtt_password"

# Exemplo de dados de configuração em JSON
payload = {
    "dispositivo_id": "id_001",
    "configuracao": {
        "parametro1": "valorA",
        "parametro2": "valorB",
        "timeout": 30
    }
}

# Converter para string JSON
payload_json = json.dumps(payload)

# Configurar cliente MQTT
client = mqtt.Client()
client.username_pw_set(username, password)

# Conectar ao broker
client.connect(broker, port, 60)

# Publicar a mensagem de configuração no tópico
client.publish(topic, payload_json)

# Fechar a conexão
client.disconnect()

print(f"Mensagem de configuração publicada para {topic}")
