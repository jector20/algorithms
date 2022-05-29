import problems.bst as bst

def test_left_root_right_visit31():
    tree = list(range(31))
    arr = [15, 7, 16, 3, 17, 8, 18, 1, 19, 9, 20, 4, 21, 10, 22, 0, 23, 11, 24, 5, 25, 12, 26, 2, 27, 13, 28, 6, 29, 14, 30]
    assert bst.left_root_right_visit(tree) == arr
   
def test_left_root_right_visit3():   
    tree = list(range(3))
    arr = [1, 0, 2]
    assert bst.left_root_right_visit(tree) == arr

def test_left_root_right_visit15():   
    tree = list(range(7))
    #   0
    # 1   2
    #3 4 5 6
    arr = [3, 1, 4, 0, 5, 2, 6]
    assert bst.left_root_right_visit(tree) == arr
    
def test_left_root_right_visit():
    tree = list(range(31))
    arr = [15, 7, 16, 3, 17, 8, 18, 1, 19, 9, 20, 4, 21, 10, 22, 0, 23, 11, 24, 5, 25, 12, 26, 2, 27, 13, 28, 6, 29, 14, 30]
    assert bst.left_root_right_visit(tree) == arr
 
def test_empty():
    tree = []
    assert bst.isBST(tree) == False
    
    tree = [0]
    assert bst.isBST(tree) == False
    
    
def test_bst():
    """
     2
    1 3
    """    
    tree = [2, 1, 3]
    assert bst.isBST(tree) == True
    
    """
                            7                        
               3                         11             
         1           5            9              13      
      0     2     4     6     8      10      12     14
    """
    tree = [7, 3, 11, 1, 5, 9, 13, 0, 2, 4, 6, 8, 10, 12, 14]
    assert bst.isBST(tree) == True
    
  
def test_tree():
    """
          6
      1       7
    3   4       9   
    """
    tree = [6, 1, 7, 3, 4, None, 9]
    assert bst.isBST(tree) == False
    
    
    """
    2
        7
      3   8
            1
              4
                5
                  6
              
    """
    tree = [2] + [None, 7] + [None, None, 3, 8] + [None]*7 + [1] + [None]*15 + [4] + [None]*31 + [5] + [None]*63 + [6]
    assert bst.isBST(tree) == False