import math
from collections import deque

class DGIM:
    def __init__(self, window_size):
        self.window_size = window_size
        self.buckets = deque()  # store (size, timestamp) for each bucket
        self.current_time = 0

    def _remove_old_buckets(self):
        while self.buckets and self.buckets[0][1] <= self.current_time - self.window_size:
            self.buckets.popleft()

    def add_bit(self, bit):
        self.current_time += 1
        if bit == 1:
            # Create a new bucket for the new 1
            self.buckets.append((1, self.current_time))
            # Merge buckets if needed
            self._merge_buckets()

        # Remove old buckets outside of the window
        self._remove_old_buckets()

    def _merge_buckets(self):
        # Merge buckets to ensure at most 2 of the same size
        size_counts = {}
        for i in range(len(self.buckets)):
            size = self.buckets[i][0]
            if size not in size_counts:
                size_counts[size] = 0
            size_counts[size] += 1
            if size_counts[size] > 2:
                # Merge the two oldest buckets
                self.buckets[i - 1] = (size * 2, self.buckets[i][1])
                del self.buckets[i]
                break

    def count_ones(self):
        total_ones = 0
        for size, timestamp in self.buckets:
            if timestamp > self.current_time - self.window_size:
                total_ones += size
            else:
                # Approximation: include only part of the oldest bucket
                fraction = (self.window_size - (self.current_time - timestamp)) / self.window_size
                total_ones += size * fraction
        return total_ones

# Example usage
dgim = DGIM(window_size=10)
stream = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1]

for bit in stream:
    dgim.add_bit(bit)
    print(f"Approximate count of 1s: {dgim.count_ones()}")
