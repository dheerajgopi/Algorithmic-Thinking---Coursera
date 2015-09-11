"""Project 1 of Algorithmic Thinking MOOC"""
EX_GRAPH0 = {0:set([1,2]), 1:set([]), 2:set([])}
EX_GRAPH1 = {0:set([1,4,5]), 1:set([2,6]), 2:set([3]), 3:set([0]),
            4:set([1]), 5:set([2]), 6:set([])}
EX_GRAPH2 = {0:set([1,4,5]), 1:set([2,6]), 2:set([3,7]), 3:set([7]),
            4:set([1]), 5:set([2]), 6:set([]), 7:set([3]),
            8:set([1,2]), 9:set([0,3,4,5,6,7])}

def make_complete_graph(num_nodes):
    """Returns a complete graph for a given number of nodes"""
    graph_out = {}
    for node in xrange(num_nodes):
        graph_out[node] = set([adj_node for adj_node in \
                            xrange(num_nodes) if adj_node != node])
    return graph_out

def compute_in_degrees(digraph):
    """Returns distribution of in-degrees of nodes in a directed graph"""
    in_degrees = {}
    for node in digraph.keys(): # initializing the result dict with 0's
        in_degrees[node] = 0
    for node in digraph.keys():
        for adj_node in digraph[node]:
            in_degrees[adj_node] = in_degrees.setdefault(adj_node) + 1
    return in_degrees

def in_degree_distribution(digraph):
    """Returns unnormalised distribution of in-degrees"""
    in_degree_distr = {}
    in_degrees = compute_in_degrees(digraph)
    for node in in_degrees.keys():
        in_degree = in_degrees[node]
        in_degree_distr[in_degree] = in_degree_distr.get(in_degree, 0) + 1
    return in_degree_distr
