from datetime import datetime
import json
import random
import time

from kafka import KafkaProducer


def main():
    producer = KafkaProducer(bootstrap_servers='localhost:9092',
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    for i in range(10):
        producer.send(topic='producer',
                      value={
                          "id": i,
                          "created_at": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                          "color": random.choice(('red', 'rose', 'white')),
                          "year": random.randint(1990, 2021),
                          "humidity" : random.randint(0, 100),
                          "temperature" : random.randint(5, 25),
                          "vibration" : random.randint(0, 5),
                      }
                      )
        time.sleep(0.02)
        print("Message Sent")
