import time
import random
from kafka import KafkaProducer

# Simulating a real-time clickstream
def generate_clickstream(topic):
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    while True:
        # Simulate a random click (1) or no click (0)
        click_event = random.choice([0, 1])
        producer.send(topic, value=str(click_event).encode('utf-8'))
        time.sleep(1)  # Simulate a new event every second

if __name__ == '__main__':
    generate_clickstream('clickstream_topic')
