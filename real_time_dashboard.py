import streamlit as st
from kafka import KafkaConsumer
from collections import deque

class DGIM:
    def __init__(self, window_size):
        self.window_size = window_size
        self.buckets = deque()
        self.current_time = 0

    def _remove_old_buckets(self):
        while self.buckets and self.buckets[0][1] <= self.current_time - self.window_size:
            self.buckets.popleft()

    def add_bit(self, bit):
        self.current_time += 1
        if bit == 1:
            self.buckets.append((1, self.current_time))
            self._merge_buckets()

        self._remove_old_buckets()

    def _merge_buckets(self):
        size_counts = {}
        for i in range(len(self.buckets)):
            size = self.buckets[i][0]
            if size not in size_counts:
                size_counts[size] = 0
            size_counts[size] += 1
            if size_counts[size] > 2:
                self.buckets[i - 1] = (size * 2, self.buckets[i][1])
                del self.buckets[i]
                break

    def count_ones(self):
        total_ones = 0
        for size, timestamp in self.buckets:
            if timestamp > self.current_time - self.window_size:
                total_ones += size
            else:
                fraction = (self.window_size - (self.current_time - timestamp)) / self.window_size
                total_ones += size * fraction
        return total_ones

# Streamlit app to display the real-time data
def real_time_dashboard():
    st.title('Real-time Clickstream 1s Count Using DGIM')

    dgim = DGIM(window_size=10)
    consumer = KafkaConsumer('clickstream_topic', bootstrap_servers='localhost:9092')

    count_placeholder = st.empty()

    for message in consumer:
        click_event = int(message.value.decode('utf-8'))
        dgim.add_bit(click_event)
        count_placeholder.text(f"Approximate count of 1s in the last 10 clicks: {dgim.count_ones()}")

if __name__ == '__main__':
    real_time_dashboard()
