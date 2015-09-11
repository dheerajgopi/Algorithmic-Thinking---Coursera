"""Project 1 of Algorithmic Thinking MOOC"""

# general imports
import urllib2
import matplotlib.pyplot as plot_graph

# Code for loading citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

citation_graph = load_graph(CITATION_URL)

####################################################

# Code for making complete graph
def make_complete_graph(num_nodes):
    """Returns a complete graph for a given number of nodes"""
    graph_out = {}
    for node in xrange(num_nodes):
        graph_out[node] = set([adj_node for adj_node in \
                            xrange(num_nodes) if adj_node != node])
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

def show_graph():
    dist = in_degree_distribution(citation_graph)
    norm_dist = normalize_distribution(dist)
    # plotting log graph
    del norm_dist[0]
    plot_graph.xscale('log')
    plot_graph.yscale('log')
    plot_graph.plot(norm_dist.keys(), norm_dist.values(), 'o')
    plot_graph.show()

show_graph()

