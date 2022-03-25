"""
Some utility functions used in crawler and windows.
"""

# Split a list into multiple small lists of equal length
def split_list(l,n = 4):
    """
    Args:
        l: The list that needed to be splited. e.g. [p1,p2,p3,p4,p5,..]
        n: Number of elements in each small list after splitting.

    Output:
        [p1,p2,p3,p4,p5,..] -> [[p1,p2,p3,p4],[p5,p6,p7,p8],...]
    """

    output = []
    for i in range(0,len(l),n):
        output.append(l[i:i+n])
    return output

# Simplify long text
def simplify(name):
    """
        Args:
            name: The text that needed to be simplified.
        
        Output:
            Simplified text without any punctuation.

    """

    name = name.replace("."," ").replace(":"," ").replace("?"," ").replace(","," ").strip()
    if len(name) > 100:
        return name[:100]
    return name