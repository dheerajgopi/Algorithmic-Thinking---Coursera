"""Project 1 of Algorithmic Thinking MOOC"""
import random
import matplotlib.pyplot as plot_graph

# Code for making complete graph
def make_er_graph(num_nodes, probability):
    """Returns a complete graph for a given number of nodes"""
    graph_out = {}
    for node in xrange(num_nodes):
        graph_out[node] = set([adj_node for adj_node in \
                            xrange(num_nodes) if adj_node != node \
                                and random.random() < probability])
    return graph_out

# Code for computing in-degree of given graph
def compute_in_degrees(digraph):
    """Returns distribution of in-degrees of nodes in a directed graph"""
    in_degrees = {}
    for node in digraph.keys(): # initializing the result dict with 0's
        in_degrees[node] = 0
    for node in digraph.keys():
        for adj_node in digraph[node]:
            in_degrees[adj_node] = in_degrees.setdefault(adj_node) + 1
    return in_degrees

# Computing in-degree distribution
def in_degree_distribution(digraph):
    """Returns unnormalised distribution of in-degrees"""
    in_degree_distr = {}
    in_degrees = compute_in_degrees(digraph)
    for node in in_degrees.keys():
        in_degree = in_degrees[node]
        in_degree_distr[in_degree] = in_degree_distr.get(in_degree, 0) + 1
    return in_degree_distr

# Normalize distribution
def normalize_distribution(distribution):
    total_nodes = sum(distribution.values())
    return {key : value * 1.0/total_nodes 
        for key, value in distribution.items()}

a = make_er_graph(1000, .05)
b = in_degree_distribution(a)
c = normalize_distribution(b)
if c.get(0, None):
    del c[0]
print b

plot_graph.xscale('log')
plot_graph.yscale('log')
plot_graph.plot(c.keys(), c.values(), 'o')
plot_graph.show()
