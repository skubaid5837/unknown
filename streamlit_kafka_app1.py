import streamlit as st
from kafka import KafkaProducer

# Create Kafka producer to send messages to Kafka topic
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Streamlit app
st.title('Real-time Clickstream Simulation')

# Button to send '1' (Click Event)
if st.button('Send 1 (Click Event)'):
    producer.send('clickstream_topic', value=b'1')
    st.write('Produced: 1 (Click Event)')

# Button to send '0' (No Click Event)
if st.button('Send 0 (No Click Event)'):
    producer.send('clickstream_topic', value=b'0')
    st.write('Produced: 0 (No Click Event)')
