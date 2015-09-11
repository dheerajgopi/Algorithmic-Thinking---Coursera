"""
Week2: Connected components and graph resilience
"""
from collections import deque
import random

# Breadth-first search
def bfs_visited(ugraph, start_node):
	"""Takes the undirected graph ugraph and the node start_node 
	and returns the set of all nodes that are visited by a BFS 
	from start_node."""
	bfs_queue = deque()
	visited = set()
	bfs_queue.append(start_node)
	visited.add(start_node)
	while bfs_queue:
		curr_node = bfs_queue.pop()
		for neighbor in ugraph[curr_node]:
			if not neighbor in visited:
				visited.add(neighbor)
				bfs_queue.append(neighbor)
	return visited


# Connected components
def cc_visited(ugraph):
	"""Takes the undirected graph ugraph and returns a list of sets, 
	where each set consists of all the nodes in a connected component, 
	NOTE: there is exactly one set in the list for each connected component
	in ugraph and nothing else."""
	remaining_nodes = ugraph.keys()
	connected_components = []
	while remaining_nodes:
		start_node = random.sample(remaining_nodes,1)[0]
		component = bfs_visited(ugraph, start_node)
		connected_components.append(component)
		remaining_nodes = [i for i in remaining_nodes if not i in component]
	return connected_components


def largest_cc_size(ugraph):
	"""Takes the undirected graph ugraph and returns the size 
	of the largest connected component in ugraph."""
	connected_components = cc_visited(ugraph)
	return max([len(c) for c in connected_components] + [0])


# Graph resilience
def compute_resilience(ugraph, attack_order):
	""" Takes the undirected graph ugraph, a list of nodes attack_order and 
	iterates through the nodes in attack_order. For each node in the list,
	the function removes the given node and its edges from the graph and then 
	computes the size of the largest connected component for the resulting graph."""
	resilience = []
	resilience.append(largest_cc_size(ugraph))
	for node_attacked in attack_order:
		remove_node(ugraph, node_attacked)
		resilience.append(largest_cc_size(ugraph))
	return resilience

def remove_node(ugraph, node_to_remove):
	""" helper function: remove a node its links from undirected graph
	"""
	del ugraph[node_to_remove]
	for adj_list in ugraph.values():
		if node_to_remove in adj_list:
			adj_list.remove(node_to_remove)
