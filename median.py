import bisect
import statistics
import math

class RealTimeStats:
    def __init__(self):
        # Initialize the array for data storage
        self.data = []

    def add_data(self, value):
        # Insert value to the data array
        bisect.insort(self.data, value)

    def median(self):
        # Calculate the median
        return statistics.median(self.data)

    def percentile(self, p):
        # Calculate the p-th percentile
        if not 0 <= p <= 100:
            raise ValueError("Percentile rank must be in the range [0, 100]")
        k = (len(self.data) - 1) * (p / 100)
        f = int(k)
        c = int(math.ceil(k))
        if f == c:
            return self.data[int(k)]
        d0 = self.data[f] * (c - k)
        d1 = self.data[c] * (k - f)
        return d0 + d1

# Example usage
stream_stats = RealTimeStats()
stream_stats.add_data(10)
stream_stats.add_data(20)
stream_stats.add_data(30)
print(f"Median: {stream_stats.median()}")  # Output: Median: 20
print(f"90th percentile: {stream_stats.percentile(90)}")  # Output: 90th percentile: 28