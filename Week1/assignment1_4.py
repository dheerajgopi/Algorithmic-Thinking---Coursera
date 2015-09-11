"""
APP-Q4
Provided code for application portion of module 1
Helper class for implementing efficient version
of DPA algorithm
"""

# general imports
import random
import matplotlib.pyplot as plot_graph

class DPATrial:
    """
    Simple class to encapsulate optimized trials for DPA algorithm
    
    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a DPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_node trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that the number of instances of
        each node number is in the same ratio as the desired probabilities
        
        Returns:
        Set of nodes
        """
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors

def dpa_graph(n, m):
    graph = make_complete_graph(m)
    dpa = DPATrial(m)
    for new_node in xrange(m, n):
        new_neighbours = dpa.run_trial(m)
        graph[new_node] = new_neighbours
    return graph

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

def show_graph(graph):
    dist = in_degree_distribution(graph)
    norm_dist = normalize_distribution(dist)
    # plotting log graph
    del norm_dist[0]
    plot_graph.xscale('log')
    plot_graph.yscale('log')
    plot_graph.plot(norm_dist.keys(), norm_dist.values(), 'o')
    plot_graph.show()

graph = dpa_graph(27770, 12)
show_graph(graph)
