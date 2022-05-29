# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.
import algorithms.search as search
from bisect import bisect

class TimeSuite:
    """
    An example benchmark that times the performance of various kinds
    of iterating over dictionaries in Python.
    """
    def time_searchIn100m(self):
        d100m = list(range(100_0000))
        for n in [1,2, 5, 8, 10, 25, 50, 75, 100, 2500, 5000, 7500, 10000, 250_0000, 499_9999, 74_9999, 99_9999, 100_0000]:
            search.index(d100m, n)

    
    
class BiTimeSuite:
    def time_searchIn100m(self):
        d100m = list(range(100_0000))
        for n in [1,2, 5, 8, 10, 25, 50, 75, 100, 2500, 5000, 7500, 10000, 250_0000, 499_9999, 74_9999, 99_9999, 100_0000]:
            bisect(d100m, n)
        
    