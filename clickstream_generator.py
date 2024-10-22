import time
import random
from kafka import KafkaProducer

# Function to simulate real-time clickstream
def generate_clickstream(topic):
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    while True:
        # Randomly choose between 1 (click) or 0 (no click)
        click_event = random.choice([0, 1])
        producer.send(topic, value=str(click_event).encode('utf-8'))
        print(f"Sent: {click_event}")  # Print to see what is being sent
        time.sleep(1)  # Wait for 1 second before sending the next event

if __name__ == '__main__':
    generate_clickstream('clickstream_topic')
