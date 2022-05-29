from problems import leftview
from datastructures import tree_nodes
import pytest
 
@pytest.mark.parametrize("tree,excepted", [(tree_nodes("1 2 3 N N 4 6 N N N N N 5 N N 7 N"), [1, 2, 4, 5]),
                                           (tree_nodes("1"), [1]), 
                                           (tree_nodes("1 2 3"), [1, 2]), 
                                           (tree_nodes("1 2 N 4 N N N 8"), [1, 2, 4, 8]),
                                           (tree_nodes("1 N 3 N N N 7 N N N N N N N 16"), [1, 3, 7, 16])
                                           ])    
def test_leftview(tree, excepted):
    assert excepted  == leftview(tree)
    