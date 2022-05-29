from datastructures import tree, tree_nodes
from datastructures.recursive import tree as tree_r
import pytest 

@pytest.mark.parametrize("p,q,excepted", [ (tree_nodes("1 2 3"), tree_nodes("1 2 3"), True),
                                           (tree_nodes("1 2"), tree_nodes("1 N 2"), False), 
                                           (tree_nodes("1 2 1"), tree_nodes("1 1 2"), False), 
                                           (tree_nodes(""), tree_nodes(""), True), 
                                           ])  
def test_is_same_tree(p, q, excepted):
    assert excepted  == tree.isSameTree(p, q)
      
    assert excepted  == tree_r.isSameTree(p, q)