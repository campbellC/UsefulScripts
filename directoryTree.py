# This program is designed to build a graph of the directory structures of a
# given folder.
# If no argument is provided it takes the current directory as it's default.
# TODO: What happens if folders have security attached?


# Version 1 takes directory and returns a basic tree of it's contents
#import pdb; pdb.set_trace()
import sys
import os
import networkx as nx

import matplotlib.pyplot as plt

import argparse

parser = argparse.ArgumentParser(description='Short sample app')

parser.add_argument('--ignore_git', help="Ignore .git repositories",action="store_true", default=True)
parser.add_argument('--folder','-f', help="Specify a folder to look at", action="store", default=os.getcwd())
parser.add_argument('--labels','-l',help="Set to True to display labels on picture.",action="store_true",default = False)

args = parser.parse_args()

def makeGraph(x=os.getcwd()):
    """This function will create the graph recursively
    by adding nodes for every file found and then a node + graph
    for any directory"""
    if not x:
        x = os.getcwd()
    G = nx.DiGraph()
    cwd = os.path.abspath(x) # Nodes will always be labelled by absolute path
    G.add_node(cwd) # G will be the graph to return so root it now
    for currentFile in os.listdir(x):
        if args.ignore_git and (str(currentFile) == ".git"):
            continue
        currentAbspath = os.path.join(cwd, currentFile)
        if os.path.isfile(currentAbspath): # In this case just add a node
           G.add_node(currentAbspath)
           G.add_edge(cwd, currentAbspath)
        elif os.path.isdir(currentAbspath): # Now recusively create the tree
            H = makeGraph(currentAbspath)
            G.add_nodes_from(H)
            G.add_edges_from(H.edges())
            G.add_edge(cwd, currentAbspath)
        else:
            raise ValueError("Must be a file")
    return G
def main():

    G = makeGraph(args.folder)
    G = nx.relabel_nodes(G,
                         lambda x :x[ x.rfind("/") + 1:])
    # write dot file to use with graphviz
    # run "dot -Tpng test.dot >test.png"
    #nx.write_dot(G,'test.dot')
    # same layout using matplotlib with no labels
    plt.title(args.folder)
    plt.axis('off')

    nx.draw_networkx(G,with_labels=args.labels,pos=nx.graphviz_layout(G,prog='dot'))
    plt.savefig('graphing.png')


if __name__ == '__main__':
    main()
