# ============================ #
# ------- VERTEX COVER ------- #
# ============================ #

import sys
from graph import Graph
from algos import *

def main():

    filename = sys.argv[1] if len(sys.argv) == 2 else 'exempleinstance.txt'

    G = Graph.from_text('../test/' + filename)
    G.show(filename)
    print("* algo couplage  :", couplage(G))
    print("* algo glouton   :", glouton(G))
    print("* branch         :", branch(G))
    print("* branch & bound :", branch_bound(G))
    print("* B & B improved :", bb_improved(G))


if __name__ == '__main__':
    main()