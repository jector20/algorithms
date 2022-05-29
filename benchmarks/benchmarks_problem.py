# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.
import problems.bst as bst

class TimeSuite:
    """
    An example benchmark that times the performance of various kinds
    of iterating over dictionaries in Python.
    """
    def setup(self):
        self.tree = list(range(31))
        self.bigtree = list(range(2**20-1))
        
        
    def time_recursive_visit_31(self):
        bst.left_root_right_visit(self.tree)

    def time_recursive_visit_100m(self):
        bst.left_root_right_visit(self.bigtree)
    
    def time_iteration_visit_31(self):
        bst.left_root_right_visit_nr(self.tree)

    def time_iteration_visit_100m(self):
        bst.left_root_right_visit_nr(self.bigtree)
        
def main():
    import timeit
    import tools 
    suite = TimeSuite()
    
    suite.setup()
    
    functions = [suite.time_recursive_visit_31, 
                suite.time_recursive_visit_100m,
                suite.time_iteration_visit_31,
                suite.time_iteration_visit_100m
               ]
               
               
    time = [timeit.Timer(suite.time_recursive_visit_31).timeit(number=1) for function in functions]
    
    for t in time:
        function_time, unit = tools.auto_time_unit(t)
        print(f"{function_time:.2f} {unit}")
    
    
    
    
    
if __name__ == "__main__":
    main()
    